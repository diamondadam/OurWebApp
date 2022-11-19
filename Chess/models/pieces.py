import logging
from ..engine.chess_base import Point, Vector

log = logging.getLogger('dan_sucks' + __name__)


class Piece():
    def __init__(self, **kwargs) -> None:
        self._pos: Point = kwargs['pos']
        self.team = kwargs['team']
        self.vectors: list = []

    def is_valid(self, end, board):
        for vector in self.vectors:
            points = vector.get_points(board, self.team, self.pos)
            # Check if the move is valid
            if end in points:
                log.debug(f"{end} in {points}")
                return True
            log.debug(f"{end} not in {points}")
        return False

    def __str__(self) -> str:
        f"{self.team}, {type(self)}, {self.pos}"
        return super().__str__()
    # Getter and Setters for the Pos value

    @property
    def pos(self):
        return self._pos

    @pos.setter
    def pos(self, value):
        self._pos = value


class Pawn(Piece):
    def __init__(self, **kwargs) -> None:
        self.first_move = True
        super().__init__(**kwargs)
        # Since pawns can only move one direction we have to flip that
        # Driection based on color
        # I hate pawns, the piece not the people
        if self.team.name == 'Black':
            self.vectors = [
                # 1 - 2 moves forward, decrement after first move
                Vector(Point(-1, 0), 2),
            ]

            self.attack_vectors = [
                # This is a special case only for the pawn
                Vector(Point(-1, 1), 1),  # Diagonal move right
                Vector(Point(-1, -1), 1),  # Diagonal move left
            ]
        else:
            self.vectors = [
                # 1 - 2 moves forward, decrement after first move
                Vector(Point(1, 0), 2),
            ]

            self.attack_vectors = [
                # This is a special case only for the pawn
                Vector(Point(1, 1), 1),  # Diagonal move right
                Vector(Point(1, -1), 1),  # Diagonal move left
            ]

    # Override the getter and setters to adjust magnitude after first move
    @property
    def pos(self):
        return self._pos

    @pos.setter
    def pos(self, value):
        if self.first_move:
            self.vectors[0].magnitude -= 1
            self.first_move = False
        self._pos = value

    # Override the is_valid function to account for seperate attack vectors
    def is_valid(self, end: Point, board):
        # If the move is an attack
        if board[end.y][end.x] is not None:
            for vector in self.attack_vectors:
                if end in vector.get_points(board, self.team, self.pos):
                    return True
            else:
                return False
        else:
            return super().is_valid(end, board)


class King(Piece):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.vectors = [
            Vector(Point(0, 1), 1),
            Vector(Point(0, -1), 1),
            Vector(Point(1, 0), 1),
            Vector(Point(-1, 0), 1),
            Vector(Point(1, 1), 1),
            Vector(Point(-1, 1), 1),
            Vector(Point(-1, -1), 1),
            Vector(Point(1, -1), 1),
        ]


class Queen(Piece):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.vectors = [
            Vector(Point(0, 1), 8),
            Vector(Point(0, -1), 8),
            Vector(Point(1, 0), 8),
            Vector(Point(-1, 0), 8),
            Vector(Point(1, 1), 8),
            Vector(Point(-1, 1), 8),
            Vector(Point(-1, -1), 8),
            Vector(Point(1, -1), 8),
        ]


class Bishop(Piece):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.vectors = [
            Vector(Point(1, 1), 8),
            Vector(Point(-1, 1), 8),
            Vector(Point(-1, -1), 8),
            Vector(Point(1, -1), 8),
        ]


class Knight(Piece):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.vectors = [
            # Start 0, 1
            Vector(Point(2, -1), 1),
            Vector(Point(2, 1), 1),
            Vector(Point(-2, -1), 1),
            Vector(Point(-2, 1), 1),

            Vector(Point(1, 2), 1),
            Vector(Point(-1, 2), 1),
            Vector(Point(-1, -2), 1),
            Vector(Point(1, -2), 1),
        ]


class Rook(Piece):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.vectors = [
            Vector(Point(0, 1), 8),
            Vector(Point(0, -1), 8),
            Vector(Point(1, 0), 8),
            Vector(Point(-1, 0), 8),
        ]
