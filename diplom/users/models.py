from django.db import models
from django.contrib.auth.models import User



class UsersSite(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True)
    name = models.CharField(max_length=200, blank=True)
    email = models.EmailField(max_length=200, blank=True)
    username = models.CharField(max_length=200, blank=True)
    avatar = models.ImageField(default='users/default.png', upload_to='users/')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username

