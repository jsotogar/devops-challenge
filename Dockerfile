# Use an official Python runtime as a parent image
FROM python:3.9-slim-buster

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Make port 8888 available to the world outside this container
EXPOSE 8888

# Define environment variable for API key
ENV API_KEY 2f5ae96c-b558-4c7b-a590-a501ae1c3f6c

# Run app.py when the container launches
CMD ["python", "main_v2.py"]