# Consume OData SAP Gateway Service by using Python Flask REST API application in SAP Cloud Platform - Cloud Foundry
A sample of integration between SAP Gateway OData service, Python Flask REST API and SAP Cloud Platform - Cloud Foundry

## Table of contents
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installing](#installing)
* [Running the Tests](#running-the-test)


## Getting Started

When I explore SAP Conversational AI (CAI) - formerly known as Recast.AI - I started with plan in mind of connecting the Chatbot to SAP backend. End users interacts with SAP backend, passing or retrieving information via Chatbot interface.

At the time this repository is published, it was difficult to find information out there on how the REST API can consume OData service in SAP Gateway, especially on the SAP Cloud Platform (SCP) Cloud Foundry (CF) setup, destination configuration and authentication handling.

I created this repository to put pieces of small puzzle into one place and for my own documentation and reference.

Steps and codes in this repository can be used for your own project and exploration.

HAPPY exploring!

## You will learn

1. Create Destination in SAP CF
2. Create a Destination Service Instance in SAP CF
3. Create an Extended Application Service User Account & Authentication - XSUAA Service Instance in SAP CF
4. Develop and deploy Python application to SCP CF

## Scope & Scenario

A Python application will be desployed in SCP CF as a REST API.

SAP Gateway Demo System ES5 (ES5) is used as the SAP Gateway and backend. ES5 has quite a number of OData services that we can consume in our Python application.

HTTP call will trigger Python application to retrieve information from SAP backend via OData service.

In SAP CAI context, you can use this Python application as webhook endpoint:

![CAI Webhook endpoint](/images/cai_webhook_endpoint.jpg)

## Prerequisites

1. Basic understanding of differences between SCP environments: Neo, Cloud Foundry, ABAP.

  The below SAP Help page link will give you basic idea of different development environments:
  https://help.sap.com/viewer/65de2977205c403bbc107264b8eccf4b/Cloud/en-US/ab512c3fbda248ab82c1c545bde19c78.html

  This SAP blog post also has a good summary on differences between Neo and Cloud Foundry environment:  
  https://blogs.sap.com/2019/02/24/sap-cloud-platform-environment-cloud-foundry-vs-neo/


2. SAP Cloud Platform account

  How can I get account on SAP Cloud Platform? You do not have to worry. SAP offers UNLIMITED duration of a free trial account on SCP Neo environment :)

  You may refer to below article on how to get one:  
  https://developers.sap.com/tutorials/hcp-create-trial-account.html


3. Cloud Foundry Trial environment

  In Prerequisites No. 1, you learnt that Cloud Foundry environment offers deployment of Python application.

  SAP offers 90 days of trial duration. Your setup and configuration will be removed once expired. However, you can reapply a new one.

  You can follow the below tutorial to get a Cloud Foundry trial account:  
  https://developers.sap.com/tutorials/cp-cf-create-account.html

4. Cloud Foundry Command Line Interface (CLI)

  Although we can deploy the application directly in SCP cockpit, but in this document, I use Cloud Foundry CLI to deploy the application.

  You may refer to step 4 - 6 in this tutorial, to download and setup your CLI to connect to your Cloud Foundry environment:  
  https://developers.sap.com/india/tutorials/hcp-cf-getting-started.html


5. SAP Gateway Demo System ES5 account



### Installing

A step by step series of examples that tell you how to get a development env running

Say what the step will be

```
Give the example
```

And repeat

```
until finished
```

End with an example of getting some data out of the system or using it for a little demo

## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags).

## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc
