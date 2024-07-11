from django.db import models
from django.utils.text import slugify
import random
import string

def generate_unique_slug(instance, new_slug=None):
    slug = new_slug or slugify(instance.title)
    Klass = instance.__class__
    if Klass.objects.filter(slug=slug).exists():
        random_string = ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))
        slug = f"{slug}-{random_string}"
        return generate_unique_slug(instance, slug)
    return slug


class Post(models.Model):
    author = models.CharField(max_length=30,null=False,blank=False)
    title = models.CharField(max_length=100,null=False,blank=False)
    content = models.TextField(null=False,blank=False)
    email = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(null=False,blank=True,unique=True,db_index=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = generate_unique_slug(self)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title}"