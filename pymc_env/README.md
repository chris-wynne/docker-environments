# docker_pymc_demo
Demo setting up docker container for containerised development using conda

## Installing Docker

### Docker desktop

Install docker desktop: "https://www.docker.com/products/docker-desktop/"

### Install ubuntu for windows

This can be installed from the windows store.

### Install WSL2

Guide: "https://learn.microsoft.com/en-us/windows/wsl/install"

## VS code extensions

Recommended vs code extensions.  

Remote - WSL

Dev Container - you need this to remote access your container.

Docker

## Container Set up guide

This uses the docker files located within this directory to set up an environment. It mounts any files or folders located in this directory to the "app" folder within the container.
\
\
To ignore files add them to the .dockerignore file.

1. To run the prebuilt compose file & generate an image type in bash: "docker-compose build". This may take a while the first time depending on your requirements.

3. To generate a container called "pymc_dev" type: "docker-compose up -d".

4. Check the container is running: "docker ps"

5. From here click the blue icon in the bottom left of VS code. Select "Attach to running container".

6. This should open a vscode window. You will need to navigate to the "app" folder

You will need to install your vscode extensions in this window as it is essentially running on a new pc. These will be saved to the container. 

Also when selecting your python interpreter make sure you select the environment created via the yml file not base python. 

## Container Close down

To close down and remove containers & images enter the below commands into bash:

1. To stop container enter: "docker stop pymc_dev".

2. To remove container enter: "docker rm pymc_dev".

3. To stop & remove container enter: "docker compose down".

4. To remove image enter: "docker rmi pymc_env".

## Helpful video guides for set up

Create a Python Dev Environment with Docker and VS Code | NetDevOps and PyATS part 1: https://www.youtube.com/watch?v=k8H0KCtsTR8&t=218s \
Docker VSCode Python Tutorial // Run your App in a Container : https://www.youtube.com/watch?v=jtBVppyfDbE

## PyMC installation for Linux

https://github.com/pymc-devs/pymc/wiki/Installation-Guide-(Linux)

## PyMC Documentation

https://www.pymc.io/projects/docs/en/latest/learn/core_notebooks/pymc_overview.html