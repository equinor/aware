FROM python:3.6-alpine3.7
WORKDIR /src
RUN pip install pipenv
COPY Pipfile Pipfile.lock ./
RUN pipenv install --system --deploy
COPY ./src /src
CMD python3 /src/app.py
