FROM ubuntu:14.04
FROM python:2.7
# Create image based on the official Node 6 image from dockerhub
FROM node:6
RUN apt-get update && \
      apt-get -y install sudo
# Create a directory where our app will be placed
ADD . /code
WORKDIR /code
RUN sudo apt-get install -y python3-setuptools
RUN sudo easy_install3 pip
#RUN sudo easy_install pip
RUN pip install -r requirements.txt

RUN mkdir -p /code/client/app
# Change directory so that our commands run inside this new directory
WORKDIR /code/client
# Copy dependency definitions
COPY package.json /code/client/app
# Install dependecies
RUN npm install
# Get all the code needed to run the app
COPY . /code/client/app
# Expose the port the app runs in
EXPOSE 4200
# Serve the app
CMD python ./code/server/app.py
CMD ["npm", "start"]