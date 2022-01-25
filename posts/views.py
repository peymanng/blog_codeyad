from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from .models import  Post

class PostListView(ListView):
    model = Post
    template_name = 'blog.html'
    context_object_name = 'posts'
    paginate_by = 6

class PostDetailView(DetailView):
    model = Post
    template_name = 'post-details.html'
    context_object_name = 'post'