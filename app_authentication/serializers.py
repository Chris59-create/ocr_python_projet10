from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class SignUpSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'password')

    def validate_email(self, value):

        if User.objects.filter(email=value).exists():

            raise serializers.ValidationError("L'email est déjà utilisé")

        return value
