import paho.mqtt.client as mqtt
from mediaplayer import mediaplayer
from pathlib import Path
from time import sleep
from sender import Sender

class MediaCenter():
    
    def __init__(self):
        # This are the global variables    
        self.functions_dict = {"phone/mediacenter/play":self.play,    
                      "phone/mediacenter/stop":self.stop,
                      "phone/mediacenter/increase_volume":self.increase_volume,
                      "phone/mediacenter/decrease_volume":self.decrease_volume,
                      "phone/mediacenter/pause":self.pause,
                      "phone/mediacenter/loadfile":self.load_file,
                      "phone/mediacenter/position/get":self.get_position
                      }

        self.sender = Sender()
        
        self.client = mqtt.Client()
        self.client.connect("localhost",1883,60)
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.client.on_disconnect = self.on_disconnect
                
        self.player = mediaplayer(1,'MainThread')
        
        self.player.exitEvent = self.exit_event
        self.player.pauseEvent = self.pause_event 
        self.player.playEvent = self.play_event
        self.player.positionEvent = self.position_event
        self.player.seekEvent = self.relative_event
        self.player.stopEvent = self.stop_event  
        self.player.start()
        self.status = dict()
        self.count = 0

    #events
    
    def exit_event(self, player, exit_status):
        print("exit_event")
        self.sender.send_simple(topic='mediacenter/exit',payload = exit_status.__str__())
    
    def pause_event(self, player):
        print("pause")
        self.sender.send_simple(topic='mediacenter/pause',payload = 'paused')
       
    def play_event(self, player):
        print("play")
        self.sender.send_simple(topic='mediacenter/play',payload = 'played')
    
    def position_event(self, player, absolute_position):
        print("position event")
        self.sender.send_simple(topic='mediacenter/position',payload = absolute_position.__str__())
        
    def relative_event(self, player, relative_position):
        print("relative")
        self.sender.send_simple(topic='mediacenter/relative',payload = relative_position.__str__())
    
    def stop_event(self, player):
        print("stop_event")
        self.sender.send_simple(topic='mediacenter/stop',payload = 'stoped')
    
    
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

    def on_disconnect(self):
        print("fuck!")
    
    #functions
    def play(self, arg):
        print("PLAY")
        self.player.play()
    
    def pause(self,arg):
        print("PLAY")
        self.player.pause()
                
    def load_file(self,arg):
        print("LOAD")
        self.player.load(arg)
    
    def stop(self,arg):
        print("STOP!")
        self.player.stop()
    
    def increase_volume(self,arg):
        print('INCREASE THE VOLUME!!!!')
        cur = self.player.volume()
        if cur<1:
            self.player.set_volume(cur+0.1)
            
    def decrease_volume(self,arg):
        print('DECREASE THE VOLUME!!!!')
        cur = self.player.volume()
        if cur>=0.1:
            self.player.set_volume(cur-0.1)

    def get_position(self, arg):
        print("GET POSITION")
        current_position = self.player.position() 
        print("current position is: ", current_position)
    
    def get_status(self):
        self.status = self.player.get_status()
        return self.status
    
    def send_status(self):
        self.status = self.player.get_status_mediaplayer()
        self.sender.send_status(status = self.status)
        
    def run(self):
        try:
            while True:
                #print("main: ",self.count)
                self.client.loop(1)
                self.send_status()
                self.count+=1
                if self.count > 65530:
                    self.count = 0
        except KeyboardInterrupt:
            print('will stop the main')
            self.player.join()

def main():
  app = MediaCenter()
  app.run()
  
if __name__== "__main__":
  main()

