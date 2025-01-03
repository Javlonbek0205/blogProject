from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post
# Create your views here.
class BlogListView(ListView):
  model = Post
  template_name = 'home.html'

class BlogDetailView(DetailView):
  model = Post
  template_name = 'post_detail.html'

class BlogPostNewView(CreateView):
  model = Post
  template_name = 'new_post.html'
  fields = ['title', 'author', 'body']

class BlogPostEditView(UpdateView):
  model = Post
  template_name = 'post_edit.html'
  fields = ['title', 'body']

class BlogDelateView(DeleteView):
  model = Post
  template_name = 'delate_post.html'
  success_url = reverse_lazy('home')
