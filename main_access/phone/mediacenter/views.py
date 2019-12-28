from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.http import JsonResponse
from django.contrib.auth.models import User, Group
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone




from rest_framework import generics
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.decorators import api_view, schema
from rest_framework.authtoken.models import Token
from rest_framework import viewsets

from .serializers import UserSerializer, GroupSerializer

from .models import status_model
from .models import MediaPlay

from .ParseFiles import Parser
from .SendPlayer import *
import csv
import json
import os
import os.path
from datetime import timedelta



def list_files(request):
    P = Parser()
    P.parseFiles()
    return redirect('mediacenter-list')
# Create your views here.
def list_media(request):
    all_media = MediaPlay.objects.all()

    context = {
        'media_list':all_media,
        'allmedia_amount':all_media.count(),
        'video_amount':all_media.filter(media_type = 1).count(),
        'music_amount':all_media.filter(media_type = 2).count()
        }
    return render(request,'mediacenter/list_media.html',context)


def play_media(request):
    print('play_media ' + request.method)
    print(request.GET)
    if request.is_ajax():
        media = MediaPlay.objects.filter(id = request.GET['id']).get()
        if media is not None:
            if os.path.isfile(media.fileName):
                
                send_to_player(media.fileName)
                status = "{'FileName': " + media.fileName +",'Previous': None,'next': None,'is_playing': True,'duration': 0,'duration_us': 0,'height': 0,'AspectRatio': 0.0,'Position': 0.0}"
                st = status_model(status = json.dumps(status))
                st.save()
                return JsonResponse({'success':True})
            else:
                media.delete()
                
    return JsonResponse({'success':False})
            

def play_media_by_id(request, pk):
    media = MediaPlay.objects.filter(id = pk).get()
    send_to_player(media.fileName)
    print("should play a song know")
    return redirect('mediacenter-list')

@csrf_exempt
def media_finished(request):
    print("media finished")
    
    return HttpResponse(status=200)

@csrf_exempt
def media_status(request):
    print("media status arrived - sent from the mediacenter controller")
    autodelete = status_model.objects.all()
    autodelete.delete()
    status = json.loads(request.body.decode('utf-8'))
    
    if status["FileName"] == "/home/pi/mediacenter/media/silence.mp3":
        status["is_playing"] = False
    else:
        status["is_playing"] = True
        
    status['ProgressBKD'] = (status['duration']-status['Position'])/status['duration']
    status['ProgressFWD'] = 1 - (status['duration']-status['Position'])/status['duration']
    status['Progress'] = 100 - 100*((status['duration']-status['Position'])/status['duration'])

    st = status_model(status = json.dumps(status))
    st.save()
    return HttpResponse(status=204)

def read_status(request):
    if request.is_ajax():
        st = status_model.objects.first()
        
        print("STATUS WHEN PASSING IT TO THE BROWSER")
        
        print(st.status)
        return JsonResponse({"status":st.status})
    return JsonResponse({'success':False})
            

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    
