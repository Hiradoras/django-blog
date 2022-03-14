from msilib.schema import ListView
from django.shortcuts import render
from django.views.generic import ListView
from .models import Post

class HomeView(ListView):
    model = Post
    template_name = 'blog/home.html'
