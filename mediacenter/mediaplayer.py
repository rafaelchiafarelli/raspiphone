from omxplayer.player import OMXPlayer
from pathlib import Path
from time import sleep
import os.path

import threading


class mediaplayer(threading.Thread, OMXPlayer):    
      
    def __init__(self, threadID, name):
        self.VIDEO_PATH = Path("/home/pi/mediacenter/media/silence.mp3") 
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.die = False
        if os.path.isfile(self.VIDEO_PATH):
            print("it IS a file")
            OMXPlayer.__init__(self, source = self.VIDEO_PATH, args=['-o','alsa:hw:1,0'])
        else:
            print("it is not a file")
        self.status = {'FileName': '/home/pi/mediacenter/media/silence.mp3',
                        'Previous': None,
                        'next': None,
                        'is_playing': False,
                        'duration': 0,
                        'duration_us': 0,
                        'height': 0,
                        'AspectRatio': 0.0,
                        'Position': 0.0
                        }

    def get_status_mediaplayer(self):
        return self.status

    def player_handler(self):
        
        
        try: 
            print("player_handler function")
            print("playing: ", self.get_source())
            print("time in: ", self.position())
            print("is_playng mediaplayer: ", self.is_playing())
            print('get_full_status')
            ret = {
                'FileName':self.get_source().__str__(),
                'Previous':self.previous(),
                'next': self.next(),
                'is_playing':self.is_playing(),
                'duration':self.duration(),
                'duration_us':self._duration_us(),
                'height':self.height(),
                'AspectRatio':self.aspect_ratio(),
                'Position': self.position()
                }
            self.status = ret
            
        except:
            print('repeat')
            self.load( self.VIDEO_PATH)
        print("let the players be players")  
    
    def run (self):
        while not self.die:
            sleep(2)
            self.player_handler()
            
        print("player is dead")

    def join(self):
        self.die = True
        print("will stop the player")
        self.quit()
        super().join() 

