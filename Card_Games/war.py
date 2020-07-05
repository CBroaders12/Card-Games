from deck_of_cards import Card, Deck, Player
from statistics import mean

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
    # print("Let's play a game of war!")
    # print("-------------------------")
    # print("Looks like it's %s vs. %s" % (player1.name, player2.name))

    # print("Shuffling deck...")
    deck.shuffle()
    
    #print("Dealing cards...")
    while deck.cards: # Deal cards until the deck is empty
        player1.draw(deck)
        player2.draw(deck)
    
    # print("Let the game begin!")
    
    round = 0
    
    while player1.hand and player2.hand: #While there are still cards in the deck
        round += 1  #Increment round counter
        # print("**********")
        # print("Round {}!".format(round))
        # print("-----------")
        
        cards_played = []
        play_hand(player1, player2, cards_played)
        
        #Check how many cards each player has
        # print("{} has {} cards".format(player1.name, len(player1.hand)))
        # print("{} has {} cards".format(player2.name, len(player2.hand)))
        # print("*******************\n")

        #Timeout the game if it reaches 10000 rounds and return no winner.
        if round >= 10000:
            #print("This is taking ages! Let's call it a draw")
            return None, None

    if player1.hand:
        winner = player1.name
    
    else:
        winner = player2.name
    
    #print("** {} wins after {} rounds! **".format(winner, round))
    return round, winner

# Function for if there is a tie takes in 2 players as input
def tie_breaker(player1, player2, cards_played=None):
    # print("Tie breaker time!")
    # print("----------------")
    
    if not cards_played:
        cards_played = []
    
    if len(player1.hand) == 0 or len(player2.hand) == 0:
        return

    elif len(player1.hand) == 1 or len(player2.hand) == 1:
        pass

    elif len(player1.hand) < 4:
        for x in range(len(player1.hand) - 1):
            cards_played.append(player1.play_card())
    
    elif len(player2.hand) < 4:
        for x in range(len(player2.hand) - 1):
            cards_played.append(player2.play_card())

    else:
        for x in range(3):
            cards_played.append(player1.play_card())
            cards_played.append(player2.play_card())
        
    play_hand(player1, player2, cards_played)

    return

def play_hand(player1, player2, cards_played):
    player1_card = player1.play_card()
    player2_card = player2.play_card()
    cards_played += [player1_card, player2_card] #Cards placed on the table

    player_card_values = [player1_card.value, player2_card.value]

    # print("%s plays the %s" % (player1.name, player1_card))
    # print("%s plays the %s" % (player2.name, player2_card))

    #Hard code deuces beat aces rule
    if "Ace" in player_card_values and "2" in player_card_values:
        if player1_card.value == "2":
            # print("-----------------")
            # print("%s takes the hand" % (player1.name))
            # print("-----------------")
            player1.hand.extend(cards_played)
        
        if player2_card.value == "2":
            # print("-----------------")
            # print("%s takes the hand" % (player2.name))
            # print("-----------------")
            player2.hand.extend(cards_played)

    #Winner adds the played cards to the bottom of their hand
    elif card_values[player1_card.value] > card_values[player2_card.value]:
        # print("-----------------")
        # print("%s takes the hand" % (player1.name))
        # print("-----------------")
        player1.hand.extend(cards_played) 
        
    elif card_values[player1_card.value] < card_values[player2_card.value]:
        # print("-----------------")
        # print("%s takes the hand" % (player2.name))
        # print("-----------------")
        player2.hand.extend(cards_played)
        
    #Use a tie breaker if card values are the same
    else:
        tie_breaker(player1, player2, cards_played)

#Initialize the deck and the players

number_rounds = []
winners = []

for i in range(1000):
    deck = Deck()
    player1 = Player("Ann")
    player2 = Player("Conor")

    rounds, winner = war(player1, player2, deck)
    if winner: #Exclude games that timed out
        number_rounds.append(rounds)
        winners.append(winner)

# for i in range(len(number_rounds)):
#     print("Game {0}: {1} in {2} rounds".format(i+1, winners[i], number_rounds[i]))
player1_wins = winners.count(player1.name)
player2_wins = winners.count(player2.name)

average_number_games = int(mean(number_rounds))
print("The average number of rounds for {0} games is {1}".format(len(winners), average_number_games))
print("{0} won {1} games".format(player1.name, player1_wins))
print("{0} won {1} games".format(player2.name, player2_wins))