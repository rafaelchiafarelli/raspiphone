from datetime import datetime
import urllib.request
import json    

import config


class Sender():
    def send_simple(self, topic, payload):
        print("send_simple")
        myurl = "http://192.168.0.103/"+topic
        req = urllib.request.Request(myurl)
        req.add_header('Content-Type', 'application/json; charset=utf-8')
        jsondata = json.dumps({'payload':payload})
        jsondataasbytes = jsondata.encode('utf-8')
        
        print(req.get_full_url())
        try:
            response = urllib.request.urlopen(req, jsondataasbytes)
            print(response.code)
            print("message sent to server")
            
            if response.code in [204, 200, 300]:
                print('Uhuuuu')
            else:
                print('never mind...')
            return True
        except Exception as e:
            response = str(e)
            print("error: " + response)
            return False
        
    
    def send_status(self, status):
        print('send_status')
        myurl = "http://192.168.0.103:8000/mediacenter/media/status"
        req = urllib.request.Request(myurl)
        req.add_header('Content-Type', 'application/json; charset=utf-8')
        jsondata = json.dumps(status)
        jsondataasbytes = jsondata.encode('utf-8')
        try:
            response = urllib.request.urlopen(req, jsondataasbytes)
            print("message sent to server")
            if response.code in [204, 200, 300]:
                print('Uhuuuu')
            else:
                print('never mind...')
            return True
        except Exception as e:
            response = str(e)
            print("error: " + response)
            return False
        
        
        
        
        
        
        
        
        
        
        
        
        