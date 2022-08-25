import datetime, jwt
from http.cookies import SimpleCookie
from rest_framework import status
from rest_framework.test import APITestCase

from users.models import User
from .models import Task

class CreateTaskTestCase(APITestCase):
    
    def test_create_task(self):
        u = User.objects.create_user(username='Test', email = "test@gmail.com", password = "TestPass")
        u.save()
       
        payload = {
        'id': u.id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
        'iat': datetime.datetime.utcnow()
        }
        
        token = jwt.encode(payload, 'secret', algorithm='HS256').decode('utf-8')
        
        self.client.cookies = SimpleCookie({'jwt': token})
        data={"body": "test task 1", "user":u.id}
        response = self.client.post("/create_task/", data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class GetTasksTestCase(APITestCase):

    def test_get_all_tasks(self):
        response = self.client.get("/get_all_tasks/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_filter_get(self):
        response = self.client.get("/get_task/?search=")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    


class UpdateTaskTestCase(APITestCase):
    
    def test_update_task(self):
        u = User.objects.create_user(username='Test2', email = "test2@gmail.com", password = "TestPass")
        u.save()
        task = Task.objects.create(body="tasktest", user = u)
        payload = {
        'id': u.id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
        'iat': datetime.datetime.utcnow()
        }
        token = jwt.encode(payload, 'secret', algorithm='HS256').decode('utf-8')
        data={"body": "test task change", "completed":True}
        self.client.cookies = SimpleCookie({'jwt': token})
        response = self.client.post("/update_task/{}/".format(task.id), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)



class DeleteTask(APITestCase):
        
     def test_get_all_tasks(self):
        u = User.objects.create_user(username='Test2', email = "test2@gmail.com", password = "TestPass")
        u.save()
        payload = {
        'id': u.id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
        'iat': datetime.datetime.utcnow()
        }
        token = jwt.encode(payload, 'secret', algorithm='HS256').decode('utf-8')
        task = Task.objects.create(body="tasktest", user = u)
        self.client.cookies = SimpleCookie({'jwt': token})
        response = self.client.delete("/delete_task/{}/".format(task.id))
        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)