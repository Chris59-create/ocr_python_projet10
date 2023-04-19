from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from projet10.mixins import MultipleSerializerMixin
from .models import Contributor
from .serializers import SignUpSerializer, ContributorListSerializer, \
    ContributorDetailSerializer
from rest_framework import status
from rest_framework.response import Response


class SignupAPIView(APIView):
    permission_classes = (AllowAny,)

    serializer_class = SignUpSerializer

    def post(self, request, *args, **kwargs):

        user_data = request.data
        serializer = SignUpSerializer(data=user_data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()

            response = {
                "message": "Collaborateur crée avec succès",
                "data": serializer.data
            }

            return Response(data=response, status=status.HTTP_201_CREATED)

        return Response(
            data=serializer.data,
            status=status.HTTP_400_BAD_REQUEST
        )


class ContributorViewset(MultipleSerializerMixin, ModelViewSet):
    permission_classes = [IsAuthenticated]

    serializer_class = ContributorListSerializer
    detail_serializer_class = ContributorDetailSerializer

    def get_queryset(self):
        return Contributor.objects.all()
