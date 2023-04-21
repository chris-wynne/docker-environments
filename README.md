# Docker Guides

Docker set up guides for containerised development. Each folder contains set up for a specific development environment or tool.

## Why use docker for containerised development?

1. **Consistent environment**: Docker containers help maintain a consistent environment across different stages of development, testing, and production. This can help reduce the "it works on my machine" issue, where code runs well on a developer's machine but fails on another system due to differences in configurations, dependencies, or system libraries.

2. **Isolation**: Docker containers isolate your application and its dependencies, which helps keep your host system clean and reduces the risk of conflicts between different projects or components.

3. **Reproducibility**: By defining your application and its dependencies using a Dockerfile, you can easily recreate the same environment for different team members, continuous integration (CI) pipelines, or even for deploying the application. This simplifies the onboarding process for new team members and makes it easier to manage dependencies.

4. **Portability**: Docker containers can run on any system with Docker installed, regardless of the underlying operating system. This makes it easy to share your development environment with others and deploy your application to different platforms.

5. **Scalability**: Docker makes it easier to manage and scale applications by using container orchestration tools like Kubernetes or Docker Swarm.

## Software requirements

1. Docker Desktop: https://www.docker.com/products/docker-desktop/ 
2. WSL2: https://learn.microsoft.com/en-us/windows/wsl/install
3. Git: https://gitforwindows.org/
4. VS Code extensions: Remote - SSH, WSL, Dev Containers, Docker

## Using Docker as a development environment

### Set up

1. Build docker file

```(bash)
docker-compose build
```

1. Run a detached container

```(bash)
docker-compose up -d
```

3. Check the container is running

```(bash)
docker ps
```
### Connect to the container

#### Option 1: VS Code

Click the blue icon in the bottom left of VS Code. Select "Attach to Running Container".

#### Option 2: Interactive bash session

```(bash)
docker-compose run --rm app bash
```

Replace bash with sh if your container uses sh instead.

### Close Down

To stop and remove the container, enter

```(bash)
docker compose down
```