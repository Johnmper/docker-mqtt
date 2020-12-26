import time
import paho.mqtt.client as mqtt
print("Starting SUB")

def on_connect(client, userdata, flags, rc):
    print("Connection returned result: " + mqtt.connack_string(rc))
    mqtt_sub.subscribe("/test/simple")
def on_disconnect(client, userdata, rc):
    if rc != 0:
        print("Unexpected disconnection.")

def on_subscribe(client, userdata, mid, granted_qos):
    print("Subscription complete")

def on_unsubscribe(client, userdata, mid):
    print("Unscription")
def on_message(client, userdata, message):
    print("Msg Recv = ", str(message.payload.decode("utf-8")))
    print("   topic = ", message.topic)
    print("     qos = ", message.qos)
    print("    flag = ", message.retain)

mqtt_sub = mqtt.Client("mqtt_sub", clean_session=True)
mqtt_sub.on_connect = on_connect
mqtt_sub.on_disconnect = on_disconnect
mqtt_sub.on_message = on_message
mqtt_sub.on_subscribe = on_subscribe
mqtt_sub.on_unsubscribe = on_unsubscribe

while True:
    try:
        mqtt_sub.connect("broker", port=1883)
        print("Connection Sucessful!!")
        break
    except ConnectionRefusedError:
        print("Failed to connect to broker")
        time.sleep(2)

print("Loop Start")
mqtt_sub.loop_start()
time.sleep(1000)