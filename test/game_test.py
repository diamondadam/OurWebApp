import logging
import pytest
from Chess.engine.chess_engine import ChessEngine
from Chess.engine.chess_base import Point

logger = logging.getLogger('dan_sucks')

handler = logging.StreamHandler()
formatter = logging.Formatter(
    '%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)


def test_engine():
    game = ChessEngine()
    assert 2 + 2 == 4


def test_point_multiplication():
    point = Point(1, 1)
    for i in range(0, 8):
        n_point = point*i
        assert n_point.x == i
        assert n_point.y == i


def test_invalid_move():
    engine = ChessEngine()
    with pytest.raises(Exception) as e_info:
        engine.move(Point(0, 0), Point(5, 5), engine.player_white)
    with pytest.raises(Exception) as e_info:   
        board = engine.move(
            Point(1, 0), Point(2, 0), engine.player_black)


def test_game1():
    # Semi-Slav Defense: Meran. Wade Variation (D47)  ·  0-1
    # https://www.chessgames.com/perl/chessgame?gid=1333287
    engine = ChessEngine()

    board = engine.move(Point(1, 4), Point(
        3, 4), engine.player_white)  # White Pawn
    board = engine.move(Point(6, 4), Point(
        4, 4), engine.player_black) # Black Pawn
    board = engine.move(Point(0, 6), Point(
        2, 5), engine.player_white) # White KF3
    board = engine.move(Point(6, 5), Point(
        5, 5), engine.player_black) # Black Pawn
    board = engine.move(Point(2, 5), Point(
        4, 4), engine.player_white) # White Horse
    board = engine.move(Point(5, 5), Point(
        4, 4), engine.player_black) # Black Horse
    print('test')
    # assert engine.move(Point(0, 0), Point(0, 0), turn) == False
    # assert engine.move(Point(0, 0), Point(0, 0), turn) == False
    # assert engine.move(Point(0, 0), Point(0, 0), turn) == False
    # assert engine.move(Point(0, 0), Point(0, 0), turn) == False
    # assert engine.move(Point(0, 0), Point(0, 0), turn) == False
