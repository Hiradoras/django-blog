from django.urls import path
from .views import CreateProfileView, register

urlpatterns = [
    path("", register, name="register"),
    path("create_profile", CreateProfileView.as_view(), name="create-profile"),

]
