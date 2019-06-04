import random
import string

from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.http import HttpResponse
from django.template import loader

from .models import URL, UserData

def shortcode_generator():
    shortcode_list = []
    for n in range(0,3):
        shortcode_list += random.choice(string.ascii_letters)
        shortcode_list += random.choice(string.digits)

    return ''.join(shortcode_list)

def indexView(request):
    URLs = URL.objects.order_by('pk')
    context = {
        'URLs' : URLs,
    }
    return render(request, 'urlshortenerapp/index.html' , context)

def addURL(request):
    url_input = request.POST['url_input']
    shortcode = shortcode_generator()
    newURL = URL( long_URL = url_input ,short_URL = shortcode )

    newURL.save()

    return HttpResponseRedirect(reverse('urlshortenerapp:indexView'))

def viewShortcode(request, short_URL ):
    targetURL = get_object_or_404(URL, short_URL = short_URL )
    # print('printing stuff')
    # print(request.META['REMOTE_ADDR'])
    user = request.META['HTTP_USER_AGENT']
    ip = request.META['REMOTE_ADDR']
    user_data = UserData(user_agent=user, ip_addr = ip, url = targetURL)
    user_data.save()

    return redirect(targetURL.long_URL)


def infoView(request):
    URLs = URL.objects.order_by('pk')
    user_data = UserData.objects.order_by('pk')
    num_visits = []
    for item in URLs:
        # print(item.short_URL)
        y = URL.objects.get(short_URL = item.short_URL)
        visits = len(y.userdata_set.all())
        num_visits.append(visits)
        # print(y.userdata_set.all())


    context = {
        'URLs': URLs,
        'num_visits': num_visits,
        'user_data': user_data,
    }

    return render(request, 'urlshortenerapp/info.html', context)

# y = URL.objects.get(short_URL='l3E3b5')
# y.userdata_set.all()