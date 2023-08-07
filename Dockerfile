FROM python:3.7.6
MAINTAINER GEUMSEONG YANG <didrmatjd@gmail.com>

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Working Directory
WORKDIR /app
COPY . /app/

# Dependency
RUN pip install --upgrade pip
RUN pip install -r requirements.txt