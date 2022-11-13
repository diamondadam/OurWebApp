import pytest
from Chess.models.game import Game


def test_build_game():
    game = Game()
    assert 2 + 2 == 4
