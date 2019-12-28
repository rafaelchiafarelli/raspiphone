from django.urls import include,path

from . import views

urlpatterns = [

    #url(r'^api-token-auth/', views.obtain_auth_token)
    path('dialphone/dial/', views.dial,name='dialphone-dial'),

    
]