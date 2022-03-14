from unicodedata import name
from django.urls import path
from blog.models import Post
from .views import (
    HomeView,
    PostDetailView,
    AddPostView)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('<int:pk>/detail', PostDetailView.as_view(), name='post-detail'),
    path('add_post', AddPostView.as_view(), name='add-post'),

]
