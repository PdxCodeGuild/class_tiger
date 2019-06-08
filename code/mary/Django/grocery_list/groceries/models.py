import datetime

from django.db import models
from django import forms
from django.utils import timezone

class GroceryItem(models.Model):
    item_text=models.CharField(max_length=100)
    created_date=models.DateTimeField('date created')
    completed_date=models.DateTimeField('date completed', null=True, blank=True)
    is_complete=models.BooleanField(default=False)

    def __str__(self):
        return self.item_text




