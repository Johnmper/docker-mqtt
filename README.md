# docker-mqtt-python

Testing MQTT libraries for python using docker

## To build/run

```bash
docker-compose build
docker-compose run
# OR
docker-compose up --build
# OR Open 3 terminals and
docker-compose up mqtt_broker
docker-compose up mqtt_pub
docker-compose up mqtt_sub
```

## Debug Docker

```bash
docker-compose images
docker-compose top
docker-compose ps
```

## Debug broker

```bash
# Open bash inside broker
docker-compose exec mqtt_broker /bin/bash
$ cat /etc/hosts
$ vmq-admin session show
$ vmq-admin cluster show
$ vmq-admin metrics show
$ vernemq ping
$ vernemq console
```