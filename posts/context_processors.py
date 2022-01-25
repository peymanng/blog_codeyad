from .models import Category , Post
from taggit.models import Tag

def all_categories(request):
    return {"all_categories" : Category.objects.all()}

def all_tags(request):
    return {"all_tags" : Tag.objects.all()}

def recent_posts(request):
    return {"recent_posts" : Post.objects.all().order_by('-pub_date')[:3]}