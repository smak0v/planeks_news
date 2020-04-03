from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email, first_name=None, last_name=None, birthday_date=None, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            birthday_date=birthday_date,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name=None, last_name=None, birthday_date=None, password=None):
        user = self.create_user(
            email,
            first_name=first_name,
            last_name=last_name,
            birthday_date=birthday_date,
            password=password,
        )
        user.is_admin = True
        user.is_active = True
        user.save(using=self._db)
        return user
