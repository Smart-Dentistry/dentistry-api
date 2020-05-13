# Dentistry API

This is an API implemented using [Django][] and [Django Rest Framework][] which goal
is to help dentists manage their clinics.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

It is assumed you have installed [Git][] and [Docker][] in your machine.

### Cloning repository

Clone this repo and navigate inside its root directory:

```bash
git clone https://github.com/Smart-Dentistry/dentistry-api.git && cd dentistry-api
```

### Building containers

Build containers:

```bash
docker-compose build
```

### Starting containers

Start containers:

```bash
docker-compose up
```

You are all set 🎉. Navigate to http://localhost:8000/ to see Django's success page.

## pre-commit and pre-push

[pre-commit][] is used in order to run some hooks and automate some tasks such as formatting files before committing and running tests before commiting and pushing. Make sure you have [installed pre-commit][install-precommit].

In order to take advantage of the hooks defined at [`.pre-commit-config.yaml`][pre-commit-file], run the following command:

```bash
pre-commit install && pre-commit install -t pre-push
```

## Docker commands

This is a compilation of some useful Docker commands.

### Containers commands

#### Build containers

```bash
docker-compose build
```

#### Start containers

```bash
docker-compose up
```

#### Stop containers

```bash
docker-compose stop
```

#### Remove containers

```bash
docker-compose rm
```

#### Destroy containers and volumes

```bash
docker-compose down -v
```

### Images commands

#### List images

```bash
docker image ls
```

#### Remove image

```bash
docker image rm <image_name>
```

### app service

#### Start bash session in python container

```bash
docker-compose exec app bash
```

#### Start Django shell

```bash
docker-compose exec app python manage.py shell
```

#### Run tests

```bash
docker-compose exec app pytest
```

### db service

#### Start bash session in postgres container

```bash
docker-compose exec db bash
```

[Django]: https://www.djangoproject.com/
[Django Rest Framework]: https://www.django-rest-framework.org/
[Docker]: https://docs.docker.com/get-docker/
[Git]: https://git-scm.com/downloads
[install-precommit]: https://pre-commit.com/#install
[pre-commit]: https://pre-commit.com
[pre-commit-file]: .pre-commit-config.yaml
