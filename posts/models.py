from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField()
    description = models.CharField(max_length=130, null=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title