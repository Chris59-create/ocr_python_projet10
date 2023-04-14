from faker import Faker
from django.urls import reverse
from rest_framework.test import APITestCase

from .models import User


class TestSetUp(APITestCase):

    def setUp(self):

        self.signup_url = reverse('app_authentication:signup')

        self.fake = Faker('fr_FR')

        self.user_data = {
            'email': self.fake.email(),
            'first_name': self.fake.first_name(),
            'last_name': self.fake.last_name(),
            'password': self.fake.password(),
        }

        self.existing_email = self.user_data['email']

        return super().setUp()

    def tearDown(self):
        return super().tearDown()


class TestAuthentication(TestSetUp):

    def test_no_signup_without_data(self):

        res = self.client.post(self.signup_url)
        self.assertEqual(res.status_code, 400)

    def test_signup(self):
        res = self.client.post(self.signup_url, self.user_data, format="json")

        self.assertEqual(res.status_code, 201)

    def test_no_signup_with_existing_email(self):

        User.objects.create_user(self.user_data)
        res = self.client.post(
            self.signup_url,
            self.user_data['email'],
            format="json"
        )

        self.assertEqual(res.status_code, 400)
