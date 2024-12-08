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
        print(sente_package_game)
        print(sente_package_game)

        #print(sente_package_game.get_results())
        #print(sente_package_game.get_results())

        #print(sente_package_game.score)

        #print(sente_package_game.score())

        #print(sente_package_game.get_winner())
        #print(sente_package_game.get_result())
        #print(sente_package_game.get_handicap())
        print(sente_package_game.get_properties())
        #print(sente_package_game.get_properties()['RE'])
        #print(sente_package_game.get_properties()['HD'])



        




        return {"white":7, "black":5}