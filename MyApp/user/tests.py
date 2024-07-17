from django.test import TestCase
from django.test.utils import setup_test_environment, teardown_test_environment
import os
import django
import uuid
from django.urls import reverse
os.environ['DJANGO_SETTINGS_MODULE'] = 'MyApp.settings'
django.setup()

import json
from django.contrib.auth.models import User
from user.models import Profile



class TestUser(TestCase):
    
    @classmethod
    def setUpClass(cls):
        setup_test_environment()
    
    @classmethod
    def tearDownClass(cls):
        teardown_test_environment()
    
    def setUp(self):
        self.user = User.objects.create_user(username=f'testuser_{uuid.uuid4().hex}', password='12345')
        self.profile = Profile.objects.create(user=self.user, point=1000)
    
    def tearDown(self):
        self.user.delete() 
        self.profile.delete()

    def test_signup_view(self):
        response = self.client.post(reverse('user:signup'), {
            'username': 'newuser',
            'password1': 'testpass',
            'password2': 'testpass'
        })
        self.assertEqual(response.status_code, 302)  # Redirect after signup
        self.assertTrue(User.objects.filter(username='newuser').exists())

    def test_login_view(self):
        response = self.client.post(reverse('user:login'), {
            'username': 'testuser',
            'password': '12345'
        })
        self.assertEqual(response.status_code, 302)  # Redirect after login
        self.assertEqual(str(response.wsgi_request.user), 'testuser')

    def test_logout_view(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.get(reverse('user:logout'))
        self.assertEqual(response.status_code, 302)  # Redirect after logout
        self.assertEqual(str(response.wsgi_request.user), 'AnonymousUser')

    def test_views_profile_view(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.get(reverse('user:profile'))
        self.assertEqual(response.status_code, 200)  # Should return a valid response
        self.assertTemplateUsed(response, 'user/profile.html')

    def test_update_profile_view(self):
        self.client.login(username=self.user.username, password='12345')
        response = self.client.post(reverse('user:updateProfile'), {
            'username': self.user.username,
            'email': 'updated@example.com'
        })
        self.user.refresh_from_db()
        self.assertEqual(self.user.email, 'updated@example.com')
        self.assertEqual(response.status_code, 302)  # Redirect after update

    def test_check_username_ajax_get(self):
        response = self.client.get(reverse('user:validate_username'), {'username': 'testuser'}, HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertEqual(response.json(), {'valid': False})

        response = self.client.get(reverse('user:validate_username'), {'username': 'newuser'}, HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertEqual(response.json(), {'valid': True})
        
    def test_check_username_ajax_post(self):
        response = self.client.post(reverse('user:validate_username'), {'username': 'testuser'}, HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertEqual(response.json(), {})
