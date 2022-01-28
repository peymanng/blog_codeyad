from django.contrib import admin
from .models import  Post , Category , Author , Comment
from mptt.admin import MPTTModelAdmin
# Register your models here.

class PostInline(admin.StackedInline):
    model = Comment
    extra = 1

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title' , 'get_categories', 'slug' , 'tag_list' , 'pub_date')
    prepopulated_fields = {'slug' : ('title' ,)}
    list_filter = ('category' , 'pub_date' , 'tags')
    inlines = [PostInline]

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('tags')

    def tag_list(self, obj):
        return u", ".join(o.name for o in obj.tags.all())

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title' , 'slug')
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Comment , MPTTModelAdmin)
admin.site.register(Author)