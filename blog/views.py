from msilib.schema import ListView
from re import template
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, DetailView
from .models import Post

class HomeView(ListView):
    model = Post
    template_name = 'blog/home.html'
    ordering = ['-date_added']


class PostDetailView(DetailView):
    model = Post
    template_name  = 'blog/post_detail.html'
