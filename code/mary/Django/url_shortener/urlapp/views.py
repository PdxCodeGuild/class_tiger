from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
import random, string

from .models import ShortUrl


def index(request):
    new_urls = ShortUrl.objects.all()
    context = {"new_urls":new_urls}
    return render(request, 'index.html', context)

def submit(request):
        short_list = ['A', 'b', 'C', 'x', '1', '3', '6', 'y', '&', '?']
        short_made = ''
        for num in range(6):
            short_made += random.choice(short_list)
        ShortUrl.objects.create(short_url=short_made)
        return HttpResponseRedirect(reverse("urlapp:shorten", args=(short_made,)))
        
def shorten(request, short_url):
    new_short = ShortUrl.objects.get(short_url=short_url)
    context={
        "new_short":new_short
    }
    return render(request, "index.html", context)




