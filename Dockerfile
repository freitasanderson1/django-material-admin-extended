FROM python:3.12

LABEL mantainer="freitas.dev@proton.me"

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt

RUN pip install -r requirements.txt

RUN mkdir /app
RUN mkdir /app/materialdash

WORKDIR /app
COPY ./app /app
COPY ./materialdash /app/materialdash
COPY ./docker /app/docker
COPY ./tests /app/test

RUN chmod +x /app/docker/start.sh

CMD ["/app/docker/start.sh"]