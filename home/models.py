from django.db import models
from datetime import datetime
from django.conf import settings
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255,null=False,blank=False)
    def __str__(self):
        return f"{self.name}"

class Slot(models.Model):
    name = models.CharField(max_length=255,null=False,blank=False)
    size =  models.TextField(null=True,blank=True)
    link = models.TextField()
    date = models.DateField(null=True,blank=True,default=datetime.utcnow  )
    author = models.ForeignKey( settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    category = models.ForeignKey( Category, on_delete=models.CASCADE, null=True, blank=True)
    price = models.TextField(null=True,blank=True)

    def __str__(self):
        return f"{self.name}"