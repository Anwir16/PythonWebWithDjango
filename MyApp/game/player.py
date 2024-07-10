from django.contrib.auth.models import User
class Player:
    def __init__(self, name, point):
        self.name = name
        self._points = point
        self.card = None
    
    @property
    def points(self):
        return self._points
    @points.setter
    def points(self, value):
        self._points = value

    def make_guess(self, house_card, guess):
        return (guess == "greater" and self.card > house_card) or (
            guess == "less" and self.card < house_card
        )

    def update_points(self, amount):
        self.points += amount


class House:
    def __init__(self):
        self.card = None

    def receive_card(self, card):
        self.card = card
