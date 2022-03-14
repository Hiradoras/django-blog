from msilib.schema import ListView
from re import template
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post
from .forms import PostForm

class HomeView(ListView):
    model = Post
    template_name = 'blog/home.html'
    ordering = ['-date_added']


class PostDetailView(DetailView):
    model = Post
    template_name  = 'blog/post_detail.html'

class AddPostView(CreateView):
    model =Post
    form_class = PostForm
    template_name = 'blog/add_post.html'