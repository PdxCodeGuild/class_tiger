from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Chirp(models.Model):
  user = models.ForeignKey(User, related_name='chirps', on_delete=models.DO_NOTHING)
  body = models.CharField(max_length=255)
  created_at = models.DateTimeField(auto_now_add=True)
# This is because it's a ForeignKey and it's required, if we try to save it
#  before we add it the form will not validate. 
  class Meta:
    ordering = ('-created_at',)