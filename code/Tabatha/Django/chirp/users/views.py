from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.models import User

from chirp.models import Chirp

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

class MyChirpList(generic.ListView):
    model = Chirp
    template_name = 'feed.html'

    def get_queryset(self):
        return Chirp.objects.filter(creator__username__exact=self.kwargs['username']).order_by('-posted')

class UserListView(generic.ListView):
    model = User
    template_name = 'user_list.html'