from flask import Flask, render_template
from flask_socketio import SocketIO
import socketio
import pydealer

app = Flask(__name__)
socketio = SocketIO(app)

game_state = {
    "players": {},
    "current_player": 0,
    "last_play": None,
    "game_over": False,
    "winner": None
}

def create_game():
    deck = pydealer.Deck(ranks=pydealer.BIG2_RANKS, rebuild=True, re_shuffle=True)
    
    game_state["players"] = {
        0: {"hand": deck.deal(13), "name": "You", "passed": False},
        1: {"hand": deck.deal(13), "name": "Player 2", "passed": False},
        2: {"hand": deck.deal(13), "name": "Player 3", "passed": False},
        3: {"hand": deck.deal(13), "name": "Player 4", "passed": False}
    }

    for player in game_state["players"].values():
        player["hand"].sort(ranks=pydealer.BIG2_RANKS)

    starting_player = None
    for player_id, player in game_state["players"].items():
        if player["hand"].find("3 of Diamonds"):
            starting_player = player_id
            break
    
    game_state["current_player"] = starting_player
    game_state["last_play"] = None
    game_state["game_over"] = False

    return game_state
    
def valid_play(cards, last_play):
    player_hand = game_state["players"][0]["hand"]
    # cards =
    return True



@app.route("/")
def main_menu():
    return render_template("index.html")

@app.route("/create-game")
def create_games():
    create_game()
    return render_template("create.html")

@app.route("/join-game")
def join_game():
    return render_template("join.html")

@app.route("/game")
def game():
    return render_template("game.html")

@app.route("/game-lobby")
def game_lobby():
    return render_template("lobby.html")

@app.route("/rules")
def game_rules():
    return render_template("rules.html")

@app.route("/test")
def test():
    create_game()
    valid_play()
    return f"Hello World"

if __name__ == "__main__":
    app.run(debug=True)

"""
@socketio.on("play_cards")
def handle_play(data):
"""