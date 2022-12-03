from django.db import models


# Create your models here.
class Feature(models.Model):
    name = models.CharField(max_length=150, blank=True, default='')
    details = models.CharField(max_length=200, blank=True, default='')
    
