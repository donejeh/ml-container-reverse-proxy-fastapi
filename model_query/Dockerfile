# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory to /app
# /app in the docker container
WORKDIR /app

# Copy the current directory contents into the container
#  at /app inside the docker container
COPY . /app

# Install any needed packages specified in requirements.txt
# this file contains any package
RUN pip install -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Run the FastAPI application
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "80"]
