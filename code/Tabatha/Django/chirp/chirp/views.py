from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, View
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from forms.forms import NewChirpForm
from .models import Chirp

class LoginView(LoginRequiredMixin, View):
    login_url = 'login'
    redirect_field_name = 'new'

class ChirpListView(ListView):
    model = Chirp
    template_name = 'feed.html'

    def get_queryset(self):
        return Chirp.objects.all().order_by('-posted')

class ChirpDetailView(DetailView):
    model = Chirp
    template_name = 'chirp_detail.html'

class ChirpCreateView(LoginRequiredMixin, CreateView):
    model = Chirp
    template_name = 'new_chirp.html'
    # fields = ['text',]
    form_class= NewChirpForm
    success_url = reverse_lazy('chirp:new')

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['chirp_list'] = Chirp.objects.all().order_by('-posted')
            context['chirp_count'] = Chirp.objects.all().filter(creator__username=self.request.user.username).count()
            return context
        

class ChirpDeleteView(LoginRequiredMixin, DeleteView):
    model = Chirp
    template_name = 'delete_chirp.html'
    success_url = reverse_lazy('chirp:new')