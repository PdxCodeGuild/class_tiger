from django.db import models
from django.urls import reverse
from datetime import timedelta

class Post(models.Model):
    squawk=models.TextField(max_length=120)
    username=models.ForeignKey('auth.User', on_delete=models.CASCADE)
    posted=models.DateTimeField(auto_now_add=True)
    edited=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.squawk
    
    def get_absolute_url(self):
        return reverse('posts:detail', args=[str(self.id)])

    @property
    def time_diff(self):
        return (self.edited - self.posted)>timedelta(seconds=1)


