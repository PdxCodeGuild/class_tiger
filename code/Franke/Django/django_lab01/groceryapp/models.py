import datetime

from django.db import models
from django.utils import timezone
from django.urls import reverse


# Create your models here.

class GroceryItem(models.Model):
    #creating fields/attribute for the table #a class will return just object to make it return data do __str__
    text_description = models.CharField(max_length=200)
    created_date = models.DateTimeField(auto_now_add= True)
    completed_date = models.DateTimeField(null=True, blank=True)
    completed = models.BooleanField(default=False)
    #a class will return just object to make it return data do __str__
    def __str__(self):
        return self.text_description
    #you can make some calculation on the 
    # def was_published_recently(self):
    #     now = timezone.now ()
    #     return now - datetime.timedelta(days=1) <= self.pub_date <= now
    def get_absolute_url(self):
        return reverse('groceryapp:index', args=[str(self.id)])