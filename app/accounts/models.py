from uuid import uuid4
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **kwargs):
        if not username:
            raise ValueError("User must have an username")
        if not email:
            raise ValueError("User must have an email")
        user:User = self.model(email=email, username=username, **kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, username, email, password=None, **kwargs):
        kwargs.setdefault('is_admin', True)
        kwargs.setdefault('is_active', True)
        user = self.create_user(username, email, password=password, **kwargs)
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    uuid = models.UUIDField(primary_key=True, default=uuid4, unique=True, editable=False)
    username = models.CharField(max_length=70, unique=True)
    email = models.EmailField()
    friends = models.ManyToManyField("self", blank=True, symmetrical=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    
    is_admin = models.BooleanField(default=False)
    verification_code = models.UUIDField(default=uuid4, unique=True)
    is_verificated = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    
    objects = UserManager()
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']
    
    def __str__(self):
        return f'{self.username} {self.email} {self.first_name} {self.last_name}'
    
    def has_perm(self, perm, obj=None):
        return True
    
    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin