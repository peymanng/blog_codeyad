from django.shortcuts import render, get_list_or_404
from django.views.generic import ListView, TemplateView
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

class CategoryPostList(TemplateView):
    template_name = 'blog.html'
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        category_slug = context['slug']
        context['posts'] = get_list_or_404(Post , category__title__icontains=category_slug)
        return context