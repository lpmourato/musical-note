#!/bin/bash
docker build -t musical-note-image:dev .
docker rm musical
docker run -t --name=musical -v `pwd`:/code -p 4200:4200 -p 5000:5000 -w /code -i -t musical-note:dev bash
#docker run -v `pwd`:/code -p 4200:4200 -p 5000:5000 -w /code -i -t musical-note:dev bash