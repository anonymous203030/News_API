import json

from django.contrib.auth import get_user_model
from django.test import TestCase
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase, APIClient
from posts.models import Category

class TestPosting(APITestCase):
    def setUp(self):
        self.category = Category.objects.create(title='Market')
        user = get_user_model()
        self.user = user.objects.create_user(username='user', password='rootroot', email='user@gmail.com', is_upgraded=True)
        self.no_upgraded_user = user.objects.create_user(username='no_upgraded_user', password='rootroot', email='user1@gmail.com', is_upgraded=False)
        self.admin_user = user.objects.create_superuser(username='admin', password='rootroot', email='admin@gmail.com', is_upgraded=True)
        self.client = APIClient()

    def test_post_valid_create(self):
        url_created = reverse('post_create')
        self.client.force_login(self.admin_user)
        data = {
            'categories': [self.category.id],
            'title': 'test',
            'content': 'test',
            'user': self.admin_user.id,
        }
        data1 = json.dumps(data)
        response = self.client.post(url_created, data1, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(data['categories'], response.data['categories'])
        self.assertEqual(data['title'], response.data['title'])
        self.assertEqual(data['content'], response.data['content'])
        self.assertEqual(data['user'], response.data['user'])

    def test_post_invalid_create(self):
        url_created = reverse('post_create')
        data = {
            'categories': [self.category.id],
            'title': 'test',
            'content': 'test',
            'user': self.admin_user.id,
        }
        data1 = json.dumps(data)
        response = self.client.post(url_created, data1, content_type='application/json')
        self.assertEqual(status.HTTP_403_FORBIDDEN, response.status_code)
        self.client.force_login(self.admin_user)
        data = {
            'categories': [self.category.id],
            'title': 'test',
            'user': self.admin_user.id,
        }
        data1 = json.dumps(data)
        response = self.client.post(url_created, data1, content_type='application/json')
        self.assertEqual(status.HTTP_400_BAD_REQUEST, response.status_code)

    def  test_valid_post_list(self):
        any_list = reverse('any_list')
        logged_list = reverse('logged_list')
        upgraded_list = reverse('upgraded_list')

        response = self.client.get(any_list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.client.force_login(self.user)
        response = self.client.get(upgraded_list)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.client.force_login(self.no_upgraded_user)
        response = self.client.get(logged_list)
        self.assertEqual(status.HTTP_200_OK, response.status_code)

    def test_invalid_post_list(self):
        logged_list = reverse('logged_list')
        upgraded_list = reverse('upgraded_list')

        response = self.client.get(path=upgraded_list, data=None)
        self.assertEqual(status.HTTP_403_FORBIDDEN, response.status_code)
        self.client.logout()
        response = self.client.get(logged_list)
        self.assertEqual(status.HTTP_403_FORBIDDEN, response.status_code)
