from uuid import uuid4
from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.
class Group(models.Model):
    uuid = models.UUIDField(default=uuid4, unique=True)
    users = models.ManyToManyField(get_user_model())
    messages = models.ManyToManyField('Message', blank=True)
    events = models.ManyToManyField('Event', blank=True)
    time_created = models.DateTimeField(auto_now_add=True)
    
    
    
class Message(models.Model):
    text = models.TextField()
    sent_time = models.DateTimeField(auto_now_add=True)
    
class Event(models.Model):
    type = models.TextField()
    time = models.DateTimeField(auto_now_add=True)