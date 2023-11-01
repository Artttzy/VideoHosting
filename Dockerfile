FROM python:3.11 as RUNNER
WORKDIR /app

COPY ./backend /app
COPY ./requirements.txt /app/requirements.txt
COPY ./.env /app/.env

RUN python -m pip install -r requirements.txt

EXPOSE 8080