from .models import Category
from taggit.models import Tag

def all_categories(request):
    return {"all_categories" : Category.objects.all()}

def all_tags(request):
    return {"all_tags" : Tag.objects.all()}