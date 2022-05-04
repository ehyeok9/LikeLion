from turtle import update
from django.db import models
from django.test import tag
from matplotlib.pyplot import title

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title