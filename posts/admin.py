from django.contrib import admin
from .models import  Post , Category , Author

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title' , 'get_categories', 'slug' , 'get_visits' , 'number_of_likes' , 'tag_list' , 'pub_date')
    prepopulated_fields = {'slug' : ('title' ,)}

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('tags')

    def tag_list(self, obj):
        return u", ".join(o.name for o in obj.tags.all())

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title' , 'slug')
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Author)