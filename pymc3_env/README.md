# Workspace

This container environment uses pymc3 for bayesian regression. \
\
Building the image for the first time may take a while.

## Set up guide

This uses the docker files located within this directory to set up an environment. It mounts any files or folders located in this directory to the container within "app". \
To ignore files add them to the .dockerignore file.

1. To run the prebuilt compose file & generate an image type in bash: "docker-compose build". This may take a minute.
2. To generate a container called "pym3_conda_dev" type: "docker-compose up -d".
3. Check the container is running: "docker ps"
4. From here click the blue icon in the bottom left of VS code. Select "Attach to running container".
\

## Close down

To close down and remove containers & images enter the below commands into bash:

1. To stop container enter: "docker stop pym3_conda_dev". \
2. To remove container enter: "docker rm pym3_conda_dev". \
3. To stop & remove container enter: "docker compose down". \
4. To remove image enter: "docker rmi miniconda_env".
