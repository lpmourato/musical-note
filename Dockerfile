FROM ubuntu:14.04

RUN apt-get update && \
      apt-get -y install curl  software-properties-common wget build-essential checkinstall libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev

# Installing python 2.7
RUN apt-add-repository ppa:fkrull/deadsnakes-python2.7
RUN apt-get update
RUN apt-get install -y --force-yes python2.7 python-setuptools python2.7-dev
RUN easy_install pip
# Install python project dependencies
RUN pip install flask
RUN pip install flask_cors
RUN pip install redis
#RUN pip install -r requirements.txt

# Installing node 
RUN curl -sL https://deb.nodesource.com/setup_6.x | sudo -E bash 
RUN apt-get install nodejs

VOLUME /code

WORKDIR /code/client
RUN npm install
WORKDIR /code/server

EXPOSE 4200
EXPOSE 5000

#CMD python app.py
#CMD ["npm", "start"]