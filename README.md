# super-duper-enigma
Deploying a Streamlit app to GCP incorporating LLM

I named my project gemini-chat.

* clone the github repo onto google cloud platform through the cloud terminal

in the home directory of the cloud terminal you can clone the git repo using

`git clone https://github.com/nschantz21/super-duper-enigma.git`

* set up the google cloud registry for storing artifacts (docker image)

`us-central1-docker.pkg.dev/gemini-chat-448423/streamlit-app`

* in google cloud build the docker image

`docker build -t latest .`

* add a new tag to the docker image

`docker tag [DOCKER_IMAGE_NAME] us-central1-docker.pkg.dev/gemini-chat-448423/streamlit-app/latest:latest`

* push the built docker image to gcr

```{bash}
docker push us-central1-docker.pkg.dev/gemini-chat-448423/streamlit-app/latest
```

* deploy the image to google cloud run

```{bash}
gcloud run deploy streamlit-app \
    --image us-central1-docker.pkg.dev/gemini-chat-448423/streamlit-app/latest \
    --platform managed \
    --region us-central1 \
    --allow-unauthenticated
```
You can also do this through the CloudRun UI

* check the cloudrun logs in log explorer directly or through the cloud run UI


