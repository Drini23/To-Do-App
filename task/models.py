from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=255)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)    
    
    def __str__(self):
        return self.title

class TaskImages(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='task/images')
    
