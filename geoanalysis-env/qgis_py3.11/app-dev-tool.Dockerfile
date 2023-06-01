# Start with Ubuntu 22.04
FROM ubuntu:22.04

# Set the working directory
WORKDIR /app

# Disable prompts during package installations
ENV DEBIAN_FRONTEND=noninteractive

# Update and install dependencies
RUN apt-get update && \
    apt-get install -y software-properties-common

#---------------------------------------------------------
# Add SSL certs (remove this if not an ARUP user)
COPY ./build/*.crt /usr/local/share/ca-certificates/
#---------------------------------------------------------

# Update and install dependencies, add SSL certs, add deadsnakes repo, and install Python
RUN apt-get update && \
    apt-get install -y software-properties-common curl && \
    apt-get update && \
    update-ca-certificates && \
    apt-get install -y python3.11 python3-venv python3-pip


# Install QGIS dependencies
RUN apt-get install -y gnupg software-properties-common && \
    add-apt-repository ppa:ubuntugis/ppa && \
    sed -i 's/http:\/\/archive.ubuntu.com/http:\/\/us.archive.ubuntu.com/g' /etc/apt/sources.list && \
    apt-get update --fix-missing && \
    apt-get install -y qgis python3-qgis qgis-plugin-grass

# Copy & install requirements.txt to the container
COPY requirements.txt .
RUN pip install -r requirements.txt

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
ENTRYPOINT [ "python" ]