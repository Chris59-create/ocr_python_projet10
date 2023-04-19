from rest_framework.serializers import ModelSerializer

from . models import Project


class ProjectListSerializer(ModelSerializer):

    class Meta:
        model = Project
        fields = ['title', 'description', 'type',]


class ProjectDetailSerializer(ModelSerializer):

    class Meta:
        model = Project
        fields = ['title', 'description', 'type', 'author_user']


class ProjectCreateSerializer(ModelSerializer):

    class Meta:
        model = Project
        fields = ['title', 'description', 'type']

