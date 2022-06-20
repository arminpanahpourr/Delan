from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError

from .models import User
from django import forms
from django.utils.translation import gettext_lazy as _


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label=_('رمز عبور'), widget=forms.PasswordInput)
    password2 = forms.CharField(label=_('تایید رمز عبور'), widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('phone_number', 'password1', 'password2', 'first_name', 'last_name', 'email')

    def clean_password2(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']

        if password1 and password2 and password1 != password2:
            raise ValidationError(_('رمز عبور همخوانی ندارد'))
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField(
        help_text=_('you can change your password from <a href = "../password/" > this link </a>'))

    class Meta:
        model = User
        fields = ('phone_number', 'password', 'email', 'first_name', 'last_name')
