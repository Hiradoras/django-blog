from dataclasses import fields
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django import forms
from django.contrib.auth.models import User
from blog.models import Profile


class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class' : 'form-control'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class' : 'form-control'}))
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
        ]


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = (
            'bio',
            'profile_pic',
            'website_url',
            'facebook_url',
            'twitter_url',
            'instagram_url',
            'pinterest_url',
            'other_url'

        )

        widgets = {
                'bio' : forms.Textarea(attrs={'class' : 'form-control'}),
                # 'profile_pic' : forms.ImageField(attrs={'class' : 'form-control'}),
                # 'profile_pic' : forms.ImageField(), 
                'website_url' : forms.TextInput(attrs={'class' : 'form-control'}),
                'facebook_url' : forms.TextInput(attrs={'class' : 'form-control'}),
                'twitter_url' : forms.TextInput(attrs={'class':'form-control'}),
                'instagram_url' : forms.TextInput(attrs={'class' : 'form-control'}),
                'pinterest_url' : forms.TextInput(attrs={'class' : 'form-control'}),
                'other_url' : forms.TextInput(attrs={'class' : 'form-control'}),
            }


class EditSettingsForm(UserChangeForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class' : 'form-control'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class' : 'form-control'}))
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class' : 'form-control'}))
    # date_joined = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class' : 'form-control'}))

    class Meta:
        model = User
        fields = ('email', 'first_name','last_name','username','password')

class PasswordChangingForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'type':'password'}))
    new_password1 = forms.CharField(max_length=100,  label='New Password', widget=forms.PasswordInput(attrs={'class' : 'form-control', 'type':'password'}))
    new_password2 = forms.CharField(max_length=100, label='Password Validation', widget=forms.PasswordInput(attrs={'class' : 'form-control', 'type':'password'}))

    class Meta:
        model = User
        fields = ('old_password', 'new_password1','new_password2')
