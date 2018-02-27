class Card:
    def __init__(self, suit, number):
        self._suit = suit
        self.number = number

    def __repr__(self):
        return self.number + " of " + self.suit

    @property
    def suit(self):
        return self._suit

    @suit.setter
    def suit(self, suit):
        if suit in ["hearts", "clubs", "diamonds", "spades"]:
            self._suit = suit
        else:
            print("That's not a suit!")

class Deck:
    def __init__(self):
        self._cards = []
        self.populate()
        print(self._cards)

    def populate(self):
        suits = ["hearts", "clubs", "diamonds", "spades"]
        numbers = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
        cards = []
        for suit in suits:
            for number in numbers:
                cards.append(Card(suit, number))
        self._cards = cards


if __name__ == '__main__':
    my_card = Card("hearts", "6")
    print(my_card)
    my_deck = Deck()