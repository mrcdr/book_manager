FROM python:3.10

WORKDIR /app
ENV PYTHONPYCACHEPREFIX=/tmp/pycache
ENV FLASK_APP=app

COPY ./code /app
WORKDIR /app

RUN apt-get update
RUN apt-get install -y sqlite3

RUN useradd -m -U app
RUN mkdir -p /app_data
RUN chown -R app:app /app_data /app

USER app
ENV PATH $PATH:/home/app/.local/bin
RUN pip install --upgrade pip
RUN pip install -r requirements.txt --user
