from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from chirps.models import Chirp

class UserListView(generic.ListView):
    model = User
    template_name = 'user_list.html'

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

class ChirpList(generic.ListView):
    model = Chirp
    template_name = 'index.html'

    def get_queryset(self):
        chirp_objects = Chirp.objects.filter(author__username__exact=self.kwargs['username']).order_by('-created')
        return chirp_objects
