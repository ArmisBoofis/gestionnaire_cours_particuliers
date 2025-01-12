#'!/Users/armand_malinvaud/Library/Mobile Documents/iCloud~is~workflow~my~workflows/Documents/gestionnaire_cours_particuliers/env/bin/python'

"""Main script of the tool, orchestrating the different parts of the app,
all implemented in different files."""

from menus import (
    choice_menu_wrapper,
    courses_menu,
    students_menu,
    houlry_rates_menu,
    stats_menu,
)

if __name__ == "__main__":
    print("Bienvenue dans le gestionnaire de cours particuliers.")

    user_continues = True

    def quit_manager():
        """Fonction quitting the program by setting <user_continues> to False."""
        global user_continues
        user_continues = False

    # Application loop
    while user_continues:
        choice_menu_wrapper(
            "Quelle action souhaitez-vous effectuer ?",
            [
                ("Gérer les cours", courses_menu),
                ("Gérer les élèves", students_menu),
                ("Gérer les taux horaire", houlry_rates_menu),
                ("Consulter les statistiques", stats_menu),
                ("Quitter le gestionnaire", quit_manager),
            ],
        )

    print("On se revoit prochainement pour des aventures de folie !")
