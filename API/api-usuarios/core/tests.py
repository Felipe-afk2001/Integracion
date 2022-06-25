# Django
from django.test import TestCase

# Python
import tempfile
import json

# Django Rest Framework
from rest_framework.test import APIClient
from rest_framework import status

# Models
from core.models import Usuario


class UserTestCase(TestCase):
    def setUp(self):
        user = Usuario(
            username='test_user'
        )
        user.set_password('admin123')
        user.save()

    def test_signup_user(self):
        """Check if we can create an user"""

        client = APIClient()
        response = client.post(
                '/core/UsuarioViewSet/', {
                'password': 'YWRtaW4xMjM=',
                'password_confirmation': 'YWRtaW4xMjM=',
                'username': 'testing1'
            },
            format='multipart'
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(json.loads(response.content), {"username":"testing1"})

    
    def test_login_user(self):

        client = APIClient()
        response = client.post(
                '/core/UserInfoView/', {
                'username': 'testing1',
                'password': 'admin123',
            },
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        result = json.loads(response.content)
        self.assertIn('access_token', result)