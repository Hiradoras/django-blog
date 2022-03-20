from django.urls import path
from .views import CreateProfileView, EditProfilePageView, ShowProfilePageView, register

urlpatterns = [
    path("", register, name="register"),
    path("create_profile", CreateProfileView.as_view(), name="create-profile"),
    path("<int:pk>/profile", ShowProfilePageView.as_view(), name="show-profile"),
    path("<int:pk>/edit_profile", EditProfilePageView.as_view(), name="edit-profile"),



]
