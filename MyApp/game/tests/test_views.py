from unittest.mock import patch
from django.test.utils import setup_test_environment, teardown_test_environment
import os
import django

from game.card import Card
os.environ['DJANGO_SETTINGS_MODULE'] = 'MyApp.settings'
django.setup()

import json
from django.test import TestCase
from django.contrib.auth.models import User
from user.models import Profile
from game.player import Player
from game.game import Game
import uuid
from django.urls import reverse

class GameViewsTestCase(TestCase):
    
    @classmethod
    def setUpClass(cls):
        setup_test_environment()
    
    @classmethod
    def tearDownClass(cls):
        teardown_test_environment()
        
    def setUp(self):
        self.user = User.objects.create_user(username=f'testuser_{uuid.uuid4().hex}', password='12345')
        self.client.login(username=self.user.username, password='12345')
        self.profile = Profile.objects.create(user=self.user, point=1000)
        self.player = Player(name=self.user.username, point=self.profile.point, user=self.user)
        self.game = Game(bet_point=100, player=self.player)
        
    def tearDown(self):
        self.user.delete() 
        self.profile.delete()
        

    # def test_start_game_redirect_if_not_logged_in(self):
    #     self.start_game_url = reverse('/play/start/')
    #     response = self.client.get(self.start_game_url)
    #     self.assertRedirects(response, f'{reverse("user:login")}?next={self.start_game_url}')
    
    def test_start_game_post(self):
        response = self.client.post('/play/start/', {'choice_bet_point': 100})
        
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'game/easy.html')
        
        context = response.context
        self.assertIn('player_card', context)
        self.assertIn('house_card', context)
        self.assertIn('reward_point', context)
    
    def test_start_game_get(self):
        response = self.client.get('/play/start/')
        
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/dashboard.html')
        
    # def test_play_round_redirect_if_not_logged_in(self):
    #     self.play_round_url = reverse('/play/round/')
    #     response = self.client.get(self.play_round_url)
    #     self.assertRedirects(response, f'{reverse("user:login")}?next={self.play_round_url}')
        
    def test_play_round_get(self):
        self.client.post('/play/start/', {'choice_bet_point': 100})

        response = self.client.get('/play/round/')
        
        self.assertEqual(response.status_code, 400)
        json_response = json.loads(response.content)
        self.assertEqual(json_response['error'], 'Invalid request')


    def test_play_round_post_correct_guess(self):
        # Start a game first
        self.client.post('/play/start/', {'choice_bet_point': 100})
        
        response = self.client.post('/play/round/', {
            'guess': 'greater',
            'action': 'continue',
        }, HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.content)
        self.assertIn('player_card', json_response)
        self.assertIn('house_card', json_response)
        self.assertIn('player_points', json_response)
        self.assertIn('reward_point', json_response)
        self.assertIn('result', json_response)

    @patch('game.player.Player.make_guess')
    def test_play_round_game_over_action(self, mock_make_gues):
        mock_make_gues.return_value = False
        self.client.post('/play/start/', {'choice_bet_point': 1000})
        
        response = self.client.post('/play/round/', {
            'guess': 'greater',
            'action': 'Stop',
        }, HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.content)
        self.assertEqual(json_response['result'], 'Game over')
        
    def mocked_auto_create_card(self):
        # Manually set the house and player cards in the mock
        self.game.house.receive_card(Card('spade', '3'))
        self.game.player.card = Card('spade', '5')

    def test_play_round_continue_action(self):
        # Start a game first
        self.client.post('/play/start/', {'choice_bet_point': 100})

        response = self.client.post('/play/round/', {
            'guess': 'greater',
            'action': 'Continue',
        }, HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.content)
        self.assertIn('player_card', json_response)
        self.assertIn('house_card', json_response)
        self.assertIn('player_points', json_response)
        self.assertIn('reward_point', json_response)
