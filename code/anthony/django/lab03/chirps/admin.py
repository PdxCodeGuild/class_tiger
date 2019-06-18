from django.contrib import admin

from .models import Chirp, Comment

admin.site.register(Chirp)
admin.site.register(Comment)
