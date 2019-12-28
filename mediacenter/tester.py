from omxplayer.player import OMXPlayer
from pathlib import Path
from time import sleep

VIDEO_PATH = Path("./media/silence.mp3")
ANOTHER_PATH = Path("./media/pno-cs.mp3")
def old_function():
    player = OMXPlayer( ANOTHER_PATH,args=['-o','alsa:hw:1,0'])
    sleep(1)
    playing = True
    count = 0
    while playing:
        try: 
            playing = player.is_playing()
        except:
            print('repeat')
            player.load( ANOTHER_PATH)
        sleep(1)
        print("let the players be players")    
        count+=1
        sleep(120)
        if count == 20:
            player.load(ANOTHER_PATH)
            sleep(2)
            player.quit()
    
            sleep(2)
            playing = False
    

#import paho.mqtt.client as mqtt #import the client1
#broker_address="192.168.0.107" 
#broker_address="iot.eclipse.org" #use external broker
#client = mqtt.Client("P1") #create new instance
#client.connect(broker_address) #connect to broker
#client.publish("phone/mediacenter/loadfile","/home/pi/main_access/media/pno-cs.mp3")#publish
#client.publish("phone/mediacenter/stop","stop")#publish
#client.publish("phone/mediacenter/play","play")#publish
#client.publish("phone/mediacenter/loadfile","./media/file_example_MP3_5MG.mp3")#publish
#client.publish("phone/mediacenter/play","")    
#client.publish("phone/mediacenter/stop","")
#client.publish("phone/mediacenter/increase_volume","")
#client.publish("phone/mediacenter/decrease_volume","")
#client.publish("phone/mediacenter/pause","")
old_function()