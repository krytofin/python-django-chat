from uuid import uuid4
from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models


class User(AbstractBaseUser):
    uuid = models.UUIDField(primary_key=True, default=uuid4, unique=True)
    username = models.CharField(max_length=70, unique=True)
    email = models.EmailField()
    friends = models.ManyToManyField("self", blank=True, symmetrical=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    
    is_admin = models.BooleanField(default=False)
    is_verificated = models.UUIDField(default=uuid, unique=True)
    
    def __str__(self):
        return f'{self.username} {self.email} {self.first_name} {self.last_name}'
