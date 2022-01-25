from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from taggit.managers import TaggableManager

class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Category(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField()
    description = models.CharField(max_length=130, null=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(unique=True, allow_unicode=True)
    category = models.ManyToManyField(Category)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='post')
    description = models.CharField(max_length=100)
    body = RichTextUploadingField()
    pub_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    image = models.ImageField(upload_to='posts/')
    tags = TaggableManager()

    def __str__(self):
        return self.title

    def get_categories(self):
        return ' , '.join([category.title for category in self.category.all()])

    def get_absolute_url(self):
        return f'/posts/post/{self.slug}'
