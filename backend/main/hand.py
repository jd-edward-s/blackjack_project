from backend.main.card import values
from backend.main.deck import Deck


class Hand:
    def __init__(self):
        self.cards = []
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


def main():
    player_hand = Hand()
    deck = Deck()
    deck.deck_shuffle()
    for i in range(2):
        player_hand.add_card_to_hand(deck.deal_a_card())
    print(f"Number of cards in player's hand: {len(player_hand.cards)}")
    print(f"\nCards in player's hand")
    for i, card in enumerate(player_hand.cards):
        print(f"Card {i+1} : {card.__repr__()}")
    print(f"Number of cards left in the main deck: {len(deck.deck_pile)}")
    print(f"The value of the cards in the player's hand: {player_hand.value}")


if __name__ == "__main__":
    main()
