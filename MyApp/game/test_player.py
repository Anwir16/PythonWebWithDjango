import unittest
from unittest.mock import patch
import django
from django.conf import settings
from django.test.utils import setup_test_environment, teardown_test_environment
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'MyApp.settings'
django.setup()

from django.contrib.auth.models import User
from user.models import Profile
from game.player import Player
import uuid

class TestPlayer(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        setup_test_environment()
    
    @classmethod
    def tearDownClass(cls):
        teardown_test_environment()
        
    def setUp(self):
        self.user = User.objects.create_user(username=f'testuser_{uuid.uuid4().hex}', password='12345')
        self.profile = Profile.objects.create(user=self.user, point=1000)
        self.player = Player(name=self.user.username, point=self.profile.point, user=self.user)
        
    def tearDown(self):
        self.user.delete()
        if self.profile.pk:  
            self.profile.delete()
        
    def test_update_points(self):
        self.player.update_points(50)
        self.profile.refresh_from_db()
        self.assertEqual(self.profile.point, 1050)
        self.assertEqual(self.player.points, 1050)
        
    def test_update_points_profile_not_found(self):
        self.profile.delete()  # Delete the profile to trigger the exception
        with patch('builtins.print') as mock_print:
            self.player.update_points(50)
            mock_print.assert_called_once_with(f"Profile for username {self.user.username} does not exist.")

        
    def test_make_guess_correct(self):
        self.player.card = 5
        house_card = 3
        result = self.player.make_guess(house_card, "greater")
        self.assertTrue(result)

    def test_make_guess_incorrect(self):
        self.player.card = 2
        house_card = 3
        result = self.player.make_guess(house_card, "less")
        self.assertTrue(result)

    def test_make_guess_wrong_guess(self):
        self.player.card = 3
        house_card = 5
        result = self.player.make_guess(house_card, "greater")
        self.assertFalse(result)
    
if __name__ == '__main__':
    unittest.main()
