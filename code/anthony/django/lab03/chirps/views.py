from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect

from .models import Chirp, Comment


class ChirpListView(ListView):
    model = Chirp
    template_name = 'home.html'

    def get_queryset(self):
        return Chirp.objects.order_by('-created')


class ChirpDetailView(DetailView):
    model = Chirp
    template_name = 'chirp_detail.html'


class ChirpCreateView(LoginRequiredMixin, CreateView):
    model = Chirp
    template_name = 'chirp_create.html'
    fields = 'body',
    success_url = reverse_lazy('chirps:home')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ChirpDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Chirp
    template_name = 'chirp_delete.html'
    success_url = reverse_lazy('chirps:home')

    def test_func(self):
        chirp = self.get_object()
        return chirp.author == self.request.user


@login_required
def post_comment(request, pk):
    chirp = get_object_or_404(Chirp, pk=pk)
    Comment.objects.create(
        post=chirp,
        author=request.user,
        body=request.POST['comment'],
    )
    return HttpResponseRedirect(reverse('chirps:detail', kwargs={'pk': pk}))


@login_required
def add_like(request, pk):
    chirp = get_object_or_404(Chirp, pk=pk)
    chirp.likes += 1
    chirp.save()

    return HttpResponseRedirect(reverse('chirps:detail', kwargs={'pk': pk}))
