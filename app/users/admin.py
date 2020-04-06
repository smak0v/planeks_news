from django.contrib.auth.admin import GroupAdmin as OriginGroupAdmin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group
from planeks_news.admin import admin_site

from .forms import UserChangeForm, UserCreationForm, GroupAdminForm
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
        'is_staff',
        'is_admin',
    ]
    list_filter = [
        'is_admin',
        'is_staff',
        'is_active',
        'is_confirmed_email',
        'birthday_date',
    ]
    fieldsets = (
        (None, {'fields': ['email', 'is_confirmed_email', 'password', 'is_active', ]}),
        ('Personal info', {'fields': ['first_name', 'last_name', 'birthday_date', ]}),
        ('Permissions', {'fields': ['is_admin', 'is_staff', 'groups', ]}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email', 'first_name', 'last_name', 'birthday_date', 'is_staff', 'is_admin', 'password1', 'password2',),
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
    filter_horizontal = [
        'groups',
    ]
    list_per_page = 50


class GroupAdmin(OriginGroupAdmin):
    form = GroupAdminForm


admin_site.register(Group, GroupAdmin)
admin_site.register(User, UserAdmin)
