from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
import random, string

from .models import Short


def home(request):
    url_list = Short.objects.all()
    context = {"url_list":url_list}
    return render(request, 'shorturl/index.html', context)

def add(request):
    if request.method == "GET":
            return render(request, "shorturl/")
    elif request.method == "POST":
        http_check = request.POST['new_url']
        print(http_check)

        if "//" not in http_check:
            http_check = "//" + http_check

        code_list=[]
        for n in range(2):
            code=random.choice(string.ascii_lowercase)
            code2=random.choice(string.ascii_uppercase)
            code3=random.choice(string.digits)
            code_list.append(code)
            code_list.append(code2)
            code_list.append(code3)
        random.shuffle(code_list)
        short_code= "".join(code_list)
        Short.objects.create(big_url=http_check, short=short_code)
       

    return HttpResponseRedirect(reverse("shorturl:shorty", args=(short_code,)))
def show_short(request, short):
    short_url = Short.objects.get(short=short)
    context={
        "short_url":short_url
    }

    return render(request, "shorturl/shorty.html", context)

def link(request, short):
    redirect = get_object_or_404(Short, short=short)
    redirect.hits+=1
    redirect.save()
    return HttpResponseRedirect(redirect.big_url)

