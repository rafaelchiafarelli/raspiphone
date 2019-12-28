from django.urls import include,path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)


urlpatterns = [
    
    #url(r'^api-token-auth/', views.obtain_auth_token)
    
    path('list/media', views.list_files,name='reload-files'),
    path('list', views.list_media,name='mediacenter-list'),
    path('list/music', views.list_media,name='mediacenter-music'),
    path('list/videos', views.list_media,name='mediacenter-videos'),
    path('list/channels', views.list_media,name='mediacenter-channels'),
    path('list/radios', views.list_media,name='mediacenter-radios'),

    path('play', views.play_media,name='play-media'),
    path('play/<int:pk>', views.play_media_by_id,name='play-media-by-id'),
    path('status', views.read_status, name='read-status'),
    path('mediacenter/exit', views.media_finished,name='mediacenter-finished'),
    
    path('mediacenter/media/status', views.media_status, name='set-media-status'),
]


