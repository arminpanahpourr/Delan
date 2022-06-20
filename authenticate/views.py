from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView

from authenticate.forms import UserCreationForm, UserLoginForm


class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'authenticate/register.html'
    success_url = reverse_lazy('accounts:login')


class LoginView(View):
    form_class = UserLoginForm
    template_name = 'authenticate/login.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home:home')
        return super().dispatch(request, *args, *kwargs)

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(
                phone_number=cd['phone_number'],
                password=cd['password'],
            )
            if user is not None:
                login(request, user)
                return redirect('home:home')
            return render(request, self.template_name, {'form': form})
        return render(request, self.template_name, {'form': form})


