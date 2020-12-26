import time
import paho.mqtt.client as mqtt
print("Starting PUB")


def on_connect(client, userdata, flags, rc):
    print("Connection returned result: " + mqtt.connack_string(rc))

def on_disconnect(client, userdata, rc):
    if rc != 0:
        print("Unexpected disconnection.")
        

mqtt_pub = mqtt.Client("mqtt_pub", clean_session=True)
mqtt_pub.on_connect = on_connect
mqtt_pub.on_disconnect = on_disconnect

while True:
    try:
        mqtt_pub.connect("broker", port=1883)
        print("Connection Sucessful!!")
        break
    except ConnectionRefusedError:
        print("Failed to connect to broker")
        time.sleep(1)

delay = 0.005
msg_count = 0
topic = "/test/simple"
while True:
    time.sleep(delay)
    msg = "messages: %d > %f" % (msg_count, delay)
    print("Trying to send message %s" % (msg))
    result = mqtt_pub.publish(topic, msg)
    if not (result[0] == 0):
        print("Message sent failed!")
    msg_count += 1