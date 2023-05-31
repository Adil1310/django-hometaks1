from django.db import models
import datetime

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=20)
    body = models.TextField(null=False, blank=False)
    date = models.DateField(default=datetime.datetime.now())
    
    def __str__(self):
        return self.title + self.body    
    
    