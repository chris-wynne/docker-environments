# Start with Ubuntu 22.04
FROM ubuntu:22.04

# Set the working directory
WORKDIR /app

# Disable prompts during package installations
ENV DEBIAN_FRONTEND=noninteractive

# Update package index, upgrade packages, and install dependencies
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y curl python3 python3-pip gnupg software-properties-common && \
    rm -rf /var/lib/apt/lists/*

# Add SSL certs (remove this if not an ARUP user)
# ---------------------------------------------------------
COPY ./build/*.crt /usr/local/share/ca-certificates/
RUN update-ca-certificates
# ---------------------------------------------------------

# Install QGIS dependencies
RUN apt-get update && \
    apt-get install -y qgis python3-qgis qgis-plugin-grass && \
    rm -rf /var/lib/apt/lists/*

# Copy requirements.txt to the container
COPY requirements.txt .

# Install Python dependencies
RUN pip3 install -r requirements.txt

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
ENTRYPOINT [ "python3" ]