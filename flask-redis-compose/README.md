# Flask-Redis Compose Application

This application is a simple example of how to use Docker Compose to set up and run a multi-container Docker application. In this case, the application consists of a Flask web application that uses Redis as its backend database.

## Overview

Docker Compose allows you to define and run multi-container Docker applications. With Compose, you use a YAML file to configure your application's services, networks, and volumes. Then, with a single command, you create and start all the services defined in your configuration.

This Flask-Redis application demonstrates the power of Docker Compose for local development environments, making it easy to deploy a web application and its dependencies with a single command.

## Prerequisites

Before you begin, ensure you have Docker installed on your system.

## Getting Started

To get started with the Flask-Redis Compose application, follow these steps:

### Build and Run with Docker Compose

From the project directory, start up the application by running:

```bash
docker compose up -d --build
```

This command builds the images for the application if they don't exist (in this case, the Flask application), downloads any images that are not yet available locally (in this case, Redis) and starts the containers.

When you're done using the app, stop it by running:

```bash
docker compose down
```

### Access the Application

Once the containers are up and running, you can access the Flask application by navigating to http://localhost:5000 in your web browser.

## Architecture

This application is composed of two services:

* Flask Application: A simple Python web application built with the Flask framework. It serves a web page and performs operations against a Redis database.
* Redis: An open-source data structure store, used as a database, cache, and message broker.
  
These services are defined in the docker-compose.yml file.

### Communication between containers

Docker compose uses Docker to establish a virtual network over which containers can communicate. Each service name in the compose file functions as a DNS name on those virtual networks. In advanced settings, multiple named networks can be created to isolate traffic between different containers.

### Configuring containers with environment variables

The environment section of a service configuration allows you to pass environment variables into the container, which can be accessed by code in order to configure them. In this case, the Flask application is configured with the name of the Redis host on the virtual network.

### Communication with the host network

To make the Flask application reachable from a web browser, the port on which it's listening for HTTP traffic is mapped to a host port. This allows for access to the web application from outside Docker containers.

### Persistence and volume mapping

To make the app's visitor count persistent between runs, a Docker volume is created and mapped to `/data` in the container's filesystem. `/data` is where the Dockerized version of Redis stores its state, and the Docker volume's contents persist even when the application is not running. Without storing data in a host volume, the app will "forget" the visitor count when Redis is shut down.

## Conclusion

This Flask-Redis Compose application demonstrates how Docker and Docker Compose can be used to easily develop and deploy multi-container applications. By defining your application's environment in a Docker Compose file, you can achieve consistent, reproducible environments across different usage scenarios.