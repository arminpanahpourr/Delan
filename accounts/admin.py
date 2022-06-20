

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group
from django.utils.translation import gettext_lazy as _
from accounts.forms import UserChangeForm, UserCreationForm
from accounts.models import User


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('phone_number', 'email', 'first_name', 'last_name')
    list_filter = ('is_staff', 'is_superuser')
    fieldsets = (
        (None, {'fields': ('phone_number', 'password')}),
        (_('اطلاعات شخصی'), {'fields': ('email', 'first_name', 'last_name')}),
        (_('دسترسی ها'), {'fields': ('is_superuser', 'is_staff', 'is_active')})
    )

    add_fieldsets = (
        (None, {'fields': ('phone_number', 'password1', 'password2')}),
        (_('اطلاعات شخصی'), {'fields': ('email', 'first_name', 'last_name')}),
        (_('دسترسی ها'), {'fields': ('is_superuser', 'is_staff', 'is_active')})
    )

    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()


admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
