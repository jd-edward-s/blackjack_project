from backend.main.hand import Hand
from backend.main.deck import Deck
from backend.main.card import Card


def test_hand_creation():
    hand = Hand()
    deck = Deck()
    deck.deck_shuffle()
    for i in range(2):
        hand.add_card_to_hand(deck.deal_a_card())

    assert isinstance(hand, Hand)
    assert len(hand.cards) == 2
    assert len(deck.deck_pile) == 50


def test_adjust_for_aces():
    card1 = Card('Hearts', 'Ace')
    card2 = Card('Spades', 'Nine')
    card3 = Card('Diamonds', 'Eight')
    hand = Hand()
    hand.add_card_to_hand(card1)
    assert hand.value == 11
    hand.add_card_to_hand(card2)
    assert hand.value == 20
    hand.add_card_to_hand(card3)
    assert hand.value == 28
    hand.adjust_for_ace()
    assert hand.value == 18


def test_split_hand():
    hand = Hand()
    card1 = Card('Hearts', 'Ten')
    card2 = Card('Spades', 'Ten')
    cards = [card1, card2]
    for card in cards:
        hand.add_card_to_hand(card)

    if hand.cards[0].rank == hand.cards[-1].rank and hand.cards[0].rank != 'Ace':
        hand.split_hand()

        assert hand.cards[0].value == hand.cards_split[0].value
