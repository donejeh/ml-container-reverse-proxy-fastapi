# Docker Compose Setup with Nginx Reverse Proxy on multiple machine learning models
## Template for running multiple machine learning models

This repository contains a Docker Compose configuration for running multiple backend services behind an Nginx reverse proxy. The setup allows you to access different services using friendly URLs instead of using port numbers.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Configuration Overview](#configuration-overview)
- [Getting Started](#getting-started)
- [Usage](#usage)

## Prerequisites
- Docker: Make sure you have Docker installed on your machine. You can download it [here](https://www.docker.com/get-started).

## Configuration Overview
The Docker Compose configuration includes the following services:
- Nginx: Acts as a reverse proxy to route incoming HTTP requests to different backend services.
- Backend Services: Multiple backend services (e.g., FastAPI applications) running on different ports.

The Nginx configuration (`nginx.conf`) defines server blocks for each backend service, allowing you to access them through friendly URLs. For example:
- `http://localhost/translate` -> `model_translate` service
- `http://localhost/query` -> `model_query` service
- `http://localhost/translate_srt` -> `model_translate_srt` service
- `http://localhost/transcribe` -> `model_transcribe` service

## Getting Started
1. Clone this repository to your local machine:
```
git clone 
```

2. Build the project 
```
docker-compose build
```

3. Run the project

```
docker-compose up

```

You can replace the dummy model folders with your desire works and also configure the nginx file however you wish.

cheer