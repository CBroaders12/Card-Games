from deck_of_cards import Card, Deck, Player

""" Let's play a game of war!
The rules are simple:
- Deal to each player until the deck is gone.
    For each round:
    - Each person plays a card
    - The high card takes all those cards and adds them to the bottom of their hand
    - If two or more people tie then they go to war
        - Each player in the war places three cards face-down
        - They flip a fourth card and the high card wins
        - If still tied they go to war again until there is a winner
- Whoever takes all the cards wins

Card values notes:
- Aces are high
- Deuces beat aces
"""

# Function to play the game takes in the players (just 2 atm) and a deck of cards as input
def war(player1, player2, deck):
    print("Let's play a game of war!")
    print("-------------------------")
    print("Looks like it's %s vs. %s" % (player1.name, player2.name))

    print("Shuffling deck...")
    deck.shuffle()
    
    print("Dealing cards...")
    while deck.cards: # Deal cards until the deck is empty
        player1.draw(deck)
        player2.draw(deck)
    

# Function for if there is a tie takes in 2 players as input
def tie_breaker(player1, player2):
    pass

#Initialize the deck and the players
deck = Deck()

player1 = Player("Joe")
player2 = Player("Bill")

war(player1, player2, deck)