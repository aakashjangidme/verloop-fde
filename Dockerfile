#pull base image
FROM python:3.8-alpine

# set work directory
WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
ADD requirements.txt /app
RUN pip3 install -r requirements.txt

ADD . /app

CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]