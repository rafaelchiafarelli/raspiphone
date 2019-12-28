
import paho.mqtt.client as mqtt #import the client1

def send_to_player(filename):
    broker_address="192.168.0.103" 
    #broker_address="iot.eclipse.org" #use external broker
    client = mqtt.Client("P1") #create new instance
    client.connect(broker_address) #connect to broker
    client.publish("phone/mediacenter/loadfile",filename)#publish


def get_media_position(filename):
    print("request media position")
    broker_address="192.168.0.103" 
    #broker_address="iot.eclipse.org" #use external broker
    client = mqtt.Client("P1") #create new instance
    client.connect(broker_address) #connect to broker,
    
    client.publish("phone/mediacenter/position/get",filename)#publish
    return 'None'