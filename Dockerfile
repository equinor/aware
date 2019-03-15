FROM python:3
WORKDIR /src
RUN pip install pipenv
COPY Pipfile Pipfile.lock ./
RUN pipenv install --system --deploy
COPY ./src /src
CMD python3 /src/app.py
