import pdb

from django.db.transaction import atomic
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from projet10.mixins import MultipleSerializerMixin
from .serializers import ProjectDetailSerializer, ProjectListSerializer
from .models import Project
from app_authentication.models import Contributor


class ProjectViewset(MultipleSerializerMixin, ModelViewSet):
    permission_classes = [IsAuthenticated]

    serializer_class = ProjectListSerializer
    detail_serializer_class = ProjectDetailSerializer

    def get_queryset(self):
        return Project.objects.all()

    @atomic
    def perform_create(self, serializer):
        user = self.request.user
        new_project = serializer.save(author_user=user)
        Contributor.objects.create(user=user, project=new_project,
                                   permission="R")

