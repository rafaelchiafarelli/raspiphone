import paho.mqtt.client as mqtt
from mediaplayer import mediaplayer
from pathlib import Path
from time import sleep
# This is the Subscriber

def on_connect(client, userdata, flags, rc):
  print("Connected with result code "+str(rc))
  client.subscribe("phone/mediacenter/file_changed")


def on_message(client, userdata, msg):
    print(msg.topic)
    if msg.payload.decode() == "Hello world!":
        print("Yes!")
    
    
    
def on_disconnect():
    print("fuck!")
    
client = mqtt.Client()
client.connect("192.168.0.107",1883,60)

client.on_connect = on_connect
client.on_message = on_message
client.on_disconnect = on_disconnect



count = 0
try:
    while True:
        print("main")
        client.loop(1)
        count+1
        if count == 20:
            client.publish('')


except KeyboardInterrupt:
    print('will stop the main')
