import datetime

from django.db import models
from django.utils import timezone
# Create your models here.
class GroceryItem(models.Model):
    item_title = models.CharField(max_length=200)
    item_quantity = models.DecimalField(max_digits=5, decimal_places=2)
    pub_date = models.DateTimeField('Date published')
    completed_date = models.DateField(null=True, blank=True)
    is_complete = models.BooleanField(default=False)

    def __str__(self):
        return self.item_title
