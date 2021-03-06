import json

from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from subscription.models import Subscription


class TestSubscription(APITestCase):
    def setUp(self):
        self.client = APIClient()
        User = get_user_model()
        self.password = 'adminadmin'
        self.user = User.objects.create_user(username='user', email='user@gmail.com',
                                             password=self.password, is_upgraded=True)
        self.admin_user = User.objects.create_superuser(username='admin', email='Admin@gmail.com',
                                                        password=self.password, is_upgraded=True)

    def test_valid_subscription_create(self):
        url_create = reverse('subscription_create')
        data = {'title': 'test'}
        data1 = json.dumps(data)
        self.client.force_login(self.admin_user)
        response = self.client.post(url_create, data1, content_type='application/json')
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertEqual(response.data['title'], data['title'])

    def test_invalid_subscription_create(self):
        url_create = reverse('subscription_create')
        data = {'title': 'test'}
        data1 = json.dumps(data)
        response = self.client.post(url_create, data1, content_type='application/json')

        self.assertEqual(status.HTTP_403_FORBIDDEN, response.status_code)

    def test_valid_subscription_list(self):
        url_list = reverse('subscription_list')
        self.client.force_login(self.admin_user)
        response = self.client.get(url_list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.client.force_login(self.user)
        response = self.client.get(url_list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_subscription_list(self):
        url_list = reverse('subscription_list')
        response = self.client.get(url_list)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class TestRelation(APITestCase):
    def setUp(self):
        user = get_user_model()
        self.password = 'adminadmin'
        self.user = user.objects.create_user(username='user', email='user@gmail.com',
                                             password=self.password, is_upgraded=True)
        self.admin_user = user.objects.create_superuser(username='admin', email='Admin@gmail.com',
                                                        password=self.password, is_upgraded=True)
        self.subscription = Subscription.objects.create(title='admin')

    def test_valid_relation_create(self):
        url_create = reverse('relation_create')
        self.client.force_login(self.admin_user)
        data = {
            'user': self.admin_user.id,
            'category': [self.subscription.id],
        }
        data1 = json.dumps(data)
        response = self.client.post(url_create, data1, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['user'], data['user'])
        self.assertEqual(response.data['category'], data['category'])

    def test_invalid_relation_create(self):
        url_create = reverse('relation_create')
        data = {
            'user': self.admin_user.id,
            'category': [self.subscription.id],
        }
        data1 =json.dumps(data)
        response = self.client.post(url_create, data1, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
