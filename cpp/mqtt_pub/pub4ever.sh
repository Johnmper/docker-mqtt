#!/bin/bash
for (( i = 1 ; i <= 60 ; i++ )); do
    sleep 1
    mosquitto_pub -t "test/topic" -m "Message $i" -h mqtt_cpp_broker -p 1883
    echo "Sent \"Message $i\""
done