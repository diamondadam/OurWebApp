from .chess_models import *
class Team():
    def __init__(self, wob:bool) -> None:
        self.wob = wob
        self.graveyard = []
        
class Game():
    def __init__(self) -> None:
        self.board = Board()
        # Append the state of the board after every turn 
        self.history = [self.board]
        teams = [Team(0), Team(1)]

    def move(self, piece: Piece, start: Point, end: Point, team):
        if(piece.is_valid(start, end)):
            #TODO implement this method on board
            if self.board.is_in_check(team):
                # Make an exception
                raise Exception('Bad Move')
            self.board[start.x][start.y] = None
            # Verify if it is an attack. 
            if self.board[end.x][start.y]:
                taken_piece = self.board[end.x][start.y]
            self.board[end.x][start.y] = piece
            self.history.append[self.board]
            self.teams[team].graveyard.append(taken_piece)
            return self.board.is_in_check(not team)
            
