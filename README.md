# super-duper-enigma
Deploying a Streamlit app to GCP incorporating LLM

* clone the github repo onto google cloud platform through the cloud terminal
* set up the google cloud registry for storing artifacts (docker image)
* in google cloud build the docker image
* push the built docker image to gcr
* deploy the image to google cloud run

```{bash}
gcloud run deploy streamlit-app \
    --image gcr.io/[PROJECT_ID]/streamlit-app \
    --platform managed \
    --region [REGION] \
    --allow-unauthenticated

```

