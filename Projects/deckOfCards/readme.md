# Deck of Cards implementation in Python 3
## By Steven Chung

This is actually from a job interview. This program first initializes a deck of cards in the main function:

```python
# Main function
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
```

Where the total number of cards in the deck is:

```python
# Total cards in the deck = length of the list
totalCardsInDeck = len(deckOfCards)
```

To shuffle the deck of cards we need to import the random library and create a function to shuffle the deck:

```python
import random

def shuffle(deckOfCards, totalCardsInDeck):
    # Swaps a card with another random generated card denoted by randomCard
    # which is within the range of deckOfCards
    for card in range(totalCardsInDeck):
        randomCard = random.randint(0, totalCardsInDeck - 1)
        deckOfCards[card], deckOfCards[randomCard] = deckOfCards[randomCard], deckOfCards[card]
        #print(card, deckOfCards[card], deckOfCards[randomCard])

    return deckOfCards
```

To deal one card when called we also need to build another function:

```python
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
```

Putting everything together, we write a test program that tests both the functions above:

```python
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
```

Alternatively, this program can use classes to help unclutter the deckOfCards array:

```python
import random

class Card: #class for each card

    def __init__(self, suit, rank):
        self.suit = suit    #member variable for suit
        self.rank = rank    #member variable for 'rank' 1 -> 13 = Ace -> King

def rank_dict(x):
    return {
            1: 'Ace', #Dictionary to map integer Card ranks to specific string ranks
            2: '2',
            3: '3',
            4: '4',
            5: '5',
            6: '6',
            7: '7',
            8: '8',
            9: '9',
            10: '10',
            11: 'Jack',
            12: 'Queen',
            13: 'King'
            }[x]

def suit_dict(x): #Function w/ dictionary to switch between suits for deck initialization
    return {
            1: 'Hearts',
            2: 'Spades',
            3: 'Diamonds',
            4: 'Clubs'
            }[x]

def shuffle(deck, num_cards): #Use random integer to shuffle deck indices
    for card in range(0, num_cards):
        random_card = random.randint(0, num_cards - 1)
        deck[card], deck[random_card] = deck[random_card], deck[card] #swap
    return deck, num_cards

def deal(deck, num_cards, no_more_cards): #Deal top card of deck; remove that card from the deck

    if no_more_cards == False:
        print(deck[0].rank + " of " + deck[0].suit) #Deal first card
        deck = deck[1 : num_cards] #Reassigns the deck to exclude the first (dealt) element
        num_cards -= 1
        if num_cards == 0:
            no_more_cards = True #Sets no more cards flag to true if only one element left in list (empty element; not a value)
    else:
        print("No more cards")

    return deck, num_cards, no_more_cards

#***Deck Initialization***

#One deck has 52 cards w/ 4 suits, each suit containing 13 individually ranked cards.

deck = list(range(1,53)) #Creates list 'deck' with numbers 1 - 52
card_count = 0

for suit in range(1, 5): #Switch suits for creation
    for rank in range(1, 14): #Switch ranks
        deck[card_count] = Card(suit_dict(suit), rank_dict(rank)) #Set current card class's suit and rank
        card_count += 1

#***Main***

num_cards = len(deck)
no_more_cards = False #Flag to determine if cards remain in deck

while True:
    callCards = int( input("How many cards would you like? ") )
    if callCards > 0:
        for call in range(0, callCards):
            [deck, num_cards] = shuffle(deck, num_cards)
            [deck, num_cards, no_more_cards] = deal(deck, num_cards, no_more_cards)
            if no_more_cards == True:
                break

    elif callCards < 0:
         print("Sorry, please enter a valid input (non-zero, positive integer).")
    if no_more_cards == True:
        print("game over")
        break
```
