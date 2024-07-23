from unittest.mock import patch
from django.test import TestCase
from django.test.utils import setup_test_environment, teardown_test_environment
import os
import django
import uuid
from django.urls import reverse


os.environ['DJANGO_SETTINGS_MODULE'] = 'MyApp.settings'
django.setup()

from django.contrib.auth.models import User
from user.models import Profile
from wallet.models import ComboPoint, PaymentHistory

class TestWallet(TestCase):
    @classmethod
    def setUpClass(cls):
        setup_test_environment()
    
    @classmethod
    def tearDownClass(cls):
        teardown_test_environment()
    
    def setUp(self):
        self.user = User.objects.create_user(username=f'testuser_{uuid.uuid4().hex}', password='12345')
        self.profile = Profile.objects.create(user=self.user, point=1000)
        self.combo_point = ComboPoint.objects.create(name='Test Combo', point=100, price=1000)
        self.payment_data = {
            'order_id': '123456',
            'amount': 1000,
            'order_desc': 'Test Order',
            'language': 'vn',
            'point': self.combo_point.point,
            'combo_point': self.combo_point.id,
        }
    
    def tearDown(self):
        self.user.delete()
        self.profile.delete()
        self.combo_point.delete()
    
    def test_view_payment_redirect_if_not_logged_in(self):
        self.view_buy_point_url = reverse('wallet:buy_point')
        response = self.client.get(self.view_buy_point_url)
        self.assertRedirects(response, f'{reverse("user:login")}?next={self.view_buy_point_url}')
        
    def test_view_payment_get(self):
        self.client.login(username=self.user.username, password='12345')
        response = self.client.get(reverse('wallet:buy_point'))
        self.assertTemplateUsed(response, 'wallet/buy_point.html')
        self.assertIn('combo_point', response.context)
        
    @patch('wallet.vnpay.vnpay.get_payment_url', return_value='https://sandbox.vnpayment.vn/paymentv2/vpcpay.html')
    def test_payment_post(self, mock_get_payment_url):
        self.client.login(username=self.user.username, password='12345')
        # Simulate POST request to create payment and store session data
        response = self.client.post(reverse('wallet:buy_point'), self.payment_data)
        
        # Check if the response is a redirect to the payment URL
        self.assertRedirects(response, 'https://sandbox.vnpayment.vn/paymentv2/vpcpay.html',  fetch_redirect_response=False)
        
        # Check if the session contains the correct values
        session = self.client.session
        self.assertEqual(session['point'], self.payment_data['point'])
        self.assertEqual(session['_order_id'], self.payment_data['order_id'])
        self.assertEqual(session['_amount'], self.payment_data['amount'])
        self.assertEqual(session['_order_desc'], self.payment_data['order_desc'])
        self.assertEqual(session['combo_point_id'], self.payment_data['combo_point'])
    
    def test_payment_get_return_code_00(self):
        self.client.login(username=self.user.username, password='12345')
        # Simulate POST request to store session data
        self.client.post(reverse('wallet:buy_point'), self.payment_data)
        
        # Simulate GET request with return_code '00'
        response = self.client.get(reverse('wallet:buy_point'), {'vnp_ResponseCode': '00'})
        
        # Check if the profile points are updated
        self.profile.refresh_from_db()
        self.assertEqual(self.profile.point, self.combo_point.point + 1000)
        
        # Check if the payment history is created
        payment_history = PaymentHistory.objects.get(user=self.user)
        self.assertEqual(payment_history.combo_point, self.combo_point)
        self.assertEqual(payment_history.order_id, self.payment_data['order_id'])
        self.assertEqual(payment_history.amount, self.payment_data['amount'])
        self.assertEqual(payment_history.order_desc, self.payment_data['order_desc'])
        self.assertEqual(payment_history.user, self.user)
        
        # Check if the session variables are cleared
        session = self.client.session
        self.assertIsNone(session.get('point'))
        self.assertIsNone(session.get('_order_id'))
        self.assertIsNone(session.get('_amount'))
        self.assertIsNone(session.get('_order_desc'))
        self.assertIsNone(session.get('combo_point_id'))
        
        # Check if the correct template is used and combo_point is in context
        self.assertTemplateUsed(response, 'wallet/buy_point.html')
        self.assertIn('combo_point', response.context)
    
    def test_view_payment_history_redirect_if_not_logged_in(self):
        self.view_payment_url = reverse('wallet:payment_history')
        response = self.client.get(self.view_payment_url)
        self.assertRedirects(response, f'{reverse("user:login")}?next={self.view_payment_url}')