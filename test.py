import json
from datetime import datetime
import random


from _datetime import datetime

file_path = "data/players.json"

data =[
  {
    "first_name": "soso",
    "last_name": "Fall",
    "date_of_birth": "1984-05-24",
    "points": 0,
    "score": 0
  },
  {
    "first_name": "lala",
    "last_name": "faye",
    "date_of_birth": "1580-06-11",
    "points": 0,
    "score": 0
  },
  {
    "first_name": "gur",
    "last_name": "marius",
    "date_of_birth": "1999-08-04",
    "points": 0,
    "score": 0
  },
  {
    "first_name": "falla",
    "last_name": "fleur",
    "date_of_birth": "1960-09-16",
    "points": 0,
    "score": 0
  },
  {
    "first_name": "fofo",
    "last_name": "diagne",
    "date_of_birth": "1994-01-04",
    "points": 0,
    "score": 0
  },
  {
    "first_name": "mama",
    "last_name": "sene",
    "date_of_birth": "1980-05-10",
    "points": 0,
    "score": 0
  },
  {
    "first_name": "golbert",
    "last_name": "diagne",
    "date_of_birth": "1995-07-14",
    "points": 0,
    "score": 0
  },
  {
    "first_name": "talla",
    "last_name": "gaye",
    "date_of_birth": "2000-04-06",
    "points": 0,
    "score": 0
  }
]

with open(file_path, 'w') as file:
    json.dump(data, file, indent=2)

'''
print(datetime(1994, 5, 6).strftime('%Y-%m-%d'))

bob = {'a': 5, 'b': 6, 'c': 4}
print(bob.items())
print(bob.values())
print(bob.keys())
print(sum(bob.values()))

class myClass:

    def __init__(self, full_name):

        self.full_name = full_name


    def displayName(self):
        print("Le nom complet est :", self.full_name)


class other_class:

    def __init__(self, first_name, name):

        self.first_name = first_name

        self.name = name


def display_name(self):
    print(f"Nom complet : {self.first_name} {self.name}")


mots = ["chat", "chien", "oiseau", "poisson", "mouton"]

# Créer des paires à partir de la liste existante
paires_mots = [(mots[i], mots[i+1]) for i in range(0, len(mots)-1, 2)]

print("Paires de mots :", paires_mots)


def exemple_fonction(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Utilisation de la fonction avec des arguments de mots-clés
exemple_fonction(nom="Alice", age=30, ville="Wonderland")




# Fonction lambda pour calculer le carré d'un nombre
carre = lambda x: x**2

# Utilisation de la fonction lambda
resultat = carre(5)
print(resultat)  # Affiche 25



# Utilisation de map() avec une fonction lambda pour calculer les carrés d'une liste de nombres
nombres = [8, 1, 2, 3, 4, 5]
carres = map(lambda x: x**2, nombres)
print(list(carres))  # Affiche [1, 4, 9, 16, 25]

tri = sorted(nombres, key=lambda x: x, reverse=True)

print(tri)



for j in range(1, 5):
  print(j)


def generate_pairs(self, round_number):
  print(self.players)
  pairs = []
  for i in range(0, len(self.players) - 1, 2):
    pair = (self.players[i], self.players[i + 1])
    print(pair)
    for j in range(1, round_number):
      if pair in self.rounds[j - 1].pairs_per_round:
        print("pair dans la liste")
        pair = (self.players[i], self.players[i + 2])
        break
    self.rounds[round_number - 1].add_match(pair)
    pairs.append(pair)
  return pairs


pairs = [
    ({'first_name': 'falla', 'last_name': 'fleur', 'date_of_birth': '1960-09-16', 'points': 3, 'score': 3}, {'first_name': 'mama', 'last_name': 'sene', 'date_of_birth': '1980-05-10', 'points': 2, 'score': 2}),
    ({'first_name': 'soso', 'last_name': 'Fall', 'date_of_birth': '1984-05-24', 'points': 2, 'score': 2}, {'first_name': 'fofo', 'last_name': 'diagne', 'date_of_birth': '1994-01-04', 'points': 2, 'score': 2}),
    ({'first_name': 'gur', 'last_name': 'marius', 'date_of_birth': '1999-08-04', 'points': 1, 'score': 1}, {'first_name': 'lala', 'last_name': 'faye', 'date_of_birth': '1580-06-11', 'points': 0, 'score': 0}),
    ({'first_name': 'talla', 'last_name': 'gaye', 'date_of_birth': '2000-04-06', 'points': 1, 'score': 1}, {'first_name': 'golbert', 'last_name': 'diagne', 'date_of_birth': '1995-07-14', 'points': 1, 'score': 1})
]

new_pairs = [({k: v for k, v in item[0].items() if k not in ['date_of_birth', 'points', 'score']},
                     {k: v for k, v in item[1].items() if k not in ['date_of_birth', 'points', 'score']}) for item in pairs]

pair = ({'first_name': 'gur', 'last_name': 'marius', 'date_of_birth': '1999-08-04', 'points': 3, 'score': 3}, {'first_name': 'lala', 'last_name': 'faye', 'date_of_birth': '1580-06-11', 'points': 2, 'score': 2})
a = {k: v for k, v in pair[0].items() if k not in ['date_of_birth', 'points', 'score']}, {k: v for k, v in pair[1].items() if k not in ['date_of_birth', 'points', 'score']}
print(a)
print(new_pairs)

if a in new_pairs:
    print('bon')
    
'''

sorted_data = sorted(data, key=lambda x: x['first_name'])

for item in sorted_data:
    print(item)
