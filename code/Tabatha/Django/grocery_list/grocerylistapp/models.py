from django.db import models
from django.utils import timezone

# Create your models here.

class GroceryItem(models.Model):
    item = models.CharField(max_length=50)
    date_created = models.DateTimeField(timezone.now())
    date_completed = models.DateTimeField(null=True, blank=True)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.item