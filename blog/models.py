from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.db.models import Count


class Post(models.Model):
    title = models.CharField(max_length=255)
    snippet = models.TextField(max_length=255)
    body = RichTextField()
    date_added = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField((""), upload_to='images/profile', null=True, blank=True)

    bio = models.TextField(null=True, blank=True)
    website_url = models.CharField(max_length=255, null=True, blank=True)
    facebook_url = models.CharField(max_length=255, null=True, blank=True)
    twitter_url = models.CharField(max_length=255, null=True, blank=True)
    instagram_url = models.CharField(max_length=255, null=True, blank=True)
    pinterest_url = models.CharField(max_length=255, null=True, blank=True)
    other_url = models.CharField(max_length=255, null=True, blank=True)
    posts = models.IntegerField(default=0)
    # posts = Post.objects.filter(author=user).count()
    def __str__(self) -> str:
        return str(self.user)

    def get_absolute_url(self):
        return reverse('home')


    
    


