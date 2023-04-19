from django.contrib.auth.hashers import make_password
from django.contrib.auth import get_user_model
from rest_framework import serializers

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
