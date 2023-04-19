from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from .serializers import ProjectDetailSerializer, ProjectListSerializer
from .models import Project


class ProjectViewset(ModelViewSet):
    permission_classes = [IsAuthenticated]

    serializer_class = ProjectListSerializer
    detail_serializer_class = ProjectDetailSerializer

    def get_queryset(self):
        return Project.objects.all()

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return self.detail_serializer_class
        return super().get_serializer_class()

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(author_user=user)

