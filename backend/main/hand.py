from backend.main.card import values
from backend.main.deck import Deck


class Hand:
    def __init__(self):
        self.cards = []
        self.cards_split = []
        self.value = 0
        self.aces = 0

    def add_card_to_hand(self, card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == "Ace":
            self.aces += 1

    def adjust_for_ace(self):

        while self.value > 21 and self.aces > 0:
            self.value -= 10
            self.aces -= 1

    def split_hand(self):
        self.cards_split.append(self.cards.pop())

    def hit(self, card):
        self.add_card_to_hand(card)
        self.adjust_for_ace()


def main():
    player_hand = Hand()
    deck = Deck()
    deck.deck_shuffle()
    print("Player's hand:")
    for i in range(2):
        player_hand.add_card_to_hand(deck.deal_a_card())
        print(f"Card {i + 1} : {player_hand.cards[-1].__repr__()}")
    print(player_hand.value)
    player_hand.hit(deck.deal_a_card())
    print(f"Card 3 : {player_hand.cards[-1]}")
    print(player_hand.value)


if __name__ == "__main__":
    main()
