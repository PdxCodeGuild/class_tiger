from django.db import models
from django.urls import reverse

class Chirp(models.Model):
    text = models.CharField(max_length=150)
    creator = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

    def get_absolute_url(self):
        return reverse('chirp:detail', args=[str(self.id)])