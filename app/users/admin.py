from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group

from .forms import UserChangeForm, UserCreationForm
from .models import User


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = [
        'email',
        'is_confirmed_email',
        'first_name',
        'last_name',
        'birthday_date',
        'is_active',
        'is_admin',
    ]
    list_filter = [
        'is_admin',
        'is_active',
        'is_confirmed_email',
        'birthday_date',
    ]
    fieldsets = (
        (None, {'fields': ['email', 'is_confirmed_email', 'password', 'is_active', ]}),
        ('Personal info', {'fields': ['first_name', 'last_name', 'birthday_date', ]}),
        ('Permissions', {'fields': ['is_admin', ]}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'birthday_date', 'is_admin', 'password1', 'password2'),
        }),
    )
    search_fields = [
        'email',
        'first_name',
        'last_name',
    ]
    ordering = [
        'email',
        'first_name',
        'last_name',
        'birthday_date',
    ]
    filter_horizontal = []
    list_per_page = 50


admin.site.register(User, UserAdmin)
