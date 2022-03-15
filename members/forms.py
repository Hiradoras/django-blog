import email
from pyexpat import model
from django.contrib.auth.forms import UserCreationForm
from django import forms

from members.models import Profile


# class RegisterForm(UserCreationForm):
#     email = forms.EmailField(required=True)

#     class Meta:
#         model = Profile