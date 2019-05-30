from django.db import models


class GroceryItem(models.Model):
    grocery_text = models.CharField(max_length=40)
    create_date = models.DateTimeField()
    complete_date = models.DateTimeField(null=True, blank=True)
    completed = models.BooleanField(default=False)
