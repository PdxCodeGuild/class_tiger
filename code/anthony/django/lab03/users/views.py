from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from django.contrib.auth.models import User

from chirps.models import Chirp


class SignupView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


class ChirpList(ListView):
    model = Chirp
    template_name = 'home.html'

    def get_queryset(self):
        return Chirp.objects.filter(author__username__exact=self.kwargs['username']).order_by('-created')
