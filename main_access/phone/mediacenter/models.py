from django.db import models
from .MediaTypes import *
from django.utils import timezone

# Create your models here.
class MediaPlay(models.Model):
    fileName = models.CharField(max_length = 500)
    media_type = models.IntegerField(choices=TYPE_CHOICES,default=3)
    def __str__(self):
        return self.fileName.split('/')[-1:].__str__()
    

class status_model(models.Model):
    status = models.TextField()
    entered = models.DateTimeField(default=timezone.now)