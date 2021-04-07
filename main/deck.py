import random

from main.card import ranks, suits, Card


class Deck:
    def __init__(self):

        self.deck_pile = []

        for suit in suits:
            for rank in ranks:
                self.deck_pile.append(Card(suit, rank))

    def __repr__(self):

        deck_structure = ""
        for card in self.deck_pile:
            deck_structure += '\n' + card.__repr__()
        return f"The deck consists of: {deck_structure}"

    def deck_shuffle(self):
        random.shuffle(self.deck_pile)

    def deal_a_card(self):
        return self.deck_pile.pop()


def main():
    new_deck = Deck()
    print(f"The deck has {len(new_deck.deck_pile)} cards in total")
    print(f'Top card before shuffle: {new_deck.deck_pile[0]}')
    Deck.deck_shuffle(new_deck)
    print(f'Top card after shuffle: {new_deck.deck_pile[0]}')
    print(f'Card dealt is: {Deck.deal_a_card(new_deck)}')
    print(f'{len(new_deck.deck_pile)} cards remaining after dealing one card')


if __name__ == '__main__':
    main()


