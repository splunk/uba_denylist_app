FROM python:3.7-alpine

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE 1
# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED 1

# Install dev dependencies
RUN apk update \
    && apk add curl postgresql-dev gcc python3-dev musl-dev openssl-dev libffi-dev

# Install poetry
RUN pip install -U pip \
    && curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
ENV PATH="${PATH}:/root/.poetry/bin"

WORKDIR /usr/src/app
COPY iocbin ./iocbin
COPY pyproject.toml poetry.lock ./

RUN poetry config virtualenvs.create false
RUN poetry install --no-dev --no-interaction --no-ansi

ENTRYPOINT [ "poetry", "run", "iocbin"]
EXPOSE 5000