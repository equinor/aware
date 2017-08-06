FROM python:3

COPY ./src /app

RUN pip install -r /app/requirements.txt

CMD python3 /app/app.py
