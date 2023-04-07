from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from rest_framework_jwt.utils import jwt_payload_handler

from .serializers import UserSerializer
from .models import User


class CreateUserAPIView(APIView):
    # Permission to reconsider (only by responsable ?)
    permission_classes = (AllowAny,)

    def post(self, request):

        user = request.data
        serializer = UserSerializer(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['POST'])
@permission_classes ([AllowAny])
def authenticate_user(request):

    try:
        email = request.data['email']
        password = request.data['password']

        user = User.objects.get(email=email, password=password)

        if user:
            try:
                payload = jwt_payload_handler(user)
