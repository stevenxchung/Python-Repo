import random


def shuffle(deck, num_cards):
    for card in range(0, num_cards):
        random_card = random.randint(0, num_cards - 1)
        deck[card], deck[random_card] = deck[random_card], deck[card]  # swap
    return deck, num_cards


def deal(
    deck, num_cards, no_more_cards
):  # Deal top card of deck; remove that card from the deck
    if no_more_cards == False:
        print(deck[0])  # Deal first card
        deck = deck[
            1:num_cards
        ]  # Reassigns the deck to exclude the first (dealt) element
        num_cards -= 1
        if num_cards == 0:
            no_more_cards = True  # Sets no more cards flag to true if only one element left in list (empty element; not a value)
    else:
        print("No more cards")

    return deck, num_cards, no_more_cards


deck = list(range(1, 53))
num_cards = len(deck)
no_more_cards = False  # Flag to determine if cards remain in deck

for i in range(0, 53):
    [deck, num_cards] = shuffle(deck, num_cards)
    [deck, num_cards, no_more_cards] = deal(deck, num_cards, no_more_cards)
