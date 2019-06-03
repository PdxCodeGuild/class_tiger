from django.db import models

# Create your models here.

class Short(models.Model):
    big_url = models.CharField(max_length=500)
    short = models.CharField(max_length=10, default="")
    hits = models.IntegerField(default=0)

    def __str__(self):
        return self.big_url
