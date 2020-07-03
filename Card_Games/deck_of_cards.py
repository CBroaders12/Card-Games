import random

class Card:
    def __init__(self, value, suit=None):
        self.value = value
        self.suit = suit
    
    def __repr__(self):
        return "%s of %s" % (str(self.value), self.suit)
    
    def show(self):
        print("{value} of {suit}".format(value=self.value,suit=self.suit))

class Deck:
    suits = ["Spades", "Clubs", "Diamonds", "Hearts"]
    values = {'Ace': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'Jack': 11, 'Queen': 12, 'King': 13}

    def __init__(self):
        self.cards = []
        self.build()
    
    def build(self):
        for suit in self.suits:
            for value in self.values.values():
                self.cards.append(Card(value, suit))
    
    def show(self):
        for card in self.cards:
            card.show()
    
    def shuffle(self):
        for idx in range(len(self.cards) - 1 , 0, -1):
            rand_idx = random.randint(0, idx)
            self.cards[idx], self.cards[rand_idx] = self.cards[rand_idx], self.cards[idx]

class Player:

    def __init__(self):
        pass



# values = {1: "Ace", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine", 10: "Ten", 11: "Jack", 12: "Queen", 13: "King"}
# rev_values = {v: k for k, v in values.items()}

deck = Deck()
deck.shuffle()
deck.show()