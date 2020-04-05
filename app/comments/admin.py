from django.contrib import admin

from .models import PostComment


class PostCommentAdmin(admin.ModelAdmin):
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


admin.site.register(PostComment, PostCommentAdmin)
