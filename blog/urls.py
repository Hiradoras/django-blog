from django.urls import path
from blog.models import Post
from django.contrib.auth.decorators import login_required
from .views import (
    HomeView,
    PostDetailView,
    )

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('<int:pk>/detail', PostDetailView.as_view(), name='post-detail'),

]
