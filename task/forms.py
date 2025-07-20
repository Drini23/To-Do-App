from django import forms 
from django.forms import ModelForm
from .models import *

class TaskForm(forms.ModelForm):
    
    class Meta:
        model = Task
        fields = ['title',  'complete', 'image']


class ImageTaskForm(forms.ModelForm):
    
    class Meta:
        model = TaskImages
        fields = [ 'image']