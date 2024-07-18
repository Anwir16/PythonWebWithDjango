from django.test import Client, TestCase
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
from user.forms import UserUpdateForm, UpdateProfileForm



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

    def test_signup_view_success(self):
        response = self.client.post(reverse('user:register'), {
            'username': 'newuser',
            'password1': 'testpass123',  # Ensure password meets all requirements
            'password2': 'testpass123'
        })
        self.assertTrue(User.objects.filter(username='newuser').exists())
        self.assertRedirects(response,'/')
        self.assertEqual(str(response.wsgi_request.user), 'newuser')
        
        
    def test_signup_view_fail_post(self):
        response = self.client.post(reverse('user:register'), {
            'username': 'newuser',
            'password1': 'testpass',  # Ensure password meets all requirements
            'password2': 'testpass'
        })
        self.assertTemplateUsed(response, 'user/signup.html')
        self.assertFalse(User.objects.filter(username='newuser').exists())
        
    def test_signup_view_get(self):
        response = self.client.get(reverse('user:register'))
        self.assertTemplateUsed(response, 'user/signup.html')

        
    def test_signup_view_is_authenticated(self):
        self.client.login(username=self.user.username, password='12345')
        response = self.client.get(reverse('user:register'))
        self.assertRedirects(response,'/')

    def test_login_view(self):
        response = self.client.post(reverse('user:login'), {
            'username': self.user.username,
            'password': '12345'
        })
        self.assertEqual(response.status_code, 302)  # Redirect after login
        self.assertRedirects(response,'/')
        self.assertEqual(str(response.wsgi_request.user), self.user.username)
        
    def test_login_view_post_fail(self):
        response = self.client.post(reverse('user:login'), {
            'username': 'newuser',
            'password': '12345'
        })
        self.assertTemplateUsed(response, 'user/login.html')
        self.assertIn('error', response.context)
        self.assertEqual(response.context['error'], 'Invalid username or password')
        
    def test_login_view_is_authenticated(self):
        self.client.login(username=self.user.username, password='12345')
        response = self.client.get(reverse('user:login'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response,'/')
        
    def test_login_view_get(self):
        response = self.client.get(reverse('user:login'))
        self.assertTemplateUsed(response, 'user/login.html')
        self.assertEqual(response.status_code, 200)

    def test_logout_view(self):
        self.client.login(username=self.user.username, password='12345')
        response = self.client.get(reverse('user:signout'))
        self.assertEqual(response.status_code, 302)  # Redirect after logout
        self.assertRedirects(response, '/user/login/')
        self.assertEqual(str(response.wsgi_request.user), 'AnonymousUser')
        
    def test_views_profile_redirect_if_not_logged_in(self):
        self.views_profile_url = reverse('user:profile')
        response = self.client.get(self.views_profile_url)
        self.assertRedirects(response, f'{reverse("user:login")}?next={self.views_profile_url}')

    def test_views_profile_view_is_user(self):
        self.client.login(username=self.user.username, password='12345')
        response = self.client.get(reverse('user:profile'))
        self.assertEqual(response.status_code, 200)  # Should return a valid response
        self.assertTemplateUsed(response, 'user/profile.html')
        self.assertTrue(response.context['user'].is_authenticated)
        self.assertFalse(response.context['user'].is_superuser)
        
    def test_views_profile_view_is_superuser(self):
        self.superuser = User.objects.create_superuser(username=f'admin_{uuid.uuid4().hex}', email='admin@example.com', password='adminpass123')
        self.client.login(username=self.superuser.username, password='adminpass123')
        response = self.client.get(reverse('user:profile'))
        self.assertEqual(response.status_code, 302)  # Should return a valid response
        self.assertRedirects(response, '/admin/')
        response = self.client.get(response.url)

        # Check authentication status
        self.assertTrue(response.wsgi_request.user.is_authenticated)
        self.assertTrue(response.wsgi_request.user.is_superuser)
        
    def test_update_profile_redirect_if_not_logged_in(self):
        self.update_profile_url = reverse('user:updateProfile')
        response = self.client.get(self.update_profile_url)
        self.assertRedirects(response, f'{reverse("user:login")}?next={self.update_profile_url}')

    def test_update_profile_view_success(self):
        self.client.login(username=self.user.username, password='12345')
        response = self.client.post(reverse('user:updateProfile'), {
            'username': self.user.username,
            'email': 'updated@example.com',
            'first_name' : 'Phuc',
            'last_name' : 'Nguyen',
            'image' : 'default.png',
            'gender' : 'Male',
            'birthday' : '06/01/2003',
            
        })
        self.user.refresh_from_db()
        self.profile.refresh_from_db()
        self.assertEqual(self.user.email, 'updated@example.com')
        self.assertEqual(response.status_code, 302)  
        self.assertRedirects(response, '/user/profile/')
        
    def test_update_profile_get(self):
        self.client.login(username=self.user.username, password='12345')
        response = self.client.get(reverse('user:updateProfile'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user/updateProfile.html')
        self.assertIsInstance(response.context['u_form'], UserUpdateForm)
        self.assertIsInstance(response.context['p_form'], UpdateProfileForm)
        
    def test_update_profile_view_fail(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.post(reverse('user:updateProfile'), {
            'username': '',
            'email': '',
            'first_name' : '',
            'last_name' : '',
            'image' : '',
            'gender' : '',
            'birthday' : '',
            
        })
        self.user.refresh_from_db()
        self.profile.refresh_from_db()
        self.assertEqual(response.status_code, 302)  
        self.assertTemplateUsed(response, 'user/updateProfile.html')
        self.assertTrue(response.context['u_form'].errors)
        self.assertTrue(response.context['p_form'].errors)


    def test_check_username_ajax_get(self):
        response = self.client.get(reverse('user:validate_username'), {'username': self.user.username}, HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertEqual(response.json(), {'valid': False})

        response = self.client.get(reverse('user:validate_username'), {'username': 'newuser'}, HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertEqual(response.json(), {'valid': True})
        
    def test_check_username_ajax_post(self):
        response = self.client.post(reverse('user:validate_username'), {'username': self.user.username}, HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertEqual(response.json(), {})
