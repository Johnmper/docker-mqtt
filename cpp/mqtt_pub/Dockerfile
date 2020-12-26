FROM debian:buster-slim
LABEL maintainer="GOMES PEREIRA João Miguel"

# Basic configuration
RUN apt update
RUN apt install -y build-essential cmake pkg-config wget unzip git

# MQQT mosquitto
RUN apt install -y mosquitto-clients

# Networking
RUN apt install -y libssl-dev

# PAHO C++ install
WORKDIR /home

CMD [ "./home/pub4ever.sh" ]
