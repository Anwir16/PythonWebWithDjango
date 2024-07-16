import logging
import re  # Regular Expressions for input validation
from game.card import Deck
from game.player import House

logging.basicConfig(level=logging.INFO)


# Decorator for logging method calls
def log_method_call(func):
    def wrapper(*args, **kwargs):
        logging.info(f"Calling method: {func.__name__}")
        result = func(*args, **kwargs)
        logging.info(f"Method {func.__name__} finished")
        return result

    return wrapper


class Game:
    def __init__(self, bet_point, player):
        self.deck = Deck()
        self.player = player
        self.house = House()
        self.current_reward = 0
        self.bet_point = bet_point

    @log_method_call
    def auto_create_card(self):
        if self.player.points >= self.bet_point:
            self.house.receive_card(self.deck.deal())
            logging.info(f"House card: {self.house.card}")

            self.player.card = self.deck.deal()
            logging.info(f"Player card: {self.player.card}")
        else:
            self.house.receive_card("back_card")
            self.player.card = "back_card"

    # Play a round of the game
    @log_method_call
    def play_round(self, guess):
        result = ""
        if self.player.points < self.bet_point:
            logging.info("Player does not have enough points to continue.")
            result = "Game over"
            return result
        elif self.player.make_guess(self.house.card, guess):
            self.current_reward += self.bet_point + (self.bet_point * 0.1)
            logging.info(
                f"Correct guess! Current reward: {self.current_reward} points."
            )
            result = "Correct"
        else:
            self.current_reward = 0
            logging.info("Wrong guess. You lose the current round's reward.")
            self.player.update_points(-self.bet_point)
            if self.player.points < self.bet_point:
                result = "Game over"
                return result
            result = "Wrong"

        if self.current_reward >= 1000:
            logging.info("Congratulations! You win the game.")
            self.player.update_points(self.current_reward)
            result = "Win"
        return result
