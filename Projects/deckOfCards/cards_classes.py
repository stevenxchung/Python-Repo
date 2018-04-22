import random

class Card: #class for each card

	def __init__(self, suit, rank):
		self.suit = suit 	#member variable for suit
		self.rank = rank	#member variable for 'rank' 1 -> 13 = Ace -> King

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
