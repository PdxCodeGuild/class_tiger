from django.db import models
from django.urls import reverse
from datetime import timedelta
# Create your models here.
class Chirp(models.Model):
    title= models.CharField(max_length=30)
    author= models.ForeignKey('auth.User', on_delete=models.CASCADE)
    body = models.CharField(max_length=150)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url (self):
        return reverse('chirps:detail', args=[str(self.id)]
