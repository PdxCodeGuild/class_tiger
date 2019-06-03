import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class URL(models.Model):
    long_URL= models.CharField(max_length=200,default='')
    short_URL=  models.CharField(max_length=200,default='')

    def __str__(self):
        return self.long_URL + ' - ' + self.short_URL


class UserData(models.Model):
    user_agent = models.CharField(max_length=200,default='')
    ip_addr = models.CharField(max_length=200,default='')
    url = models.ForeignKey(URL,on_delete=models.CASCADE)

    def __str__(self):
        return self.ip_addr