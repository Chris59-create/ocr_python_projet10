from django.conf import settings
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

from app_softdesk.models import Project


class UserManager(BaseUserManager):
    """Define a Manager with no username"""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):

    username = None
    first_name = models.CharField(max_length=100, blank=False)
    last_name = models.CharField(max_length=100, blank=False)
    email = models.EmailField(unique=True, blank=False)

    projects = models.ManyToManyField(
        Project,
        related_name='user',
        through='Contributor'
    )

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = []

    objects = UserManager()


class Contributor(models.Model):

    PERMISSION_CHOICES = (
        ('R', 'Responsable'),
        ('C', 'Contributeur')
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='Contributor',
        on_delete=models.CASCADE
    )
    project = models.ForeignKey(
        Project,
        related_name='Contributor',
        on_delete=models.CASCADE,
        null=True
    )
    permission = models.CharField(
        max_length=1,
        choices=PERMISSION_CHOICES,
        default='C'
    )

