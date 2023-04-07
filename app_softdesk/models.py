from django.db import models
from django.conf import settings


class Project(models.Model):
    objects = models.Manager()

    TYPE_CHOICES = [
        ('B', 'Back-end'),
        ('F', 'Front-end'),
        ('I', 'IOS'),
        ('A', 'Android'),
    ]

    title = models.CharField(max_length=128)
    description = models.TextField(max_length=2048)
    type = models.CharField(max_length=1, choices=TYPE_CHOICES)
    author_user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='projet_author'
    )


class Issue(models.Model):
    objects = models.Manager()

    TAG_CHOICES = [
        ('A', 'Amélioration'),
        ('B', 'Bug'),
        ('T', 'Tâche'),
    ]

    PRIORITY_CHOICES = [
        ('F', 'Faible'),
        ('M', 'Moyenne'),
        ('É', 'Élevée'),
    ]

    STATUS_CHOICES = [
        ('F', 'A faire'),
        ('C', 'En cours'),
        ('T', 'Terminé'),
    ]

    title = models.CharField(max_length=128)
    description = models.TextField(max_length=2048)
    tag = models.CharField(max_length=1, choices=TAG_CHOICES)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    author_user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='issue_author'
    )
    assignee_author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='assignee_author'
    )
    created_time = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    objects = models.Manager()

    description = models.TextField(max_length=2048)
    author_user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='comment_author'
    )
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)
