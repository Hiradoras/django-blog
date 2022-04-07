from dataclasses import field
from tkinter import Widget
from django import forms
from django.contrib.auth.models import User
from django_quill.forms import QuillFormField
from .models import(
    Post
)

class PostForm(forms.ModelForm):
    content = QuillFormField()
    class Meta:
        model = Post
        fields = ('title', 'content','snippet')
        
        Widgets = {
            'title' : forms.TextInput(attrs={'class' : 'form-control'}),
            'content' : forms.Textarea(attrs={'class' : 'form-control'}),
            'snippet' : forms.TextInput(attrs={'class' : 'form-control'})
        }

class EditPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content','snippet')

        Widgets = {
            'title' : forms.TextInput(attrs={'class' : 'form-control'}),
            'content' : forms.Textarea(attrs={'class' : 'form-control'}),
            'snippet' : forms.TextInput(attrs={'class' : 'form-control'})
        }