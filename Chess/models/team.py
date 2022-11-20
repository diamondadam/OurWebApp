
import logging
from ..models.pieces import King

log = logging.getLogger('dan_sucks' + __name__)


class Team():
    def __init__(self, **kwargs) -> None:
        self.name: str = str(kwargs['name']).strip().lower().capitalize()
        self.check: bool = False

    def in_check(self, board, king):
        for row in board:
            for piece in row:
                if piece is not None and piece.team == self:
                    if piece.is_valid(king.pos, board):
                        log.debug((f"Piece {piece} for team {piece.team} has team {self.team}"
                                   f"in check from {piece.pos.y}, {piece.pos.x} to {king.pos.y},"
                                   f"{king.pos.x}"))
                        return True
        return False

    def __str__(self) -> str:
        return self.name

