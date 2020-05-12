FROM python:alpine

ENV PYTHONDONTWRITEBYTECODE 1 \
  PYTHONUNBUFFERED=1 \
  POETRY_VERSION=1.0.5

# Install psycopg2 and other dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev openssl-dev libffi-dev

# Install poetry
RUN pip install -U pip && pip install poetry

WORKDIR /usr/src/app
COPY . .
RUN poetry config virtualenvs.create false \
  && poetry install --no-interaction --no-ansi

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
# File wsgi.py was not found in subfolder:mvp_back. Please enter the Python path to wsgi file.
# CMD ["gunicorn", "--bind", "0.0.0.0:8000", "mvp.wsgi"]

# run entrypoint.sh
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
