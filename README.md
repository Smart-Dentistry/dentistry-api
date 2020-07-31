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

### Creating a gpg RSA key-pair

Install [git-secret][] and [create a gpg RSA key-pair][create-gpg-key].
Send your `public-key.gpg` file to a developer and ask him to
add you to this repository using git-secret.

### Cloning repository (depends on previous step)

Once you have confirmed that you have been included in the repo using git-secret, clone this repo and navigate inside its root directory:

```bash
git clone https://github.com/Smart-Dentistry/dentistry-api.git && cd dentistry-api
```

### Decrypting secrets

Decrypt the secret files by running the following command:

```python
git secret reveal
```

The previous command will decript two files `.env.app` and `.env.db` which contain environment variables with keys and secrets for configuration.

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

## Adding a new developer

If you are a new developer joining the project,
create a new branch called `new-dev-[username]` and
add yourself as a dict element (`username` and `email`) at the end of the `DEVS` list located at [seed.py][].
(see existing elements in `DEVS`)

Once you have added yourself, commit the changes, push the branch, and create a pull request.

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

[create-gpg-key]: https://git-secret.io/#using-gpg
[Django]: https://www.djangoproject.com/
[DRF]: https://www.django-rest-framework.org/
[Docker]: https://www.docker.com
[Git]: https://git-scm.com/downloads
[git-secret]: https://git-secret.io/
[install-precommit]: https://pre-commit.com/#install
[poetry]: https://python-poetry.org
[PostgreSQL]: https://www.postgresql.org
[pre-commit]: https://pre-commit.com
[pre-commit-file]: .pre-commit-config.yaml
[python]: https://www.python.org
[seed.py]: ./core/management/commands/seed.py
