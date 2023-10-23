from models.player import Player
from datetime import datetime
import json
import random


class Match:

    def __init__(self, player1, player2):
        self.player1: Player = player1
        self.player2: Player = player2
        self.winner: Player = self.player1
        self.looser: Player = self.player2
        self.json_file = "data/players.json"

    def play_match(self):
        self.player1.score = random.choice([0, 1])
        self.player2.score = 1 - self.player1.score
        return self.player1.score, self.player1.score

    def result_match(self):
        if self.player1 < self.player2:
            self.winner = self.player2
            self.winner.points += 1
            self.looser = self.player1
            print(f'the winner {self.winner.first_name}')
            print(f'the looser {self.looser.first_name}')
        elif self.player1 > self.player2:
            self.winner = self.player1
            self.winner.points += 1
            self.looser = self.player2
            print(f'the winner {self.winner.first_name}')
            print(f'the looser {self.looser.first_name}')

    def update_json_file(self):
        with open(self.json_file, 'r') as file:
            datas = json.load(file)
        for player in datas:
            if player['first_name'] == self.winner.first_name:
                player['score'] += self.winner.score
                player['points'] += self.winner.points
                break
        with open(self.json_file, 'w') as file:
            json.dump(datas, file, indent=2)

    def __str__(self):
        return f"{self.player1.first_name} vs {self.player2.first_name}"


if __name__ == "__main__":
    play1 = Player("moussa", "sall", datetime(1984, 5, 24))

    play2 = Player("ousmane", "diagne", datetime(1580, 6, 11))

    match1 = Match(play1, play2)
    print(match1)

    match1.play_match()
    print(f'result : {play1.score} - {play2.score} ')

    match1.result_match()
    print(f'points ---> {play1.first_name}: {play1.points} , {play2.first_name}: {play2.points} ')

    match1.update_json_file()

