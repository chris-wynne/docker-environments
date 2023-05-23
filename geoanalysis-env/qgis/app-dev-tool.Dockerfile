# Start with Ubuntu 20.04
FROM ubuntu:20.04

# Set the working directory
WORKDIR /app

# Disable prompts during package installations
ENV DEBIAN_FRONTEND=noninteractive

# Update package index and upgrade packages
RUN apt-get update && apt-get upgrade -y

#add SSL certs (remove this if not an ARUP user)
#---------------------------------------------------------
COPY ./build/*.crt /usr/local/share/ca-certificates/
RUN apt-get install -y curl && \
    apt-get update && \
    update-ca-certificates
#---------------------------------------------------------

# Install Python 3 and pip
RUN apt-get install -y python3 python3-pip

# Install QGIS dependencies
RUN apt-get install -y gnupg software-properties-common && \
    add-apt-repository ppa:ubuntugis/ppa && \
    sed -i 's/http:\/\/archive.ubuntu.com/http:\/\/us.archive.ubuntu.com/g' /etc/apt/sources.list && \
    apt-get update --fix-missing && \
    apt-get install -y qgis python3-qgis qgis-plugin-grass

# Copy requirements.txt to the container
COPY requirements.txt .

# Install Python dependencies
RUN pip3 install -r requirements.txt

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
ENTRYPOINT [ "python3" ]