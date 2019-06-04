from django.db import models


class URL(models.Model):
    url_long = models.CharField(max_length=200)
    url_short = models.CharField(max_length=12, null=True, blank=True)
    number_of_times_clicked = models.IntegerField(default=0)


class USER(models.Model):
    language = models.CharField(max_length=200, null=True, blank=True)
    ip_address = models.CharField(max_length=200, null=True, blank=True)
    hostname = models.CharField(max_length=200, null=True, blank=True)
