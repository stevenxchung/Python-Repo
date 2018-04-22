# Deck of Cards implementation in Python 3 by Steven Chung

import random

def shuffle(deckOfCards, totalCardsInDeck):
    # Swaps a card with another random generated card denoted by randomCard
    # which is within the range of deckOfCards
    for card in range(totalCardsInDeck):
        randomCard = random.randint(0, totalCardsInDeck - 1)
        deckOfCards[card], deckOfCards[randomCard] = deckOfCards[randomCard], deckOfCards[card]
        #print(card, deckOfCards[card], deckOfCards[randomCard])
    
    return deckOfCards

def deal_one_card(deckOfCards, totalCardsInDeck):
    # Deals one card at a time as long as the deck is not empty
    if totalCardsInDeck != 0:
        print(deckOfCards[0])
        deckOfCards = deckOfCards[1:totalCardsInDeck]
        totalCardsInDeck -= 1
    # If the deck is empty then the game will issue a statement declaring that there are no cards left
    else:
        print("Sorry, there are no cards left in the deck.")
    # We want to update the total cards so we return it
    return deckOfCards, totalCardsInDeck

# Main function
#deckOfCards = list(range(1, 53))
deckOfCards = ["Ace of Hearts", "Ace of Diamonds", "Ace of Clubs", "Ace of Spades", 
                "2 of Hearts", "2 of Diamonds", "2 of Clubs", "2 of Spades",
                "3 of Hearts", "3 of Diamonds", "3 of Clubs", "3 of Spades",
                "4 of Hearts", "4 of Diamonds", "4 of Clubs", "4 of Spades",
                "5 of Hearts", "5 of Diamonds", "5 of Clubs", "5 of Spades",
                "6 of Hearts", "6 of Diamonds", "6 of Clubs", "6 of Spades",
                "7 of Hearts", "7 of Diamonds", "7 of Clubs", "7 of Spades",
                "8 of Hearts", "8 of Diamonds", "8 of Clubs", "8 of Spades",
                "9 of Hearts", "9 of Diamonds", "9 of Clubs", "9 of Spades",
                "10 of Hearts", "10 of Diamonds", "10 of Clubs", "10 of Spades",
                "Jack of Hearts", "Jack of Diamonds", "Jack of Clubs", "Jack of Spades",
                "Queen of Hearts", "Queen of Diamonds", "Queen of Clubs", "Queen of Spades",
                "King of Hearts", "King of Diamonds", "King of Clubs", "King of Spades"]
# Total cards in the deck = length of the list
totalCardsInDeck = len(deckOfCards)
#print(shuffle(deckOfCards, totalCardsInDeck))

# Test program within the main function to deal a number of cards specified by user
# Loop through until there are no cards left
while True:
    callCards = int(input("How many cards would you like? "))
    # Check if call for number of cards is within bounds
    if callCards > 0 and callCards < 53:
        # Executes the shuffle function and deal one card from the deck until the 52nd card is dealt
        for call in range(0, callCards):
            deckOfCards = shuffle(deckOfCards, totalCardsInDeck)
            [deckOfCards, totalCardsInDeck] = deal_one_card(deckOfCards, totalCardsInDeck)
            # This is minor but it makes "Sorry, there are no cards left in the deck." print
            # only once after the 52nd card is dealt
            if totalCardsInDeck == 0:
                print("Sorry, there are no cards left in the deck.")
                break
    elif callCards >= 53:
        print("Sorry, please enter a value less than 53")
    else:
        print("Sorry, please enter a valid input (non-zero, positive integer).")
    # If there are no more cards in the deck, end the program
    if totalCardsInDeck == 0:
        break