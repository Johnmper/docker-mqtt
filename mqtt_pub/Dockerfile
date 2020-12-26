FROM python:3.8-slim-buster
LABEL maintainer="GOMES PEREIRA João Miguel"

RUN apt update

# Core dependencies. 
RUN apt install -y build-essential cmake  pkg-config apt-utils yasm software-properties-common
RUN apt install -y git wget unzip 

RUN pip3 install --upgrade pip && pip3 --no-cache-dir install numpy paho-mqtt
EXPOSE 1883 8883 8080 44053 4369 8888 \
       9100 9101 9102 9103 9104 9105 9106 9107 9108 9109
CMD ["python", "/home/pub.py"]