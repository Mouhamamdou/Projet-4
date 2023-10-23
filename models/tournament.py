from models.round import Round
import json
import random


class Tournament:

    json_file = "data/players.json"

    def __init__(self):
        self.name = None
        self.place = None
        self.start_date = None
        self.end_date = None
        self.round_number = 1
        self.nbr_of_round = 4
        self.description = ""
        self.rounds = [Round(f"Round {i + 1}") for i in range(self.nbr_of_round)]
        self.players = []

    def registered_player(self, player):
        self.players = self.load_players()
        self.players.append(player.to_dict())
        with open(Tournament.json_file, 'w') as file:
            json.dump(self.players, file, indent=2)

    def load_players(self):
        try:
            with open(Tournament.json_file, 'r') as file:
                self.players = json.load(file)
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            self.players = []
        return self.players

    def mix_players(self):
        random.shuffle(self.players)
        return self.players

    def generate_pairs(self, round_number):
        pairs = [(self.players[i], self.players[i + 1]) for i in range(0, len(self.players) - 1, 2)]
        for pair in pairs:
            self.rounds[round_number - 1].add_match(pair)
        return pairs

    def sorted_players(self):
        with open(self.json_file, 'r') as file:
            self.players = json.load(file)
        self.players.sort(key=lambda s: s["points"], reverse=True)
        with open(Tournament.json_file, 'w') as file:
            json.dump(self.players, file, indent=2)

    def sorted_players_by_name(self):
        players = self.load_players()
        players_by_name = sorted(players, key=lambda x: x['first_name'])
        return players_by_name


'''
if __name__ == "__main__":

    play1 = Player("soso", "Fall", datetime(1984,5,24))

    play2 = Player("lala","faye",datetime(1580,6,11))

    play3 = Player("gur", "marius", datetime(1999, 8, 4))

    play4 = Player("falla", "fleur", datetime(1960, 9, 16))

    play5 = Player("fofo", "diagne", datetime(1994,1,4))

    play6 = Player("mama","sene",datetime(1980,5,10))

    play7 = Player("golbert", "diagne", datetime(1995, 7, 14))

    play8 = Player("talla", "gaye", datetime(2000, 4, 6))

    tournoi = Tournament("Tournoi d'échecs", "LieuX", "2023-01-01", "2023-01-15", nbr_of_round=3)

    #tournoi.registered_player([play1, play2])

    tournoi.registered_player(play1)

    tournoi.registered_player(play2)

    tournoi.registered_player(play3)

    tournoi.registered_player(play4)

    tournoi.registered_player(play5)

    tournoi.registered_player(play6)

    tournoi.registered_player(play7)

    tournoi.registered_player(play8)

    #match1 = Match(play1, play2)
    #print(match1)

    #tours = tournoi.rounds
    #for tour in tours:
        #print(tour.round_name)
        #tour.add_match(match1)
        #print(tour.matches)

    #print(tournoi.players)
    play2.scored()
    print(play2.score)

    #match1.result_match()

    #match1.update_json_file()

    print(tournoi.players)
    tournoi.sorted_players()
    print(tournoi.players)

    for match in tournoi.generate_the_matches():
        print(match)

'''
