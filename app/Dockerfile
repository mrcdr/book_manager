FROM python:3.10

RUN apt-get update && apt-get install -y sqlite3

RUN mkdir -p /app
RUN mkdir -p /app_data
RUN useradd -m -U app
RUN chown -R app:app /app_data /app
USER app
ENV PATH $PATH:/home/app/.local/bin

COPY ./code/requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install -r /app/requirements.txt --user
ENV PYTHONPYCACHEPREFIX=/tmp/pycache
ENV FLASK_APP=app

COPY ./code /app
WORKDIR /app