from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.core.management.base import BaseCommand
from news.models import Post


class Command(BaseCommand):
    help = 'Create init groups and permissions'

    def handle(self, *args, **options):
        users_group, created_users_group = Group.objects.get_or_create(name='users')
        editors_group, created_editors_group = Group.objects.get_or_create(name='editors')
        administrators_group, created_administrators_group = Group.objects.get_or_create(name='administrators')

        content_type = ContentType.objects.get_for_model(Post)
        need_pre_moderation_permission, created = Permission.objects.get_or_create(codename='need_pre_moderation',
                                                                                   name='Need pre moderation',
                                                                                   content_type=content_type)

        if need_pre_moderation_permission:
            users_group.permissions.add(need_pre_moderation_permission)
        else:
            users_group.permissions.add(created)
