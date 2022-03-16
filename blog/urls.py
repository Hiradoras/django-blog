from django.urls import path, include 
from blog.models import Post
from django.contrib.auth.decorators import login_required
from .views import (
    HomeView,
    PostDetailView,
    AddPostView,

    )

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('<int:pk>/detail', PostDetailView.as_view(), name='post-detail'),
    path('', include("django.contrib.auth.urls")),
    path('add_post', AddPostView.as_view(), name= 'add-post' ),


]
