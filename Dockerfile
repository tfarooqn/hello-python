# set base image (host OS)
FROM python:3.7

ARG MS_PORT

RUN mkdir /app
WORKDIR /app
ADD . /app/

RUN pip install -r requirements.txt

EXPOSE 7000

# command to run on container start
CMD [ "python", "./src/server.py" ]