from django.shortcuts import get_object_or_404, render, redirect
from .forms import ProfileForm, RegisterForm
from blog.models import Profile
from django.views.generic import CreateView, DetailView



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


class ShowProfilePageView(DetailView):
    model = Profile
    template_name = 'registration/show_profile.html'

    def get_context_data(self,*args, **kwargs):
        users = Profile.objects.all()
        context = super(ShowProfilePageView, self).get_context_data(*args, **kwargs)
        
        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])

        context['page_user'] = page_user
        return context