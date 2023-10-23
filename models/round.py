from datetime import datetime
from models.match import Match


class Round:

    def __init__(self, round_name):
        self.round_name = round_name
        self.pairs_per_round = []
        self.start_date = None
        self.end_date = None

    def add_match(self, match):
        self.pairs_per_round.append(match)
        return self.pairs_per_round

    def start_round(self):
        self.start_date = datetime.now()
        return self.start_date

    def end_round(self):
        self.end_date = datetime.now()
        return self.end_date

    def __str__(self):
        return f"{self.round_name}===>{self.pairs_per_round}"


if __name__ == "__main__":
    pass

'''
round = Round("Round 1")
print(round.round_name)
print(round.start_round())
'''
