import json
from models.tournament import Tournament
from models.player import Player
from models.match import Match
from views.tournamentview import TournamentView


class TounrnamentManager:

    json_file = "data/tournaments.json"

    def __init__(self):
        self.tournament = Tournament()
        self.player = Player
        self.view = TournamentView()

    def create_tournament(self):
        name, place, start_date, end_date = self.view.prompt_create_tournament()
        self.tournament.name = name
        self.tournament.place = place
        self.tournament.start_date = start_date.strftime('%Y-%m-%d')
        self.tournament.end_date = end_date.strftime('%Y-%m-%d')
        self.tournament.load_players()
        self.tournament.mix_players()
        self.save_tournament()

    def throw_round(self, round_number):
        print()
        round_ = self.tournament.rounds[round_number - 1]
        print(f'{round_.round_name} débute : ')
        pairs = self.tournament.generate_pairs(round_number)
        print(f'les paires dans le {round_.round_name} {pairs}')
        for players in pairs:
            p1 = players[0]
            p2 = players[1]
            player1 = Player(p1['first_name'], p1['last_name'], p1['date_of_birth'])
            player2 = Player(p2['first_name'], p2['last_name'], p2['date_of_birth'])
            match = Match(player1, player2)
            match.play_match()
            match.result_match()
            match.update_json_file()
        self.tournament.sorted_players()

    def add_player(self):
        player_data = self.view.prompt_add_player()
        p = self.player.add_player(player_data[0], player_data[1], player_data[2])
        self.tournament.registered_player(p)

    def manage_players_by_name(self):
        datas = self.tournament.sorted_players_by_name()
        self.view.show_all_players(datas)

    def manage_rounds(self):
        rounds = self.tournament.rounds
        self.view.display_rounds(rounds)

    def manage_tournaments(self):
        tournaments = self.save_tournament()
        self.view.show_all_tournaments(tournaments)

    def save_tournament(self):
        tournament_datas = {
            "name": self.tournament.name,
            "start_date": self.tournament.start_date,
            "end_date": self.tournament.start_date,
        }

        with open(TounrnamentManager.json_file, "r") as json_file:
            try:
                data = json.load(json_file)
            except json.JSONDecodeError:
                data = []

            data.append(tournament_datas)

        with open(TounrnamentManager.json_file, 'w') as file:
            json.dump(data, file, indent=4)

        return data
