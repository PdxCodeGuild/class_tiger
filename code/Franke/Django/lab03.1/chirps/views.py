from django.shortcuts import render

# Create your views here.

from .models import Chirp

def feed(request):
  userids = []
  for id in request.user.chirprprofile.follows.all():
    userids.append(id)

  userids.append(request.user.id)
  chirps = Chirp.objects.filter(user_id__in=userids)[0:25]

  return render(request, 'feed.html', {'chirps': chirps})