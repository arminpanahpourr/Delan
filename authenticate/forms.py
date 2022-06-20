from accounts.models import User
from django import forms
from django.utils.translation import gettext_lazy as _


class UserCreationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'


class UserLoginForm(forms.Form):
    phone_number = forms.CharField(label=_('شماره تلفن'), widget=forms.TextInput())
    password = forms.CharField(label=_('رمز عبور'), widget=forms.PasswordInput())
