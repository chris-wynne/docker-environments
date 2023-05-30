# Start with Ubuntu 23.04
FROM ubuntu:23.04

# Set the working directory
WORKDIR /app

# Disable prompts during package installations
ENV DEBIAN_FRONTEND=noninteractive

# Update and install dependencies
RUN apt-get update && \
    apt-get install -y software-properties-common

#add SSL certs (remove this if not an ARUP user)
#---------------------------------------------------------
COPY ./build/*.crt /usr/local/share/ca-certificates/
RUN apt-get install -y curl && \
    apt-get update && \
    update-ca-certificates
#---------------------------------------------------------

# Add deadsnakes repo
#RUN add-apt-repository ppa:deadsnakes/ppa

RUN apt-get update && \
    apt-get install -y software-properties-common python3.11 python3-venv python3-pip

# Install QGIS dependencies
RUN apt-get install -y gnupg software-properties-common && \
    add-apt-repository ppa:ubuntugis/ppa && \
    sed -i 's/http:\/\/archive.ubuntu.com/http:\/\/us.archive.ubuntu.com/g' /etc/apt/sources.list && \
    apt-get update --fix-missing && \
    apt-get install -y qgis python3-qgis qgis-plugin-grass

# Create a virtual environment and activate it
RUN python3.11 -m venv --system-site-packages venv
ENV PATH="/app/venv/bin:$PATH"

# Copy & install requirements.txt to the container
COPY requirements.txt .
RUN pip install -r requirements.txt

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
ENTRYPOINT [ "python3" ]