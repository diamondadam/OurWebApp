class Board():
    def __init__(self) -> None:
        bottom_white = [
            Rook(pos=Point(0, 0), color=0),
            Bishop(pos=Point(1, 0), color=0),
            Knight(pos=Point(2, 0), color=0),
            Queen(pos=Point(3, 0), color=0),
            King(pos=Point(4, 0), color=0),
            Knight(pos=Point(2, 0), color=0),
            Bishop(pos=Point(1, 0), color=0),
            Rook(pos=Point(0, 0), color=0),
        ]
        top_white = [Pawn(pos=Point(x, 1), color=0) for x in range(0, 8)]
        
        top_black = [Pawn(pos=Point(x, 6), color=1) for x in range(0, 8)]
        bottom_black = [
            Rook(pos=Point(0, 7), color=1),
            Bishop(pos=Point(1, 7), color=1),
            Knight(pos=Point(2, 7), color=1),
            Queen(pos=Point(3, 7), color=1),
            King(pos=Point(4, 7), color=1),
            Knight(pos=Point(2, 7), color=1),
            Bishop(pos=Point(1, 7), color=1),
            Rook(pos=Point(0, 7), color=0),
        ]

        self.board=[
            bottom_white,
            top_white,
            [None for x in range(0, 8)],
            [None for x in range(0, 8)],
            [None for x in range(0, 8)],
            [None for x in range(0, 8)],
            top_black,
            bottom_black
        ]


class Point():
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def __mul__(self, n: int):
        self.x *= n
        self.y *= n
        return self

    def is_off(self) -> bool:
        if self.x < 0:
            return True
        if self.x > 8:
            return True
        if self.y < 0:
            return True
        if self.y > 8:
            return True
        return False

class Vector():
    def __init__(self, x, y, magnitude) -> None:
        self.point = Point(x, y)
        self.magnitude = magnitude

    def get_points(self):
        points = []
        for i in range(1, self.magnitude):
            if (self.point * i).is_off():
                return points
            points.append(self.point * i)

        return points


class Piece():
    def __init__(self, **kwargs) -> None:
        self.pos = kwargs['pos']
        # self.picture = kwargs['pic']
        self.color = kwargs['color']
        self.vectors = []

    def is_valid(self, point):
        for vector in self.vectors:
            if point in vector.get_points():
                return True
        return False


class Pawn(Piece):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.vectors = [
            Vector(0, 1, 2),  # 1 - 2 moves forward, decrement after first move
        ]

        self.attack_vectors = [
            #This is a special case only for the pawn
            Vector(1, 1, 1),  # Diagonal move right
            Vector(-1, 1, 1),  # Diagonal move left
        ]

    def decrement_pawn(self):
        self.vectors[0].magnitude -= 1

    def is_valid(self, point, attack):
        if attack:
            for vector in self.attack_vectors:
                if point in vector.get_points():
                    return True
            return False
        else:
            super().is_valid(point)


class King(Piece):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.vectors = [
            Vector(0, 1, 1),
            Vector(0, -1, 1),
            Vector(1, 0, 1),
            Vector(-1, 0, 1),

            Vector(1, 1, 1),
            Vector(-1, 1, 1),
            Vector(-1, -1, 1),
            Vector(1, -1, 1),
        ]


class Queen(Piece):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.vectors = [
            Vector(0, 1, 8),
            Vector(0, -1, 8),
            Vector(1, 0, 8),
            Vector(-1, 0, 8),

            Vector(1, 1, 8),
            Vector(-1, 1, 8),
            Vector(-1, -1, 8),
            Vector(1, -1, 8),
        ]


class Bishop(Piece):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.vectors = [
            Vector(1, 1, 8),
            Vector(-1, 1, 8),
            Vector(-1, -1, 8),
            Vector(1, -1, 8),
        ]


class Knight(Piece):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        # TODO Change moveset
        self.vectors = [
            Vector(1, 1, 8),
            Vector(-1, 1, 8),
            Vector(-1, -1, 8),
            Vector(1, -1, 8),
        ]

class Rook(Piece):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.vectors = [
            Vector(0, 1, 8),
            Vector(0, -1, 8),
            Vector(1, 0, 8),
            Vector(-1, 0, 8),
        ]
