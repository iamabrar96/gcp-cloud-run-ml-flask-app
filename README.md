## Deploying a Dockerized ML Model Using Flask on Google Cloud Run
This guide provides step-by-step instructions to deploy a machine learning model, encapsulated in a Docker container and served via Flask, on Google Cloud Run.

# Prerequisites
A Google Cloud account.
Docker installed on your local machine.
Google Cloud SDK (gcloud CLI) installed. Install the gcloud CLI.

Steps to Deploy
1. Create a Google Cloud Project
Log in to Google Cloud Console: Go to Google Cloud Console.
Create a New Project:
Navigate to IAM & Admin -> Manage resources.
Click on Create Project.
Enter your project name and note down the generated project ID.
2. Set Up Google Cloud SDK

Install Google Cloud SDK: Follow the installation instructions for your operating system.

Initialize gcloud:

``
gcloud init
``

Follow the prompts to set your default project and region.

3. Enable Required APIs

Enable the Artifact Registry API to allow pushing 

Docker images:


``
gcloud services enable artifactregistry.googleapis.com --project=YOUR_PROJECT_ID
``

4. Authenticate Docker with Google Cloud
Authenticate Docker to use the Google Container Registry:

``
gcloud auth configure-docker
``

5. Build and Push Docker Image

Build the Docker Image:

``
docker build -t gcr.io/YOUR_PROJECT_ID/ms-temp-prediction .
``

Push the Docker Image to Google Container Registry:

``
docker push gcr.io/YOUR_PROJECT_ID/ms-temp-prediction
``

6. Deploy to Google Cloud Run

Deploy the Docker image to Google Cloud Run:

``
gcloud run deploy ms-temp-prediction --image gcr.io/YOUR_PROJECT_ID/ms-temp-prediction --platform managed --region your region --project YOUR_PROJECT_ID
``

7. Access Your Deployed Service
Once deployed, Google Cloud Run will provide a URL for your service. You can access your Flask application via this URL.

Additional Notes

Source Name: The source name (ms-temp-prediction in this example) is a free text field. You can specify any name you prefer for your Docker image.

Region: Choose the region closest to your user base from the list of supported Google Cloud regions.


# Conclusion
By following these steps, you can successfully deploy a Dockerized machine learning model using Flask on Google Cloud Run. This setup allows your model to scale seamlessly with demand while leveraging the robust infrastructure of Google Cloud.

For more details, refer to the Google Cloud Run documentation.

This README provides a structured and clear guide for deploying a Dockerized ML model using Flask on Google Cloud Run. It includes all necessary steps, commands, and explanations to help users understand and complete the deployment process.