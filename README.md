# Docker
You will need docker on your machine for this exercise. You could install docker on your local machine (Windows)
by following the instructions in the following link.
https://docs.docker.com/desktop/windows/install/

# Docker-compose
We will be using docker-compose in this exercise. The docker-compose will be used to orchestrate multiple docker containers.
It is a great tool that can mimic the behavior of Kubernetes if don't have access to Kubernetes environment. 
If you have installed Docker Desktop in your machine, then that comes with docker-compose.

# Nginx
We will be using the latest version of nginx docker image from the Docker hub. Nginx is used as reverse proxy 
to implement API gateway.

# Flask
Simple Flask API will be written in Python to mimic the behavior of backend services.

# API test via Postman
Test by sending GET request to the 0.0.0.0:9090/backend_path

i.e.: backend_path -> api/v1/search/id/1

# Build and run

Build
```
docker-compose build

```

Run
```
docker-compose up

```