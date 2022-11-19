import logging
log = logging.getLogger('dan_sucks' + __name__)

class Point():

    def __init__(self, y, x) -> None:
        self.y = y
        self.x = x

    def __mul__(self, n: int):
        return Point(self.y * n, self.x * n)

    def __add__(self, p):
        return Point(self.y + p.y, self.x + p.x)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def off_edge(self):
        if self.x < 0 or self.y < 0 or self.x > 7 or self.y > 7:
            return True
        return False

    def __str__(self) -> str:
        return (f"y: {self.y}, x: {self.x}")


class Vector():
    def __init__(self, point: Point, magnitude: int) -> None:
        self.point = point
        self.magnitude = magnitude

    def get_points(self, board, team, start) -> list:
        # Condition to check for
        # Movement is limited by board edges,
        # enemy players inclusive
        # friendly players exclusive
        points = []
        
        for i in range(1, self.magnitude+1):
            n_point: Point = start + (self.point * i)
            # If we have reach the edge of the board in this vector return
            if n_point.off_edge():
                return points
            # If the position is not None
            if board[n_point.y][n_point.x] is not None:
                # Make sure it is and enemy, return regardlessss
                if board[n_point.y][n_point.x].team == team:
                    return points
                else:
                    log.debug((f"{type(board[self.point.y][self.point.x]).__name__} at {start}\n"
                                    f"\tHas a valid move to {n_point}"))
                    points.append(n_point)
                    return points
            # Else the position is None and is valid
            else:
                log.debug((f"{type(board[self.point.y][self.point.x]).__name__} at {start}\n"
                                f"\tHas a valid move to {n_point}"))
                points.append(n_point)
        return points
