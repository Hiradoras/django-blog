from django import forms
from django.contrib.auth.models import User
from .models import(
    Post
)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'body')
        
        Widgets = {
            'title' : forms.TextInput(attrs={'class' : 'form-control'}),
            'body' : forms.Textarea(attrs={'class' : 'form-control'}),
        }
