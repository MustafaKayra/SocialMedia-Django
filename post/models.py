from django.db import models

class Post(models.Model):
    author = models.CharField(max_length=30,null=False,blank=False)
    title = models.CharField(max_length=100,null=False,blank=False)
    content = models.TextField(null=False,blank=False)
    email = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="C:/Users/kayra/socialmediaproject/static/img")

    def __str__(self):
        return f"{self.title}"
