from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class ChirprProfile(models.Model):
  user = models.OneToOneField(User, on_delete=models.DO_NOTHING)
  follows = models.ManyToManyField('self', related_name='followed_by', symmetrical=False)

User.chirprprofile = property(lambda u: ChirprProfile.objects.get_or_create(user=u)[0])