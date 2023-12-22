from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=255)
    brief = models.CharField(max_length=511)
    content = models.TextField()
    image = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(default=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    
class Comment(models.Model):
    name = models.CharField(max_length=255)
    comment = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(default=1)
