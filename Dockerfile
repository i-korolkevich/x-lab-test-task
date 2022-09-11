FROM python:3.8-slim as x-lab-test-task-image

ENV LANG C.UTF-8
ENV PYTHONPATH=/opt

RUN apt update && apt install -y build-essential && apt clean && rm -rf /var/lib/apt/lists/*
RUN python -m pip install --upgrade pip
WORKDIR /opt
COPY requirements.txt /opt/requirements.txt
RUN python -m pip install --no-cache-dir -r requirements.txt