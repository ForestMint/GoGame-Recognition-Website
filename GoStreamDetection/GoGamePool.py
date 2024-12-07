import uuid

class GoGamePool():
    def __init__(self):
        self.games = {}

    def add_game(self,game):
        game_uuid = uuid.uuid1()
        print(game_uuid)
        self.games[game_uuid] = game
        return game_uuid