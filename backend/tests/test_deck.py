from backend.main.deck import Deck
from backend.main.card import Card


def test_deck_creation():
    """"
    Tests that the deck is created completely with 52 unique card objects.
    """
    new_deck = Deck()
    assert isinstance(new_deck, Deck)
    assert isinstance(new_deck.deck_pile[0], Card)
    assert len(new_deck.deck_pile) == 52
    assert len(set(new_deck.deck_pile)) == 52


def test_deck_shuffle():
    """
    Tests that the top card in the deck pile before a shuffle is different to the top card in the deck pile
    post the shuffle method.
    """
    new_deck = Deck()

    top_card = new_deck.deck_pile[0]
    Deck.deck_shuffle(new_deck)
    new_top_card = new_deck.deck_pile[0]

    assert top_card != new_top_card


def test_deal_a_card():
    """
    Checks that when the deal_a_card() is called the deck pile reduces by one and the dealt card is removed from the
    deck pile.
    """
    new_deck = Deck()
    dealt_card = Deck.deal_a_card(new_deck)
    assert len(new_deck.deck_pile) == 51
    assert dealt_card not in new_deck.deck_pile
