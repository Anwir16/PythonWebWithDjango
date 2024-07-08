import random


class Suit:
    suit = {
        "Heart": 4,
        "Diamond": 3,
        "Club": 2,
        "Spade": 1    
    }
    
class Rank:
    rank = {
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "10": 10,
        "J": 11,
        "Q": 12,
        "K": 13,
        "A": 14,
        "2": 15,
        "Black Joker": 16,
        "Red Joker": 17
    }


class Card:
    def __init__(self, suit, rank):
        self._suit = suit
        self._rank = rank
        
    @property
    def suit(self):
        return self._suit

    # Property for rank to manage access
    @property
    def rank(self):
        return self._rank

    def __str__(self):
        if self.rank in ("Black Joker", "Red Joker"):
            return f"{self.rank}"
        return f"{self.rank} of {self.suit}"

    def __lt__(self, other):
        if Rank.rank[self.rank] == Rank.rank[other.rank]:
            return Suit.suit[self.suit] < Suit.suit[other.suit]
        return Rank.rank[self.rank] < Rank.rank[other.rank]

    def __gt__(self, other):
        if Rank.rank[self.rank] == Rank.rank[other.rank]:
            return Suit.suit[self.suit] > Suit.suit[other.suit]
        return Rank.rank[self.rank] > Rank.rank[other.rank]

class Deck:
    def __init__(self):
        self.cards = [
            Card(suit, rank)
            for suit in Suit.suit.keys()
            for rank in Rank.rank.keys()
            if rank not in ("Black Joker", "Red Joker")
        ] + [Card("", "Black Joker"), Card("", "Red Joker")]
        self.shuffle()

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop()
