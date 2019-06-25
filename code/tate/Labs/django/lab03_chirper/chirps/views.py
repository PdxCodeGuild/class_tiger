from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Chirp

class HomeView(ListView):
    model = Chirp
    template_name = 'index.html'

    def get_queryset(self):
        return Chirp.objects.all().order_by('-created')

class ChirpDetail(DetailView):
    model = Chirp
    template_name = 'chirp_detail.html'

class ChirpCreate(LoginRequiredMixin, CreateView):
    model = Chirp
    template_name = 'chirp_new.html'
    fields = ['title','body']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class ChirpDelete (LoginRequiredMixin, DeleteView):
    model = Chirp
    template_name = 'chirp_delete.html'
    success_url = reverse_lazy('chirps:index')

class ChirpEdit (LoginRequiredMixin, UpdateView):
    model = Chirp
    template_name = 'chirp_edit.html'
    fields = ['title','body']
