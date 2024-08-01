import unittest
from unittest.mock import patch
from game.card import Deck, Card

class TestCard(unittest.TestCase):
    def setUp(self):
        self.deck = Deck()
        
    def test_deck_initialization(self):
        # Check that the deck contains 54 cards (52 + 2 jokers)
        self.assertEqual(len(self.deck.cards), 54)

        # Check the presence of black and red jokers
        black_joker = Card("", "black_joker")
        red_joker = Card("", "red_joker")
        self.assertIn(black_joker, self.deck.cards)
        self.assertIn(red_joker, self.deck.cards)

    @patch('random.shuffle')
    def test_shuffle(self, mock_shuffle):
        self.deck.shuffle()
        mock_shuffle.assert_called_once_with(self.deck.cards)

    def test_deal(self):
        initial_length = len(self.deck.cards)
        dealt_card = self.deck.deal()
        # Check that the dealt card is a Card instance
        self.assertIsInstance(dealt_card, Card)
        # Check that the length of the deck is reduced by one
        self.assertEqual(len(self.deck.cards), initial_length - 1)
