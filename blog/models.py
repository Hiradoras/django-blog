from tokenize import blank_re
from django.urls import reverse
import profile
from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


class Post(models.Model):
    title = models.CharField(max_length=255)
    body = RichTextField()
    date_added = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField((""), upload_to='images/profile_pic_images', null=True, blank=True)

    bio = models.TextField(null=True, blank=True)
    website_url = models.CharField(max_length=255, null=True, blank=True)
    facebook_url = models.CharField(max_length=255, null=True, blank=True)
    twitter_url = models.CharField(max_length=255, null=True, blank=True)
    instagram_url = models.CharField(max_length=255, null=True, blank=True)
    pinterest_url = models.CharField(max_length=255, null=True, blank=True)
    other_url = models.CharField(max_length=255, null=True, blank=True)
     

    def __str__(self) -> str:
        return str(self.user)

    def get_absolute_url(self):
        return reverse('home')   

