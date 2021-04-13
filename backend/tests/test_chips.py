from backend.main.chips import Chips


def test_chips_creation():
    player_chips = Chips()
    assert isinstance(player_chips, Chips)
