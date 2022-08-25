from rest_framework import status
from rest_framework.test import APITestCase

from users.models import User

class RegistrationTestCase(APITestCase):

    def test_registration(self):
        data = {
        "username":"Test",
        "name": "Test",
        "email": "test@gmail.com",
        "password": "TestPass"
        }
        response = self.client.post("/user/register/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class LoginTestCase(APITestCase):
    
    def test_login(self):
        u = User.objects.create_user(username='Test', email = "test@gmail.com", password = "TestPass")
        u.save()
                
        data = {
        "email": "test@gmail.com",
        "password": "TestPass"
        }

        response = self.client.post("/user/login/", data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class LogoutTestCase(APITestCase):
    
    def test_logout(self):
        response = self.client.post("/user/logout/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

