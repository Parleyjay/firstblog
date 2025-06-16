from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name



class Blog(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    blog_title = models.CharField(max_length=200)
    blog_post = models.TextField()
    date_uploaded = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='blogs', null=True)


    def __str__(self):
        return f'{self.blog_title}'
    


