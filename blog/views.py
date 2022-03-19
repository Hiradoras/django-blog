from msilib.schema import ListView
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from .models import Post
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User


class HomeView(ListView):
    model = Post
    template_name = 'blog/home.html'
    ordering = ['-date_added']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class PostDetailView(DetailView):
    model = Post
    template_name  = 'blog/post_detail.html'

class AddPostView(CreateView):
    model =Post
    form_class = PostForm
    template_name = 'blog/add_post.html'


    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # I FORGOT TO CHANGE form.instance.user TO form.insance.author. THAT WAS THE PROBLEM.
    # NOW I CAN GRAB AUTHOR FROM USER 

    
    # def form_valid(self, form):
    #     form.instance.user = self.request.user
    #     return super().form_valid(form)

    success_url = reverse_lazy('home')
    