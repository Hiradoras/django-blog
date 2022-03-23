import profile
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse_lazy
from .forms import EditSettingsForm, ProfileForm, RegisterForm, PasswordChangingForm
from blog.models import Post, Profile
from django.views.generic import CreateView, DetailView, UpdateView
from django.views import generic
from django.contrib.auth.views import PasswordChangeView
from django.db.models import Count


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
        # users = Profile.objects.all()
        context = super(ShowProfilePageView, self).get_context_data(*args, **kwargs)
        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])
        context['page_user'] = page_user
        return context
    
    def get_context_data(self,**kwargs):
        context = super(ShowProfilePageView,self).get_context_data(**kwargs)
        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])
        post_list_for_count = Post.objects.all().filter(author=page_user.user)
        post_list = Post.objects.filter(author=page_user.user)
        #context['post_list'] = post_list
        context['post_list'] = post_list.order_by('-date_added')
        context['post_count'] = post_list_for_count.count()
        return context

class EditProfilePageView(generic.UpdateView):
    model =Profile
    template_name = 'registration/edit_profile.html'
    fields = [
        'bio',
        'profile_pic',
        'website_url',
        'facebook_url',
        'twitter_url',
        'instagram_url',
        'pinterest_url'
        ]
    success_url = reverse_lazy('home')

class EditSettingsView(generic.UpdateView):
    form_class = EditSettingsForm
    template_name = 'registration/edit_settings.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user


class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangingForm
    success_url = reverse_lazy('login')

def password_success(request):
    return render(request, 'registration/password_success.html')

        
