# Start with Ubuntu 20.04
FROM python:3.11-slim as build

# Set the working directory
WORKDIR /app

COPY requirements.txt .

# Install Python dependencies
RUN pip3 install -r requirements.txt

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
ENTRYPOINT [ "python3" ]