import uuid

class GoGamePool():
    def __init__(self):
        self.games = {}

    def add_game(self,game):
        game_uuid = uuid.uuid1()
        uuid_for_watchers = uuid.uuid1()
        #print(game_uuid)
        game = {'uuid_for_watchers' : str(uuid_for_watchers), 'game' : game}
        self.games[str(game_uuid)] = game
        return str(game_uuid), str(uuid_for_watchers)
    
    def get_game(self, game_uuid):
        return self.games[game_uuid]['game']
    
    #this function checks whether the uuid typed by the watcher is among the UUIDs for watchers in the dict (i.e. associated with a game)
    def fetch_streamer_game_uuid(self,streamer_game_uuid):
        for key, value in self.games.items():
            if value ['uuid_for_watchers'] == streamer_game_uuid :
                return True
        return False

    def get_game_from_watcher_uuid(self, watcher_uuid):
        for key, value in self.games.items():
            if value ['uuid_for_watchers'] == watcher_uuid :
                return value ['game']
        return None
    
