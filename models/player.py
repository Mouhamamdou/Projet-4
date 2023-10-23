from _datetime import datetime
import random


class Player:

    def __init__(self, first_name, last_name, date_of_birth, score=0, points=0):
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.score = score
        self.points = points

    def to_dict(self):
        return {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'date_of_birth': self.date_of_birth.strftime('%Y-%m-%d'),
            'points': self.points,
            'score': self.score
        }

    @classmethod
    def add_player(cls, first_name, last_name, date_of_birth):
        p = Player(first_name, last_name, date_of_birth)
        return p

    def scored(self):
        self.score = random.randint(1, 5)
        return self.score

    def __lt__(self, other):
        return self.score < other.score


if __name__ == "__main__":
    joueur1 = Player("momo", "gaye", datetime(1994,8,14))

    joueur2 = Player("mister","diop",datetime(1800,5,14))

    print(joueur2.score)
    joueur2.scored()
    print(joueur2.score)





