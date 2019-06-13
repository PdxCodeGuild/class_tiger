from django.db import models

class ShortUrl(models.Model):
    long_url = models.CharField(max_length=500)
    short_url = models.CharField(max_length=10, default="")
  

    def __str__(self):
        return self.big_url
