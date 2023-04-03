# QGIS & geospatial development environment

This docker file installs QGIS and python libraries for geospatrial analysis. This allows you to build qgis programmatically projects through python scripts.

# Software requirements

The README guides featured in these folders are set up using the below recommended software & extensions.

Docker desktop
Install docker desktop: "https://www.docker.com/products/docker-desktop/"

Install WSL2
Guide: "https://learn.microsoft.com/en-us/windows/wsl/install"

Install Git
https://gitforwindows.org/

VS code extensions
Remote - SSH
WSL
Dev Containers
Docker

Helpful video guides for set up
Create a Python Dev Environment with Docker and VS Code | NetDevOps and PyATS part 1:

https://www.youtube.com/watch?v=k8H0KCtsTR8&t=218s

Docker VSCode Python Tutorial // Run your App in a Container :

https://www.youtube.com/watch?v=jtBVppyfDbE

# Docker Development Tool

Below are instructions for setting up and using Docker as a geospatial development area.

## Set up

1. Build docker file

```(bash)
docker-compose build
```

2. Run a detached container to connect ot in vscode

```(bash)
docker-compose up -d
```

3. Check the container is running

```(bash)
docker ps
```

4. From here click the blue icon in the bottom left of VS code. Select "Attach to running container" 

## Close Down

5. To stop and remove the container enter

```(bash)
docker compose down
```