import uuid

class GoGamePool():
    def __init__(self):
        self.games = {}

    def add_game(self,game):
        game_uuid = uuid.uuid1()
        uuid_for_watchers = uuid.uuid1()
        #print(game_uuid)
        game = {'uuid_for_watchers' : uuid_for_watchers, 'game' : game}
        self.games[str(game_uuid)] = game
        return str(game_uuid)
    
    def get_game(self, game_uuid):
        return self.games[game_uuid]['game']
    
