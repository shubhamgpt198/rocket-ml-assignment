
# RocketML Assignment

**Flask App**

*app.py* : Flask App which uses GPT-3 API from openAI for sentiment analysis. Also detectes the language and topic.

**Dockerization**

*Dockerfile* : Dockerfile to create container image for Flask App.

**CI/CD**

*jenkinpipeline* : contains script to for jenkins CI/CD pipeline. It uses git repo code to build docker pushes it to gcr and then deploys it to Google Kubernetes Cluster. *deployemt.yaml* and *service.yaml* contain the files for kubernetes deployment for workload and service. Apart from this there is a need of secret.yaml which is used to fetch the container image from gcr to GKE.  pipeline can triggered using url. url and secret.yaml files are shared via mail.

Note: You need to provide Open AI API Key in deployment file.

**Infra Automation**

*main.tf*: contains terraform script to create a Kubernetes Cluster on GCP.

**Load Testing with JMeter**


**Postman Collection**

*RocketML-Assignment.postman_collection.json* file contains the collection.






