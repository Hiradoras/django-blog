from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import RegisterForm


class UserRegisterView(CreateView):
    form_class = RegisterForm
    template_name = "members/register.html"
    success_url = reverse_lazy('login')

