#Inspired by https://medium.com/@anthonytapias/build-a-deck-of-cards-with-oo-python-c41913a744d3

#Import modules
import random

#Define Classes
#Class for individual cards for later use in other classes
class Card:
    def __init__(self, value, suit):
        self.value = value  #value is a string or int to accomodate face cards
        self.suit = suit    #suit is a string

    def __repr__(self):
        return "{value} of {suit}".format(value=self.value, suit=self.suit)

    def show(self):
        print("{value} of {suit}".format(value=self.value,suit=self.suit))

#Class for the deck where the cards are placed
class Deck:
    #Set class variables for suits and values of cards
    suits = ["Spades", "Clubs", "Diamonds", "Hearts"]
    values = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']

    #Initialize the deck as an empty list of cards that is built out automatically
    def __init__(self):
        self.cards = []
        self.build()

    #Builds the deck using the class variables above
    def build(self):
        for suit in self.suits:
            for value in self.values:
                self.cards.append(Card(value, suit))

    #Displays the entire deck
    def show(self):
        for card in self.cards:
            card.show()

    #Randomizes the order of the deck using Fisher Yates shuffle
    def shuffle(self):
        for idx in range(len(self.cards) - 1 , 0, -1):
            rand_idx = random.randint(0, idx)
            self.cards[idx], self.cards[rand_idx] = self.cards[rand_idx], self.cards[idx]

    #Draws a single card from the top of the deck
    def draw_card(self):
        return self.cards.pop(0)

#Class for the player who will play with the cards and deck
class Player:

    #Player has a name and starts with an empty hand
    def __init__(self, name):
        self.name = name
        self.hand = []

    #Draws a card from the top of the deck and adds it to their hand
    def draw(self, deck):
        self.hand.append(deck.draw_card())
        return self

    #Displays the player's hand
    def show_hand(self):
        print("{player}'s hand:".format(player=self.name))
        for card in self.hand:
            card.show()
        print('----------')

    #Deal a full hand of # cards to yourself and another player from the deck
    def deal_hand(self, player, num_cards, deck):
        for i in range(num_cards):
            self.draw(deck)
            player.draw(deck)

    #Plays a card from the player's hand.
    #Defaults to playing the first card in their hand
    def play_card(self, card=None):
        if card:
            if card in self.hand:
                card_idx = self.hand.index(card)
                return self.hand.pop(card_idx)
        return self.hand.pop(0)


deck = Deck()
deck.shuffle()

dealer = Player('Dealer')
conor = Player('Conor')

dealer.deal_hand(conor, 5, deck)

conor.show_hand()
dealer.show_hand()

# card_to_play = input("What card do you want to play? ")
# print(conor.play_card(card_to_play))
