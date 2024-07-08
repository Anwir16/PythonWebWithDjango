import logging
import re  # Regular Expressions for input validation
from card import Deck
from player import Player, House

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
    def __init__(self):
        self.deck = Deck()
        self.player = Player("Player")
        self.house = House()
        self.current_reward = 0

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

    # Play a round of the game
    @log_method_call
    def play_round(self):
        if self.player.points < 25:
            logging.info("Player does not have enough points to continue.")
            return

        self.player.update_points(-25)
        self.house.receive_card(self.deck.deal())
        logging.info(f"House card: {self.house.card}")

        self.player.card = self.deck.deal()
        logging.info(f"Player card: {self.player.card}")

        guess = Game.validate_input()
        if self.player.make_guess(self.house.card, guess):
            self.current_reward += 20
            self.player.update_points(25)
            logging.info(f"Correct guess! Current reward: {self.current_reward} points.")
        else:
            self.current_reward = 0
            logging.info("Wrong guess. You lose the current round's reward.")

        if self.player.points >= 1000:
            logging.info("Congratulations! You win the game.")
        elif self.player.points < 30:
            logging.info("You do not have enough points. Game over.")

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