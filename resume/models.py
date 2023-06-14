from django.db import models

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    # images = models.ListField(models.ImageField(upload_to='images/', blank=True))
    time_create = models.DateTimeField(auto_now_add=True)
    is_relevant = models.BooleanField(default=True)
    difficulty = models.IntegerField(default=1)
    likes = models.IntegerField(default=1)
    # tags = models.ListField(models.TextField(max_length=30, blank=True))
    