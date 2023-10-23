from controllers.tournamentmanager import TounrnamentManager


def main():

    controller = TounrnamentManager()

    print("Menu principal :")
    print("1 - Ajouter un joueur ")
    print("2- Créer un tournoi")
    choice = input("Faites un choix: ")
    if choice == "1":
        controller.add_player()
        while True:
            response = input("Vous voulez ajouter un autre joueur dans le tournoi ? (oui/non): ")
            if response != 'oui':
                break
            controller.add_player()
    elif choice == "2":
        controller.create_tournament()

        # start the first round
        controller.throw_round(1)

        # start the second round
        controller.throw_round(2)

        # start the third round
        controller.throw_round(3)

        # start the fourth round
        controller.throw_round(4)

        # Display the round and the matches
        controller.manage_rounds()

        # display the sorted players by name
        controller.manage_players_by_name()

        # display the tournaments
        controller.manage_tournaments()
    else:
        print("choix invalide")


if __name__ == "__main__":
    main()
