import uuid

class GoGamePool():
    def __init__(self):
        self.games = {}

    def add_game(self,game):
        game_uuid = uuid.uuid1()
        print(game_uuid)
        self.games[str(game_uuid)] = game
        return game_uuid
    
    def get_captures_from_game(self, game_uuid):

        sente_package_game = self.games[game_uuid].game
        return {"white":7, "black":5}