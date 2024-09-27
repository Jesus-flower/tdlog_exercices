"""
Une méthode agile est une approche itérative et collaborative pour
mener à bien un projet.
Elle génère un produit de haute qualité tout en prenant en compte
l’évolution des besoins des clients.

La méthode la plus connue est Scrum.

Au début d'un projet un « backlog », ensemble de tache à réaliser
est défini avec le client.
Ce « backlog » évolue dans le temps en fonction du besoin de client.
On peut y rajouter des taches comme on peut en enlever.

Durant le projet, une réunion avec l'équipe technique et l'équipe
opérationnelle est organisée à chaque
« sprint » (unité de temps composé de quelques semaines).
Lors cette réunion, le client valide ou non les taches
qui ont été réalisées durant la période de « sprint ».

Dans ce challenge, vous devez déterminer si à la date de la livraison
finale, le client obtient la totalité de son produit.


Format des données

Entrée
Ligne 1 : un entier N correspondant au nombre de sprints(réunion).
Ligne 2 : un entier T correspondant au nombre de taches dans le « backlog »
        initial.
Ligne 3 à N+2 : un entier V et un entier U séparés par un espace où V est
le nombre de taches validées
et U le nombre de taches à ajouter (si U est positif) ou à supprimer
(si U est négatif) dans le « backlog ».

Sortie
La chaîne OK si le backlog est vide. Sinon retourner la chaîne KO.

"""
import unittest

def processLines(lines) -> str:
    # Lire le nombre de sprints et le nombre de tâches initiales
    N = int(lines[0])
    T = int(lines[1])

    # On parcourt les lignes correspondant aux réunions de sprint
    for i in range(2, N + 2):
        V, U = map(int, lines[i].split())  # Lire V (validées) et U (ajoutées/supprimées)
        T -= V  # Soustraire le nombre de tâches validées du backlog
        T += U  # Ajouter ou retirer des tâches selon U

    # Si le backlog est vide, on retourne "OK", sinon "KO"
    return "OK" if T == 0 else "KO"


class TestExo3(unittest.TestCase):

    def test_input_1(self):
        with open("sample/input1.txt") as input1:
            lines = input1.readlines()

        with open("sample/output1.txt") as output1:
            expected = output1.read()

        self.assertEqual(expected.strip(), processLines([line.strip() for line in lines]))

    def test_input_2(self):
        with open("sample/input2.txt") as input2:
            lines = input2.readlines()

        with open("sample/output2.txt") as output2:
            expected = output2.read()

        self.assertEqual(expected.strip(), processLines([line.strip() for line in lines]))


