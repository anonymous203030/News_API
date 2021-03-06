FROM python:3.8-slim

ENV PYTHONUNBUFFERED 1
MAINTAINER NewsAPI


RUN apt-get update -y \
&& apt-get upgrade -y \
&& apt-get install -y apt-utils \
&& apt-get install gcc -y \
&& apt-get clean \
&& apt-get install -y python-setuptools \
&& apt-get install -y libpq-dev python3-dev \
&& apt-get install -y systemd



COPY ./requirements.txt /requirements.txt

RUN pip3 install -r requirements.txt


RUN mkdir /NewsAPI
WORKDIR /NewsAPI
COPY . ./NewsAPI
