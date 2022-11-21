from flask import Flask
from flask import request
from Chess.engine.handler import Handler

app = Flask(__name__)

@app.route("/chessgame/", methods=['POST'])
def create_game():
    """Returns a game instance in json format 
    Return:
    json(board)
    """
    return Handler.create_game(request.get_json()[0], request.get_json()[1])

@app.route("/chessgame/<game_id>", methods=['GET'])
def get_game(game_id):
    """Returns a game instance in json format 
    Keyword arguments:
    game_id -- id of the game instance
    Return:
    json(board)
    """
    return Handler.get_game(game_id)

@app.route("/chessgame/<game_id>", methods=['POST'])
def move(game_id):
    """Returns a game instance in json format 
    Keyword arguments:
    game_id -- id of the game instance
    Payload:
    json [{x: <x>, y: <y>}, {x: <x>, y: <y>}, <team>]
    Return:
    json(board)
    """
    req = request.get_json()
    start = (req[0]['x'], req[0]['y'])
    end = (req[1]['x'], req[1]['y'])
    team = req[2]
    return Handler.move(game_id, start, end, team)



