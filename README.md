# machine_learning_project

This is the first machine learning project

To setup CI/CD Pipeline in Heroku we need 3 Information

1. Heroku_Email : meerajangra1974@gmail.com
2. Heroku_API_KEY : 9a37fbc0-87e1-4b61-94e8-4547b932a7d9
3. Heroku_App_Name : ml-project-regression-app

BUILD DOCKER IMAGE
```
docker build -t <image_name>:<tagname> .
```

> NOTE: Image name for docker must be in lowercase.

To list Docker images
```
docker images
```

Run docker images
```
docker run -p 5000:5000 -e PORT=5000 <IMAGE_ID>
```

To check running container in docker
```
docker ps
````

To stop docker container
```
docker stop <contained_id>
```
