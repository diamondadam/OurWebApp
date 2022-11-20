from copy import deepcopy
from enum import Enum

from ..models.pieces import *
from ..models.team import Team
from .chess_base import Point
from .engine_exceptions import InvalidMove

log = logging.getLogger('dan_sucks' + __name__)


class ChessEngine():
    def __init__(self) -> None:
        # Set White Major pieces
        self.player_white = Team(**{'name': 'white'})
        self.player_black = Team(**{'name': 'black'})

        bottom_white = [
            Rook(pos=Point(0, 0), team=self.player_white),
            Knight(pos=Point(0, 1), team=self.player_white),
            Bishop(pos=Point(0, 2), team=self.player_white),
            Queen(pos=Point(0, 3), team=self.player_white),
            King(pos=Point(0, 4), team=self.player_white),
            Bishop(pos=Point(0, 5), team=self.player_white),
            Knight(pos=Point(0, 6), team=self.player_white),
            Rook(pos=Point(0, 7), team=self.player_white),
        ]
        # Set White Minor pieces
        top_white = [Pawn(pos=Point(1, x), team=self.player_white)
                     for x in range(0, 8)]
        # Set Black Minor pieces
        top_black = [Pawn(pos=Point(6, x), team=self.player_black)
                     for x in range(0, 8)]
        # Set Black Major pieces
        bottom_black = [
            Rook(pos=Point(7, 0), team=self.player_black),
            Knight(pos=Point(7, 1), team=self.player_black),
            Bishop(pos=Point(7, 2), team=self.player_black),
            Queen(pos=Point(7, 3), team=self.player_black),
            King(pos=Point(7, 4), team=self.player_black),
            Bishop(pos=Point(7, 5), team=self.player_black),
            Knight(pos=Point(7, 6), team=self.player_black),
            Rook(pos=Point(7, 7), team=self.player_black),
        ]

        # Initialize Board
        self.board = [
            bottom_white,
            top_white,
            [None for x in range(0, 8)],
            [None for x in range(0, 8)],
            [None for x in range(0, 8)],
            [None for x in range(0, 8)],
            top_black,
            bottom_black
        ]

        # Create pointers to kings
        self.kings = {'White' : self.board[0][4], 'Black': self.board[7][4]}
        # Create History
        self.history = [deepcopy(self.board)]
        self.graveyards = {'White' : [], 'Black': []}

       

    def move(self, start: Point, end: Point, team: Team) -> tuple():
        """
        We are going to assume that the handler only allows user to 
        call move when it is their turn. 
        """

        # Make sure a piece exists there
        piece: Piece = self.board[start.y][start.x]

        if piece is None:
            raise InvalidMove('Not a Piece')

        if piece.team is not team:
            raise InvalidMove(f"Not {team}'s piece.")

        # Check that move is valid for that piece
        if (piece.is_valid(end, self.board)):

            # Make changes
            self.graveyards[team.name].append(self.board[end.y][end.x])
            self.board[end.y][end.x] = self.board[start.y][start.x]
            self.board[start.y][start.x] = None
            self.board[end.y][end.x].pos = end
            

            # If this cause the current_player to be in check reverse the changes and raise exception
            if team.in_check(self.board, self.kings[team.name]):
                self.board[start.y][start.x] = self.board[end.y][end.x]
                self.board[end.y][end.x] = self.graveyards[team.name].pop()   
                self.board[start.y][start.x].pos = start
                raise InvalidMove(f"Places {team} in check.")                 
            # Append game history
            self.history.append(deepcopy(self.board))
            if team.name == 'White':
                return (self.board, self.player_black.in_check(self.board, self.kings["Black"]))
            else:
                return (self.board, self.player_black.in_check(self.board, self.kings["White"]))

        else:
            # Raise invalid move exception
            raise Exception('Invalid Move: General Error')