# Dentistry API

This is an API to help dentists manage their clinics.

## Technologies

The main technologies used in this project are:

* [Docker][]
* [PostgreSQL][] (container)
* [Python 3][python] (container)
* [poetry][]
* [Django][]
* [Django REST Framework][DRF]

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

### Seed database (recommended)

You can populate the database by running the following command:

```python
docker-compose exec app python manage.py seed
```

You are all set 🎉. Navigate to http://localhost:8000/admin/ to see Django's admin login page.

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

#### Seed database

```bash
docker-compose exec app seed
```

#### Clear database (keep migrations' table)

```bash
docker-compose exec app flush --no-input
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
[DRF]: https://www.django-rest-framework.org/
[Docker]: https://www.docker.com
[Git]: https://git-scm.com/downloads
[install-precommit]: https://pre-commit.com/#install
[poetry]: https://python-poetry.org
[PostgreSQL]: https://www.postgresql.org
[pre-commit]: https://pre-commit.com
[pre-commit-file]: .pre-commit-config.yaml
[python]: https://www.python.org
