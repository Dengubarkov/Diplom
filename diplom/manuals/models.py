from django.db import models
from users.models import UsersSite

class Manuals(models.Model):
    owner = models.ForeignKey(UsersSite, on_delete=models.SET_NULL, blank=True, null=True)
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=500, blank=True)
    text = models.TextField(blank=True)
    directory_file = f"manuals/%Y/%m/%d/"
    logo = models.ImageField(blank=True, default="manuals/default.png", upload_to=directory_file)
    files = models.FileField(blank=True, upload_to=directory_file)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
# Create your models here.
