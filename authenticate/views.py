from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from authenticate.forms import UserCreationForm


class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'authenticate/register.html'
    success_url = reverse_lazy('login')
