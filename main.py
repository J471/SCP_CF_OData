from flask import Flask, jsonify
from cfenv import AppEnv

import requests
import base64


app = Flask(__name__)

def scp_connect(dest_name,dest_uri,dest_client):
    ######################################################################
    ############### Step 1: Read the environment variables ###############
    ######################################################################

    env = AppEnv()
    uaa_service = env.get_service(name='uaa_service')
    dest_service = env.get_service(name='destination_service')
    sUaaCredentials = dest_service.credentials["clientid"] + ':' + dest_service.credentials["clientsecret"]

    #######################################################################
    ##### Step 2: Request a JWT token to access the destination service ###
    #######################################################################

    headers = {'Authorization': 'Basic '+base64.b64encode(sUaaCredentials), 'content-type': 'application/x-www-form-urlencoded'}
    form = [('client_id', dest_service.credentials["clientid"] ), ('grant_type', 'client_credentials')]

    r = requests.post(uaa_service.credentials["url"] + '/oauth/token', data=form, headers=headers)

    #######################################################################
    ###### Step 3: Search your destination in the destination service #####
    #######################################################################

    token = r.json()["access_token"]
    headers= { 'Authorization': 'Bearer ' + token }

    r = requests.get(dest_service.credentials["uri"] + '/destination-configuration/v1/destinations/' + dest_name, headers=headers)

    #######################################################################
    ############### Step 4: Access the destination securely ###############
    #######################################################################

    destination = r.json()
    token = destination["authTokens"][0]    
    headers= { 'Authorization': token["type"] + ' ' + token["value"], 'Accept': 'application/json'}   
    
    if dest_client:
        dest_client = '?sap-client=' + dest_client
    else:
        #Read sap-client from Destinations configuration
        dest_client = '?sap-client=' + destination["destinationConfiguration"]["sap-client"]

    r = requests.get(destination["destinationConfiguration"]["URL"] + dest_uri + dest_client, headers=headers)

    return r


@app.route('/odata_es5')
def odata_es5():
    sDestinationName = 'SAP_Gateway'
    sURI = '/sap/opu/odata/sap/EPM_REF_APPS_SHOP_SRV/Products'
    #Client number can be defined here to override default client in Destinations
    sClient = ''

    r = scp_connect(sDestinationName, sURI, sClient)
    results = r.json()

    return jsonify(**results)



@app.route('/odata_nwd')
def odata_nwd():
    headers= { 'Accept': 'application/json' }
    
    r = requests.get('https://services.odata.org/V2/Northwind/Northwind.svc/Products', headers=headers)
    results = r.json()

    return jsonify(**results)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
