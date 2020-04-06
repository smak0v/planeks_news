from comments.models import PostComment
from django import forms
from django.contrib import admin
from django.db import models
from markdownx.admin import MarkdownxModelAdmin
from planeks_news.admin import admin_site

from .models import Post


class PostCommentInline(admin.StackedInline):
    model = PostComment
    readonly_fields = [
        'creator',
    ]
    max_num = 50
    extra = 0

    def has_add_permission(self, request, obj):
        return False


class PostAdmin(MarkdownxModelAdmin):
    list_display = [
        'pk',
        'creator',
        'timestamp',
        'status',
    ]
    list_filter = [
        'timestamp',
        'status',
    ]
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('body', 'creator', 'status', ),
        }),
    )
    search_fields = [
        'body',
        'creator',
        'timestamp',
    ]
    ordering = [
        'pk',
        'creator',
        'timestamp',
        'status',
    ]
    inlines = [
        PostCommentInline,
    ]
    list_per_page = 50


admin_site.register(Post, PostAdmin)
