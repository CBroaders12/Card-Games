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
card_values = {'Ace': 14, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'Jack': 11, 'Queen': 12, 'King': 13}

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
    
    print("Let the game begin!")
    
    round = 0

    while player1.hand and player2.hand:
        round += 1
        print("**********")
        print("Round {}!".format(round))
        print("-----------")
        cards_played = []
        player1_card = player1.play_card()
        player2_card = player2.play_card()
        cards_played += [player1_card, player2_card]

        print("%s plays the %s" % (player1.name, player1_card))
        print("%s plays the %s" % (player2.name, player2_card))

        if card_values[player1_card.value] > card_values[player2_card.value]:
            print("-----------------")
            print("%s takes the hand" % (player1.name))
            print("-----------------")
            player1.hand += cards_played
        
        elif card_values[player1_card.value] < card_values[player2_card.value]:
            print("-----------------")
            print("%s takes the hand" % (player2.name))
            print("-----------------")
            player2.hand += cards_played
        
        else:
            tie_breaker(player1, player2)
        
        print("{} has {} cards".format(player1.name, len(player1.hand)))
        print("{} has {} cards".format(player2.name, len(player2.hand)))
        print("*******************\n")
    

# Function for if there is a tie takes in 2 players as input
def tie_breaker(player1, player2):
    print("Tie breaker time!")
    print("----------------")
    
    cards_played = []

    for x in range(3):
        cards_played.append(player1.play_card())
        cards_played.append(player2.play_card())
    
    player1_card = player1.play_card()
    player2_card = player2.play_card()
    cards_played += [player1_card, player2_card]


#Initialize the deck and the players
deck = Deck()

player1 = Player("Joe")
player2 = Player("Bill")

war(player1, player2, deck)