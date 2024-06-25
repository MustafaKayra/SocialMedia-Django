from django.db import models

class Tweet(models.Model):
    name = models.CharField(max_length=50,null=False,blank=False)
    email = models.CharField(max_length=50,null=False,blank=False)
    content = models.TextField(null=False,blank=False)

    def __str__(self):
        return f"{self.content}"
