import logging
import re  # Regular Expressions for input validation
from game.card import Deck
from game.player import Player, House
from user.models import Profile

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
    def __init__(self, bet_point):
        self.deck = Deck()
        self.player = None
        self.house = House()
        self.current_reward = 0
        self.bet_point = bet_point

    # Validate user input using regular expressions
    @log_method_call
    def validate_input():
        isVailid = False
        while not isVailid:
            try:
                guess = input("Guess if your card is greater or less than the house's card (greater/less): ").strip().lower()
                if not re.match("^(greater|less)$", guess):
                    logging.error("Invalid input! Please enter 'greater' or 'less'.")
                    raise ValueError("Invalid input! Please enter 'greater' or 'less'.")
                else:
                    isVailid = True
            except ValueError as e:
                print(e)
        return guess
    
    @log_method_call
    def auto_create_card(self):
        if self.player.points > self.bet_point:
            self.house.receive_card(self.deck.deal())
            logging.info(f"House card: {self.house.card}")

            self.player.card = self.deck.deal()
            logging.info(f"Player card: {self.player.card}")

    # Play a round of the game
    @log_method_call
    def play_round(self,guess):
        result = ''
        if self.player.points < self.bet_point:
            logging.info("Player does not have enough points to continue.")
            result = "Player does not have enough points to continue."
            return result
          
        if self.player.make_guess(self.house.card, guess):
            self.current_reward += self.bet_point + (self.bet_point * 0.1)
            logging.info(f"Correct guess! Current reward: {self.current_reward} points.")
            result = "Correct"
        else:
            self.current_reward = 0
            logging.info("Wrong guess. You lose the current round's reward.")
            result = "Wrong"

        if self.current_reward >= 1000:
            logging.info("Congratulations! You win the game.")
            result = "Win"
        elif self.player.points < 30:
            logging.info("You do not have enough points. Game over.")
            result = "Game over"
        return result

    @log_method_call
    def start_game(self):
        while self.player.points >= 30 and self.player.points < 1000:
            self.play_round()
            continue_game = input("Do you want to continue to the next round? (yes/no): ").strip().lower()
            if continue_game not in ("yes", "y"):
                self.player.update_points(self.current_reward)
                self.current_reward = 0
                logging.info(f"Player's total points: {self.player.points}")
                break