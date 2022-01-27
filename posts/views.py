from taggit.models import Tag
from django.shortcuts import render, get_list_or_404 , get_object_or_404
from django.views.generic import ListView, TemplateView
from django.http import HttpResponseRedirect
from .models import  Post
from .forms import NewCommentForm

class PostListView(ListView):
    model = Post
    template_name = 'blog.html'
    context_object_name = 'posts'
    paginate_by = 2

def detail_view(request , slug):
    post =get_object_or_404(Post , slug=slug)
    allcomments = post.comments.filter(status=True,parent=None).order_by('-pub_date')
    children = allcomments.get_descendants()
    user_comment = None

    if request.method == 'POST':
        comment_form = NewCommentForm(request.POST)
        if comment_form.is_valid():
            user_comment = comment_form.save(commit=False)
            user_comment.post = post
            user_comment.save()
            return HttpResponseRedirect('/posts/post/' + post.slug)
    else:
        comment_form = NewCommentForm()
    return render(request,
                  'post-details.html',
                  {'post': post,
                   'comments':  user_comment,
                   'comment_form': comment_form
                    ,'allcomments': allcomments,
                    'replies' : children,
                   })


class CategoryPostList(TemplateView):
    template_name = 'blog.html'
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        category_slug = context['slug']
        context['posts'] = get_list_or_404(Post , category__title__icontains=category_slug)
        return context

class TagsPostListView(TemplateView):
    template_name = 'blog.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        tag_slug = context['slug']
        tag = get_object_or_404(Tag, slug=tag_slug)
        context['posts'] = get_list_or_404(Post , tags__name__in=[tag])
        return context
