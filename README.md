# Docker Guides

Docker set up guides for containerised development.

## Why use docker for containerised development?

Docker allows you to containerise develpment for repeatability. This lets users set up, share and run environments without running into OS issues. You also don't need to install unnecessary software.

## Software requirments

These guides are set up using the below recomneded software & extensions.

### Docker desktop

Install docker desktop: "https://www.docker.com/products/docker-desktop/"

### Install WSL2

Guide: "https://learn.microsoft.com/en-us/windows/wsl/install"

### Install Git

### VS code extensions

Remote - WSL \
Dev Container \
Docker

### Helpful guides for set up

Create a Python Dev Environment with Docker and VS Code | NetDevOps and PyATS part 1: https://www.youtube.com/watch?v=k8H0KCtsTR8&t=218s \
Docker VSCode Python Tutorial // Run your App in a Container : https://www.youtube.com/watch?v=jtBVppyfDbE

## Set up guides

### Running vscode within a basic container

This will let you set up a simple container for development, you code and install packages from within the container. \
\
In bash enter the below commands. You can replace the image "python" with another from docker hub. \
\

1. Download base docker image: "docker pull python"
2. Start running a container in the background: "docker run -d -i --name pythondevs python bash"
3. Check the container is running: "docker ps"
\
From here click the blue icon in the bottom left of VS code. \
Select "Attach to runing container". \
This should open up a new vs code window, this will allow you to develop within the container. \
To stop container enter: "docker stop pythondevs". \
To remove container enter: "docker rm pythondevs". \
To remove image enter: "docker rm python".

### Docker compose

This uses the docker files located within this directory to set up an environment. This allows you options to customize set up, copy local files and mount local drives.\

1. To run the prebuilt compose file simply type in bash: "docker compose run". This may take a minute.
2. To generate a container called "dev_con" type into bash: "docker run -d -i geo_analysis_conda".
3. Check the container is running: "docker ps"
\
You can now open the container using VS code.
