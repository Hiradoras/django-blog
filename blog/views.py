from msilib.schema import ListView
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView
from .models import Post

class HomeView(ListView):
    model = Post
    template_name = 'blog/home.html'
