from django.urls import include,path

from . import views

urlpatterns = [

    #url(r'^api-token-auth/', views.obtain_auth_token)
    path('sensors/land/', views.land,name='sensors-land'),

    
]