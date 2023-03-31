# Generated by Django 4.1.7 on 2023-03-31 18:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("app_softdesk", "0002_delete_users"),
    ]

    operations = [
        migrations.CreateModel(
            name="Projects",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=128)),
                ("description", models.TextField(max_length=2048)),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("B", "Back-end"),
                            ("F", "Front-end"),
                            ("I", "IOS"),
                            ("A", "Android"),
                        ],
                        max_length=1,
                    ),
                ),
                (
                    "author_user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="projet_author",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Issues",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=128)),
                ("description", models.TextField(max_length=2048)),
                (
                    "tag",
                    models.CharField(
                        choices=[("A", "Amélioration"), ("B", "Bug"), ("T", "Tâche")],
                        max_length=1,
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[("F", "A faire"), ("C", "En cours"), ("T", "Terminé")],
                        max_length=1,
                    ),
                ),
                ("created_time", models.DateTimeField(auto_now_add=True)),
                (
                    "assignee_author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="assignee_author",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "author_user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="issue_author",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "project",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="app_softdesk.projects",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Comments",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("description", models.TextField(max_length=2048)),
                (
                    "author_user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="comment_author",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "issue",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="app_softdesk.issues",
                    ),
                ),
            ],
        ),
    ]