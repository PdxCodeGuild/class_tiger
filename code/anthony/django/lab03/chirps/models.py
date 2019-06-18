from django.db import models
from django.urls import reverse


class Chirp(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    body = models.TextField(max_length=140)
    created = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.author

    def get_absolute_url(self):
        return reverse("chirp:detail", args=[str(self.id)])


class Comment(models.Model):
    post = models.ForeignKey('Chirp', on_delete=models.CASCADE)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    body = models.TextField(max_length=140)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author
