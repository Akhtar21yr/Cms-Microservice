FROM python:3.11-slim

# Install system dependencies for mysqlclient
RUN apt-get update && \
    apt-get install -y default-libmysqlclient-dev build-essential && \
    apt-get clean

ENV PYTHONBUFFERED 1

WORKDIR /app
COPY pkg.txt /app/pkg.txt
RUN pip install --no-cache-dir -r pkg.txt
COPY . /app

