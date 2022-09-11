FROM python:3.8-slim as x-lab-test-task-base

ENV LANG C.UTF-8
ENV PYTHONPATH=/opt

RUN apt-get update && apt-get install -y build-essential
RUN python -m pip install --upgrade pip


FROM x-lab-test-task-base as x-lab-test-task-image
WORKDIR /opt
COPY requirements.txt /opt/requirements.txt
RUN python -m pip install -r requirements.txt