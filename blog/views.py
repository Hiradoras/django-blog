from audioop import reverse
from msilib.schema import ListView
from re import template
import re
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import Post
from .forms import  EditPostForm, PostForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model


class HomeView(ListView):
    model = Post
    template_name = 'blog/home.html'
    ordering = ['-date_added']


    def get_context_data(self,**kwargs):
        all_users = User.objects.all()
        posts = Post.objects.all()
        users_to_show = []
        for u in all_users:
            post_count = posts.filter(author=u).count()
            if post_count > 0:
                users_to_show.append(u)
        context = super(HomeView,self).get_context_data(**kwargs)
        context['user_list'] = users_to_show
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class PostDetailView(DetailView):
    model = Post
    template_name  = 'blog/post_detail.html'
    slug_field = "slug"

    form = CommentForm

    def post(self, requset, *args, **kwargs):
        form = CommentForm(requset.POST)
        if form.is_valid():
            post = self.get_object()
            form.instance.user = requset.user
            form.instance.post = post
            form.save()

            return redirect(reverse("post", kwargs={
                "slug": post.slug
            }))
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = self.form  
        return context
    




class AddPostView(CreateView):
    model = Post
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
    
class DeletePostView(DeleteView):
    model = Post
    template_name = 'blog/delete_post.html'
    success_url = reverse_lazy('home')

class EditPostView(UpdateView):
    model = Post
    form_class = EditPostForm
    template_name = 'blog/edit_post.html'
    success_url = reverse_lazy('home')
    


