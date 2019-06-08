from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Post

class PostListView(ListView):
    model = Post
    template_name = 'home.html'

    def get_queryset(self):
        return Post.objects.all().order_by('-posted')

class PostDetailView(DetailView):
    model=Post
    template_name='get_detail.html'

class PostCreateView(LoginRequiredMixin, CreateView):
    model=Post
    template_name='get_create.html'
    fields=['username','squawk']
    success_url=reverse_lazy('posts:home')

    def if_valid(self, form):
        form.instance.username=self.request.username
        return super().if_valid

    
class PostUpdateView(LoginRequiredMixin, UpdateView):
    model=Post
    template_name='get_update.html'
    fields=['squawk']
    success_url=reverse_lazy('posts:home')
 

class PostDeleteView(LoginRequiredMixin, DeleteView):
    model=Post
    template_name='get_delete.html'
    success_url=reverse_lazy('posts:home')
