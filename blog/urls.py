from django.urls import path
from blog.models import Post
from .views import HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),

]
