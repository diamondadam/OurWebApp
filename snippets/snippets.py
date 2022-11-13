    # This file is all the code I wrote or copy pastad from stack and didn't want to delet completley

    
    # def find_limit(self, point: Point, vector: Vector, board: Board):
    #     limit = 0
    #     for point in vector.get_points():
    #         # For each point lieing on the line
    #         # if the point on the board returns a piece
    #         # that is the limit 
    #         if board.square(point):
    #             return limit
    #         # Else return the full magnitude
    #         return limit


    # https://stackoverflow.com/questions/328107/how-can-you-determine-a-point-is-between-two-other-points-on-a-line-segment
    # def isBetween(self, a: Point, b: Point, c: Point):
    #     crossproduct = (c.y - a.y) * (b.x - a.x) - (c.x - a.x) * (b.y - a.y)

    #     # compare versus epsilon for floating point values, or != 0 if using integers
    #     if abs(crossproduct) != 0:
    #         return False

    #     dotproduct = (c.x - a.x) * (b.x - a.x) + (c.y - a.y)*(b.y - a.y)
    #     if dotproduct < 0:
    #         return False

    #     squaredlengthba = (b.x - a.x)*(b.x - a.x) + (b.y - a.y)*(b.y - a.y)
    #     if dotproduct > squaredlengthba:
    #         return False

    #     return True

    
# def is_valid(self, point):
#     for vector in self.vectors:
#         # If it is a dynamically limited piece
#     #if vector.magnitude == None:
#         # Find the limit in this vector
#         #vector.magnitude = self.find_limit(vector)
#         # If point lies between (inclusive) it is valid
#         if point in vector.get_points():
#             return True
#         # if self.isBetween(self.pos, vector.point, point):
#         #     return True
#         # Reset the Vector limit
#         # vector.magnitude = None

#         # elif point in vector.get_points():
#         #     # Else if the moveset is static
#         #     return True
#     return False
