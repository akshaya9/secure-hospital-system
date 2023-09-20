# pull official base image
# FROM continuumio/miniconda3:4.10.3p0-alpine
FROM python:3.9
# set work directory
WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DEBUG 0


# install psycopg2
RUN apt update \
    && apt install --virtual build-essential gcc python3-dev musl-dev
    # && apk add postgresql-dev 
    # && pip install psycopg2

# install dependencies
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# RUN wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
# RUN bash Miniconda3-latest-Linux-x86_64.sh -b -p /miniconda
# ENV PATH=$PATH:/miniconda/condabin:/miniconda/bin

# RUN conda install -c kumatea tensorflow

# copy project
COPY . .

RUN python manage.py collectstatic --noinput

# add and run as non-root user
RUN adduser -D myuser
USER myuser

# run gunicorn
CMD gunicorn shs.wsgi:application --bind 0.0.0.0:$PORT