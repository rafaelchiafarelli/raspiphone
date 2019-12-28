import paho.mqtt.client as mqtt
from dialer import dialer
from pathlib import Path
from time import sleep

class MediaCenter():
    
    def __init__(self):
        # This are the global variables    
        self.functions_dict = {"phone/phonecenter/dial":self.dial,    
                              "phone/phonecenter/answer":self.rang,
                              "phone/phonecenter/read_sms":self.read_sms,
                              "phone/phonecenter/send_sms":self.send_sms,
                              "phone/phonecenter/connect_net":self.connect_net,
                              "phone/phonecenter/disconnect":self.disconnect}
        
        self.client = mqtt.Client()
        self.client.connect("localhost",1883,60)
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.client.on_disconnect = self.on_disconnect
                
        self.count = 0
    
    def on_connect(self, client, userdata, flags, rc):
      print("Connected with result code "+str(rc))
      
      for topic in self.functions_dict:
          print(topic)
          print("connect to topic: ",topic)
          self.client.subscribe(topic)
    
    def on_message(self, client, userdata, msg):
        print("hey, here is a message to you!!!!!")
        print(msg.topic)
        print(msg.payload.decode())
        if msg.topic in self.functions_dict:
            self.functions_dict[msg.topic](msg.payload.decode())
            
        if msg.payload.decode() == "Hello world!":
            ANOTHER_PATH = Path("./media/pno-cs.mp3")
            #sender_box(topic = msg.topic, payload = msg.payload )
            player.load(ANOTHER_PATH)
            print("Yes!")
    
    def on_disconnect(self):
        print("fuck!")
    
    #functions
    def dial(self, arg):
        print("Dial")
    
    def rang(self,arg):
        print("Rang")
                
    def read_sms(self,arg):
        print("read_sms")
    
    def send_sms(self,arg):
        print("send_sms")
    
    def connect_net(self,arg):
        print('connect to the net')
            
    def disconnect(self,arg):
        print('disconnect from the web')
            
    def run(self):
        try:
            while True:
                #print("main: ",self.count)
                self.client.loop(1)
                self.count+=1
        except KeyboardInterrupt:
            print('will stop the main')
            self.app.join()

def main():
  app = MediaCenter()
  app.run()
  
if __name__== "__main__":
  main()

