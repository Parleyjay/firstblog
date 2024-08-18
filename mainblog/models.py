from django.db import models


# Create your models here.
class Blog(models.Model):
    blog_title = models.CharField(max_length=200)
    blog_post = models.TextField()
    date_uploaded = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'{self.blog_title}'
