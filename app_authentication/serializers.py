from django.contrib.auth.hashers import make_password
from django.contrib.auth import get_user_model, authenticate
from rest_framework import serializers
from rest_framework.serializers import api_settings

USER_MODEL = get_user_model()


class SignUpSerializer(serializers.ModelSerializer):

    class Meta:
        model = USER_MODEL
        fields = ('email', 'first_name', 'last_name', 'password')
        extra_kwargs = {
            'email': {
                'error_messages': {
                    'unique': 'Un utilisateur avec cet email existe déjà'
                }
            },
        }

    def validate_password(self, value):
        # Hashes the password
        return make_password(value)


class LoginSerializer(serializers.ModelSerializer):

    class Meta:
        model = USER_MODEL
        fields = ['email', 'password']

    def validate(self, attrs):

        email = attrs.get('email', None)
        password = attrs.get('password', None)

        if not email:
            raise serializers.ValidationError(
                'Une adresse email est requise pour se connecter'
            )

        if not password:
            raise serializers.ValidationError(
                'Le mot de passe est requis pour se connecter'
            )

        user = authenticate(email=email, password=password)

        if not user:
            raise serializers.ValidationError(
                "Pas d'utilisateur correspondant à cet email et mot de passe"
            )

        return attrs
