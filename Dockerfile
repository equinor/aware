FROM python:3.7-alpine3.9
ENV PYTHONUNBUFFERED=1
WORKDIR /src
RUN apk update && pip install --upgrade pip && pip install pipenv
COPY Pipfile Pipfile.lock ./
RUN pipenv install --system --deploy && pipenv check
COPY ./src /src
CMD python3 /src/app.py
