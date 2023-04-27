# Use an official Python runtime as a parent image
FROM python:3.9-slim-buster

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Set environment variable for Flask
ENV FLASK_APP app.py

# Expose port 5000 for the Flask app
EXPOSE 5000

# Copy the database file into the container
COPY database.db /app

# Run app.py when the container launches
CMD ["flask", "run", "--host=0.0.0.0"]
