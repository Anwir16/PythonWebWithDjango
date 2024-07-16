from user.models import Profile

class Player:
    def __init__(self, name, point, user):
        self._name = name
        self._points = point
        self.card = None
        self.user = user
    
    @property
    def points(self):
        return self._points

    @points.setter
    def points(self, value):
        self._points = value
        
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    def make_guess(self, house_card, guess):
        return (guess == "greater" and self.card > house_card) or (
            guess == "less" and self.card < house_card
        )

    def update_points(self, amount):
        try:
            profile = Profile.objects.get(user=self.user)
            profile.point += amount
            profile.save()
            self.points += amount
        except Profile.DoesNotExist:
            # Handle the case where the profile does not exist
            print(f"Profile for username {self.name} does not exist.")


class House:
    def __init__(self):
        self.card = None

    def receive_card(self, card):
        self.card = card
