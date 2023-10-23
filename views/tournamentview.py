from datetime import datetime


class TournamentView:

    def prompt_create_tournament(self):
        print("Créer un tournoi")
        name = input("nom du tournoi : ")
        place = input("lieu où se déroule le tournoi : ")
        start_date = datetime.strptime(input("date de démarrage du tournoi au format aaaa-mm-dd : "), '%Y-%m-%d')
        end_date = datetime.strptime(input("date de fin du tournoi au format aaaa-mm-dd : "), '%Y-%m-%d')
        # nbr_of_rounds = input("nombre de tours : ")

        return name, place, start_date, end_date

    def prompt_add_player(self):
        print("Ajouter un joueur dans le tournoi")
        first_name = input("prenom : ")
        last_name = input("nom : ")
        date_of_birh = datetime.strptime(input("date de naissance au format aaaa-mm-dd : "), '%Y-%m-%d')

        return first_name, last_name, date_of_birh

    def display_rounds(self, rounds):
        print()
        print("les tours : ")
        for round in rounds:
            print(round)

    def show_all_players(self, datas):
        print()
        print("Tous les joueurs par ordre alphabétique : ")
        for item in datas:
            print(item)

    def show_all_tournaments(self, tournaments):
        print()
        print("les tournois : ")
        for item in tournaments:
            print(item)
