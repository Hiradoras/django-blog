from django.shortcuts import render, redirect
from .forms import ProfileForm, RegisterForm
from blog.models import Profile
from django.views.generic import CreateView



def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
        
        return redirect("login")
    else:
        form = RegisterForm()
    return render(response, "register/register.html",{"form":form})


class CreateProfileView(CreateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'registration/create_profile.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

