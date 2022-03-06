FROM python:3.10

WORKDIR /app
ENV PYTHONPYCACHEPREFIX=/tmp/pycache
ENV FLASK_APP=app

COPY ./code/requirements.txt ./

RUN apt-get update
RUN apt-get install -y sqlite3

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
