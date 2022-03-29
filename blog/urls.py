from django.urls import path, include 
from blog.models import Post
from django.contrib.auth.decorators import login_required
from .views import (
    DeletePostView,
    EditPostView,
    HomeView,
    PostDetailView,
    AddPostView,

    )

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('<int:pk>/detail', PostDetailView.as_view(), name='post-detail'),
    path('', include("django.contrib.auth.urls")),
    path('add_post', AddPostView.as_view(), name= 'add-post' ),
    path('<int:pk>/delete_post', DeletePostView.as_view(), name="delete-post"),
    path('<int:pk>/edit_post', EditPostView.as_view(), name="edit-post"),
    

]
