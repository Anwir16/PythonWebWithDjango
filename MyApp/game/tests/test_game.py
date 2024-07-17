import unittest
from unittest.mock import patch
import django
from django.conf import settings
from django.test.utils import setup_test_environment, teardown_test_environment

# Set the environment variable for Django settings module
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'MyApp.settings'  

# Initialize Django
django.setup()

from game.player import Player
from game.game import Game
from game.card import Card
from django.contrib.auth.models import User
from user.models import Profile

class TestGame(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        setup_test_environment()
    
    @classmethod
    def tearDownClass(cls):
        teardown_test_environment()
        
    def setUp(self):
        self.user = User.objects.create_user(username=f'testuser_{self.id()}', password='12345')
        self.profile = Profile.objects.create(user=self.user, point=1000)
        self.player = Player(name=self.user.username, point=self.profile.point, user=self.user)
        self.game = Game(bet_point=100, player=self.player)
        
    def tearDown(self):
        self.user.delete()
        self.profile.delete()
        
    def test_auto_create_card(self):
        self.game.auto_create_card()
        self.assertIsNotNone(self.game.player.card)
        self.assertIsNotNone(self.game.house.card)
        
    @patch('random.shuffle')
    def test_shuffle(self, mock_shuffle):
        self.game.deck.shuffle()
        mock_shuffle.assert_called_once_with(self.game.deck.cards)
        
    def test_guess_wrong(self):
        self.game.player.card = Card('hearts', '4')
        self.game.house.card = Card('hearts', '5')
        result = self.game.play_round('greater')
        self.assertEqual(result, 'Wrong')
        
    def test_guess_correct(self):
        self.game.player.card = Card('hearts', '10')
        self.game.house.card = Card('hearts', '5')
        result = self.game.play_round('greater')
        self.assertEqual(result, 'Correct')
        
    def test_play_round_wrong_not_enough_points(self):
        self.player.update_points(-900)
        self.game.player.card = Card('hearts', '10')
        self.game.house.card = Card('hearts', '5')
        result = self.game.play_round('less')
        self.assertLess(self.player.points, self.game.bet_point)
        self.assertEqual(result, 'Game over')

    def test_play_round_not_enough_points(self):
        self.player.update_points(-950)  # Player's points drop below the bet point
        self.assertLess(self.player.points, self.game.bet_point)  # Check points are less than bet point
        # Try to play the round
        result = self.game.play_round('greater')  
        self.assertEqual(result, 'Game over')  # Expect "Game over" result

    def test_play_round_game_win(self):
        self.game.current_reward = 950
        self.game.player.card = Card('hearts', '10')
        self.game.house.card = Card('hearts', '5')
        result = self.game.play_round('greater')
        self.assertEqual(result, 'Win')
        self.assertEqual(self.game.player.points, 2060.0)
        
if __name__ == '__main__':
    unittest.main()
    
