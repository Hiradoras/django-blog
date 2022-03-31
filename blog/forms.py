from dataclasses import field
from tkinter import Widget
from django import forms
from django.contrib.auth.models import User
from .models import(
    Post
)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'body','snippet')
        
        Widgets = {
            'title' : forms.TextInput(attrs={'class' : 'form-control'}),
            'body' : forms.Textarea(attrs={'class' : 'form-control'}),
            'snippet' : forms.TextInput(attrs={'class' : 'form-control'})
        }

class EditPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'body','snippet')

        Widgets = {
            'title' : forms.TextInput(attrs={'class' : 'form-control'}),
            'body' : forms.Textarea(attrs={'class' : 'form-control'}),
            'snippet' : forms.TextInput(attrs={'class' : 'form-control'})
        }