from django.contrib import admin
from planeks_news.admin import admin_site

from .models import PostComment


class PostCommentAdmin(admin.ModelAdmin):
    readonly_fields = [
        'creator',
        'post',
    ]
    list_display = [
        'post',
        'creator',
        'timestamp',
        'body',
    ]
    list_filter = [
        'timestamp',
    ]
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('post', 'creator', 'body',),
        }),
    )
    search_fields = [
        'post',
        'creator',
        'timestamp',
        'body',
    ]
    ordering = [
        'post',
        'creator',
        'timestamp',
        'body',
    ]
    filter_horizontal = []
    list_per_page = 50


admin_site.register(PostComment, PostCommentAdmin)
