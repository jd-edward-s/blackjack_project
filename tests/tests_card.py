from main.card import Card


def test_card_creation():
    new_card = Card('Clubs', 'Ace')
    assert isinstance(new_card, Card)
    assert new_card.suit == 'Clubs'
    assert new_card.rank == 'Ace'
    assert new_card.value == 11
