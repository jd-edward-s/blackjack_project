suits = ('Hearts', 'Diamonds', 'Clubs', 'Spades')
ranks = ('One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'One': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __repr__(self):
        return f"{self.rank} of {self.suit}"


if __name__ == "__main__":
    new_card = Card('Hearts', 'Two')
    print(new_card)
    print(f"{new_card.rank} of {new_card.suit}")
