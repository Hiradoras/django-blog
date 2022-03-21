from django.urls import path
from .views import CreateProfileView, EditProfilePageView, EditSettingsView, PasswordsChangeView, ShowProfilePageView, register
from . import views

urlpatterns = [
    path("", register, name="register"),
    path("create_profile", CreateProfileView.as_view(), name="create-profile"),
    path("<int:pk>/profile", ShowProfilePageView.as_view(), name="show-profile"),
    path("<int:pk>/edit_profile", EditProfilePageView.as_view(), name="edit-profile"),
    path("<int:pk>/edit_settings", EditSettingsView.as_view(), name='edit-settings'),
    path('password/', PasswordsChangeView.as_view(template_name = "registration/change_password.html")),
    path('password_success', views.password_success, name= "password_success"),




]
