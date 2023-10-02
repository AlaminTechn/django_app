# Use the official Python 3.8 image as the base image
FROM python:3.8
# Set an environment variable to ensure Python output is not buffered (helpful for logging)
ENV PYTHONUNBUFFERED 1

# Copy the requirements.txt file from the host machine to the container's current directory
COPY requirements.txt ./
# install all files from requiremnets.txt to the container's current directory'
RUN pip install -r requirements.txt
# install all files from the host machine to the container's current directory'
COPY . .
# Set the working directory inside the container to /app
WORKDIR /app
# Copy all files from the host machine to the /app directory inside the container (redundant, already copied above)
COPY . /app
# Run the entrypoint.sh script using bash
RUN bash entrypoint.sh
# Expose port 3030 to allow external connections to this port (not necessary for local development)
EXPOSE 3030
# Define the entry point command for the container
ENTRYPOINT ["python", "manage.py", "runserver", "0.0.0.0:3030"]