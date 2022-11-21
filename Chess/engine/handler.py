from .chess_engine import ChessEngine
class Handler():
    #TODO Implement ORM to handle game data    

    @staticmethod    
    def get_game(game_id):
        return 'Game'

    @staticmethod
    def move(game_id, start, end, team):
        return 'Move'

    @staticmethod
    def create_game(white, black):
        return 'New Game'
    