# ElasticSearch Docker 

Use this project to deploy the core components via Docker containers:

* ElasticSearch
* Kibana
* FSCrawler
* Portainer (for container management)
* document web server
* Apache Zeppelin

FSCrawler REST is enabled, but the standard file system crawler functionality is expected to be used in this version, for smaller corpus sets. If higher volumes are required, look at passing a df to Elastic instead.

## Pre-requisites

### Docker

* [Docker](https://docs.docker.com/engine/install/)
* [Docker Compose](https://docs.docker.com/compose/install/)

Check that Docker runs correctly:

`docker run hello-world`

### Environment variables

Create a `.env` configuration file in the same directory as `docker-compose.yml`, with required values, eg:

```
ELASTIC_VERSION=7.12.0
ELASTIC_PASSWORD=changeme    
FSCRAWLER_FOLDER=./test/data
JAVA_OPTS=-Xmx256m -Xms256m
```

This system has been tested against Elastic/Kibana version `7.12.0`. Set the password to a unique value (you can change it at any time), and set the target folder as required



## Starting and stopping

Start the cluster with

`docker-compose up -d`

Test locally with:

`curl http://localhost:9200`  (it may take a few minutes to come up)



The services will be available on the following ports/urls. You will need to update the domain if accessing remotely, and supply the `elastic` username, plus whatever password is set in `.env`

* Elastic: http://localhost:9200/
* raw docs: http://localhost:9200/idx/_search
* Kibana: http://localhost:5601/
* FSCrawler REST http://localhost:8080/fscrawler
* doc web server http://localhost:8100
* Apache Zeppelin http://localhost:8900


Stop the cluster with:

`docker-compose down`

This will close all the services, but retain all the data,users and other custom settings, saved as [volumes](https://docs.docker.com/storage/volumes/). If you wish to reset, then add the `-v` parameter, to remove the local volumes:

`docker-compose down -v`

Note, this will not impact any changes made to the configuration files in `/config`


## Container management

[Portainer](https://www.portainer.io/) has been included to simplify container management, specifically for:

* logs
* console access

Other features are available

http://localhost:9500 - swap `localhost` for your domain

## User management

Use Portainer to log into the Elastic container

Add and remove users, through the [file-based user authentication](https://www.elastic.co/guide/en/elasticsearch/reference/current/users-command.html), with the appropriate roles:

`bin/elasticsearch-users useradd newuser  -r superuser`

You will be asked for the password interactively. These users will then be able to log in via Kibana. 

There are a number of built-in roles (eg `superuser`), or new ones can be added to manage access to indexes


## Configuration

A number of base configuration files are packaged under the `config` directory, and mapped into the cluster as [bind mounts](https://docs.docker.com/storage/bind-mounts/)

Elastic and Kibana should not need any further configuration

All hosts have been defined as `0.0.0.0` to expose them externally

### FSCrawler

A single template configuration file is supplied - `config/fscrawler/idx/_template.yaml`. This has a placeholder for the Elastic password, which is pulled from the environment file `.env` at creation time, and written to the required `_settings.yaml` file.

A single index `idx` has been created, to regularly scan the folder defined in `FSCRAWLER_FOLDER`. To change the index name, or add new ones, matching configuration files and extra FSCrawler instances will need to be defined in `docker-compose.yml`


## Document webserver

A http server has been added, mapped to the source folder `FSCRAWLER_FOLDER` and exposed on port 8100. This allows browser access to the original document, by adding a [scripted field](https://www.elastic.co/guide/en/kibana/current/scripted-fields.html) to the [index pattern](https://www.elastic.co/guide/en/kibana/current/index-patterns.html)

`return "http://glwubu101.global.arup.com:8100" +  doc['path.virtual'].value`

Please note that this is the most basic  web server, a Python simple http command, so has no inbuilt security. Consider IP address filtering or a more advanced web server supporting authentication if required


## Troubleshooting

### Heap Space

`java.lang.OutOfMemoryError: Java heap space`

Update the `JAVA_OPTS` setting in `.env`

eg

JAVA_OPTS=-Xmx2g -Xms2g