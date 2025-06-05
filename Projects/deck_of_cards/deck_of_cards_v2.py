import random
from collections import defaultdict


class Card:
    def __init__(self, suit: str, rank: str):
        self.suit = suit  # Member variable for suit
        self.rank = rank  # Member variable for 'rank' 1 -> 13 = Ace -> King


class Solution:
    def __init__(self):
        '''
        Deck Initialization

        One deck has 52 cards w/ 4 suits, each suit containing 13 individually ranked cards.
        '''
        self.deck = defaultdict(Card)
        self.cards_left = 52
        self.no_more_cards = False  # Flag to determine if cards remain in deck
        card_count = 0

        for suit in range(1, 5):  # Switch suits for creation
            for rank in range(1, 14):  # Switch ranks
                self.deck[card_count] = Card(
                    self.suit_dict(suit), self.rank_dict(rank)
                )  # Set current card class's suit and rank
                card_count += 1

    def rank_dict(self, x: int) -> str:
        # Dictionary to map integer Card ranks to specific string ranks
        return {
            1: 'Ace',
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
            13: 'King',
        }[x]

    def suit_dict(self, x: int) -> str:
        # Function w/ dictionary to switch between suits for deck initialization
        return {1: 'Hearts', 2: 'Spades', 3: 'Diamonds', 4: 'Clubs'}[x]

    def shuffle(self) -> None:
        # Convert deck dictionary to a list
        deck_list = list(self.deck.values())
        # Shuffle the list
        random.shuffle(deck_list)
        # Convert the shuffled list back to a dictionary
        self.deck = {i: card for i, card in enumerate(deck_list)}

    def deal(self) -> None:
        # Deal top card of deck; remove that card from the deck
        if not self.no_more_cards:
            # Deal first card
            print(f'{self.deck[0].rank} of {self.deck[0].suit}')
            # Reassigns the deck to exclude the first (dealt) element
            del self.deck[0]
            self.cards_left -= 1
            if self.cards_left == 0:
                # Sets no more cards flag to true if only one element left in list (empty element; not a value)
                self.no_more_cards = True
        else:
            print('No more cards')

    def printError(self):
        print('Sorry, please enter a valid input (non-zero, positive integer).')

    def run(self):
        while True:
            try:
                user_input = int(
                    input(
                        f'How many cards would you like (1-{self.cards_left})? '
                    )
                )
                if user_input > 0:
                    for _ in range(0, user_input):
                        self.shuffle()
                        self.deal()
                        if self.no_more_cards:
                            break
                elif user_input < 0:
                    self.printError()

                if self.no_more_cards:
                    print('All cards dealt!')
                    break
            except ValueError:
                self.printError()


if __name__ == '__main__':
    test = Solution()
    test.run()
