# Docker Guides

Docker set up guides for containerised development. Each folder contains set up for a specific development environment.

## Why use docker for containerised development?

Docker allows you to containerise development for repeatability. This lets users set up, share and run environments without running into OS issues. You also don't need to install unnecessary software.

## Software requirements

The README guides featured in these folders are set up using the below recommended software & extensions.

### Docker desktop

Install docker desktop: "https://www.docker.com/products/docker-desktop/"

### Install WSL2

Guide: "https://learn.microsoft.com/en-us/windows/wsl/install"

### Install Git

https://gitforwindows.org/

### VS code extensions

Remote - WSL \
Dev Container \
Docker

### Helpful video guides for set up

Create a Python Dev Environment with Docker and VS Code | NetDevOps and PyATS part 1: https://www.youtube.com/watch?v=k8H0KCtsTR8&t=218s \
Docker VSCode Python Tutorial // Run your App in a Container : https://www.youtube.com/watch?v=jtBVppyfDbE

## Basic Set up guide

### Running vscode within a basic container

This will let you set up a simple container for development, you code and install packages from within the container. \
\
In bash enter the below commands. You can replace the image "python" with another from docker hub.

1. Download base docker image: "docker pull python"
2. Start running a container in the background: "docker run -d -i --name pythondevs python bash"
3. Check the container is running: "docker ps"
4. From here click the blue icon in the bottom left of VS code. Select "Attach to running container".

You should now have a new vs code window, this will allow you to develop within the container. \

### Close down

To close down and remove containers & images enter the below commands into bash:

1. To stop container enter: "docker stop pythondevs". \
2. To remove container enter: "docker rm pythondevs". \
3. To remove image enter: "docker rm python".
