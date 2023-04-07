from django.contrib import admin

from app_softdesk.models import Project, Issue, Comment

admin.site.register(Project)
admin.site.register(Issue)
admin.site.register(Comment)
