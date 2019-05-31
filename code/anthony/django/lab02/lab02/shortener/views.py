from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
import random

from .models import URL, USER


def minified_url():
    characters = 'abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    short_url = ''
    i = 0
    while(i < 9):
        short_url += random.choice(characters)
        i += 1
    return short_url


def index(request):
    if(request.method == 'POST'):
        try:
            temp_url = URL.objects.get(url_long=request.POST['url-input'])
        except(KeyError, URL.DoesNotExist):
            temp_url = URL(
                url_long=request.POST['url-input'], url_short=minified_url())
            temp_url.save()
        return render(request, 'shortener/index.html', {'url': temp_url})
    else:
        return render(request, 'shortener/index.html')


def new_url(request, url_short):
    urlObj = get_object_or_404(URL, url_short=url_short)
    url = urlObj.url_long
    urlObj.number_of_times_clicked += 1
    try:
        new_user = USER.objects.get(ip_address=request.META['REMOTE_ADDR'])
    except(KeyError, USER.DoesNotExist):
        new_user = USER(language=request.META['HTTP_ACCEPT_LANGUAGE'],
                        ip_address=request.META['REMOTE_ADDR'], hostname=request.META['REMOTE_HOST'])
    if (url.startswith('https://') or url.startswith('//') or url.startswith('http://')):
        return redirect(url)
    else:
        url = '//' + url
    new_user.save()
    urlObj.save()
    return redirect(url)
