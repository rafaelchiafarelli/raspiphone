from .models import MediaPlay
from django.conf import settings

import os
import subprocess
from os import listdir
from os.path import isfile, join



class Parser():
    
    def __init__(self):
        self.functions_dict ={".mp3":self.music,    
                          ".wav":self.music,
                          ".aac":self.music,
                          ".wma":self.music,
                          ".avi":self.video,
                          ".mkt":self.video,
                          ".mp4":self.video,
                          ".m4a":self.video,
                          ".m4v":self.video,
                          ".f4v":self.video,
                          ".f4a":self.video,
                          ".m4b":self.video,
                          ".m4r":self.video,
                          ".f4b":self.video,
                          ".mov":self.video,
                          ".3gp":self.video,
                          ".3gp2":self.video,
                          ".3g2":self.video,
                          ".3gpp":self.video,
                          ".3gpp2":self.video,
                          ".ogg":self.video,
                          ".oga":self.video,
                          ".ogv":self.video,
                          ".ogx":self.video,
                          ".wmv":self.video,
                          ".wma":self.video,
                          ".asf":self.video,
                          ".flac":self.video
                          }
        
    def parseFiles(self):
        for path, subdirs, files in os.walk(settings.MEDIA_ROOT):
            for name in files:
                if name[-4:] in self.functions_dict:
                    self.functions_dict[name[-4:]](os.path.join(path, name))
        print("search for usb devices in /media/pi")
        for path, subdirs, files in os.walk("/media/pi"):
            for name in files:
                if name[-4:] in self.functions_dict:
                    self.functions_dict[name[-4:]](os.path.join(path, name))        
                    
    def music(self,FileName):
        print("The Sound of Music")
        self.dataBase(FileName=FileName, Type=2)
            

    
    def video(self,FileName):
        print("it is a video")
        self.dataBase(FileName=FileName, Type=1)
        
    
    def dataBase(self,FileName,Type):
        is_there = MediaPlay.objects.filter(media_type = Type).filter(fileName = FileName).count()
        if is_there == 0:
            obj = MediaPlay(fileName = FileName,media_type = Type)
            obj.save()
        if is_there > 1:
            is_there.delete()
            obj = MediaPlay(fileName = FileName,media_type = Type)
            obj.save()
        
        
        
        
        
        
        
        
        