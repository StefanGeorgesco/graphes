from graphes import *

donnees_graphes_orientes = [
    {
        "nom": "'RCP101_Partie1_Graphes_et_Algorithmes' (RCP101), pages 25/27/33",
        "noms_sommets": ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17",
                         "18", "19"],
        "liens": [
            ("1", "2", 1),
            ("1", "5", 1),
            ("2", "1", 1),
            ("2", "3", 1),
            ("3", "2", 1),
            ("3", "4", 1),
            ("4", "3", 1),
            ("4", "9", 1),
            ("5", "1", 1),
            ("5", "10", 1),
            ("6", "5", 1),
            ("6", "7", 1),
            ("7", "2", 1),
            ("7", "13", 2),
            ("8", "3", 1),
            ("8", "7", 1),
            ("8", "9", 1),
            ("9", "4", 1),
            ("9", "15", 1),
            ("10", "5", 1),
            ("10", "16", 1),
            ("11", "10", 1),
            ("11", "17", 1),
            ("12", "6", 1),
            ("12", "11", 1),
            ("13", "12", 1),
            ("13", "14", 1),
            ("13", "18", 1),
            ("14", "8", 1),
            ("14", "15", 1),
            ("15", "9", 1),
            ("15", "19", 1),
            ("16", "10", 1),
            ("16", "17", 1),
            ("17", "16", 1),
            ("17", "18", 1),
            ("18", "17", 1),
            ("18", "19", 1),
            ("19", "15", 1),
            ("19", "18", 1)
        ],
        "sommet_départ": "1"
    },
    {
        "nom": "'RCP101_Partie1_Graphes_et_Algorithmes' (RCP101), page 74",
        "noms_sommets": ["1", "2", "3", "4", "5", "6", "7", "8"],
        "liens": [
            ("1", "2", 8),
            ("1", "3", 1),
            ("2", "3", 1),
            ("3", "4", 2),
            ("3", "5", 1),
            ("4", "2", 3),
            ("4", "8", 3),
            ("5", "6", 1),
            ("6", "4", 1),
            ("6", "7", 1),
            ("6", "8", 3),
            ("7", "8", 1)
        ],
        "sommet_départ": "1"
    },
    {
        "nom": "'RCP101_Partie1_Graphes_et_Algorithmes' (RCP101), page 85",
        "noms_sommets": ["1", "2", "3", "4", "5", "6", "7", "8", "9"],
        "liens": [
            ("1", "2", 1),
            ("1", "3", -2),
            ("1", "4", 2),
            ("2", "4", 3),
            ("2", "6", 1),
            ("2", "7", 5),
            ("3", "4", -1),
            ("3", "5", 2),
            ("4", "8", 4),
            ("5", "7", 1),
            ("6", "9", 1),
            ("7", "4", 3),
            ("7", "6", -1),
            ("7", "8", -3),
            ("9", "8", 12)
        ],
        "sommet_départ": "1"
    },
    {
        "nom": "'RCP101_Partie1_Graphes_et_Algorithmes' (RCP101), page 92",
        "noms_sommets": ["A", "B", "C", "D", "E", "F"],
        "liens": [
            ("A", "B", 4),
            ("A", "E", 3),
            ("B", "C", -3),
            ("B", "E", -2),
            ("C", "F", -2),
            ("D", "B", 5),
            ("D", "C", 2),
            ("E", "D", -1),
            ("F", "D", 1),
            ("F", "E", 4)
        ],
        "sommet_départ": "A"
    },
    {
        "nom": "'RCP101_Partie1_Graphes_et_Algorithmes' (RCP101), page 112 - Méthode MPM - Dates au plus tôt et "
               "chemin critique",
        "noms_sommets": ["début", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "fin"],
        "liens": [
            ("début", "a", 0),
            ("a", "b", -1),
            ("a", "e", -1),
            ("b", "c", -2),
            ("c", "d", -1),
            ("c", "h", -1),
            ("d", "k", -1),
            ("e", "f", -2),
            ("f", "g", -1),
            ("f", "h", -1),
            ("g", "i", -2),
            ("h", "j", -2),
            ("i", "j", -1),
            ("j", "k", -2),
            ("k", "l", -1),
            ("l", "fin", -2)
        ],
        "sommet_départ": "début"
    },
    {
        "nom": "'RCP101_Partie1_Graphes_et_Algorithmes' (RCP101), page 112 - Méthode MPM - Dates au plus tard",
        "noms_sommets": ["début", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "fin"],
        "liens": [
            ("a", "début", 0),
            ("b", "a", -1),
            ("e", "a", -1),
            ("c", "b", -2),
            ("d", "c", -1),
            ("h", "c", -1),
            ("k", "d", -1),
            ("f", "e", -2),
            ("g", "f", -1),
            ("h", "f", -1),
            ("i", "g", -2),
            ("j", "h", -2),
            ("j", "i", -1),
            ("k", "j", -2),
            ("l", "k", -1),
            ("fin", "l", -2 + 12)
        ],
        "sommet_départ": "fin"
    },
    {
        "nom": "RCP101 - ED1 - Exercice 1",
        "noms_sommets": ["A", "B", "C", "D", "E", "F"],
        "liens": [
            ("A", "B", 1),
            ("A", "F", 1),
            ("B", "A", 1),
            ("B", "B", 1),
            ("B", "C", 1),
            ("B", "E", 1),
            ("C", "D", 1),
            ("D", "C", 1),
            ("E", "B", 1),
            ("E", "D", 1),
            ("E", "E", 1),
            ("E", "F", 1),
            ("F", "A", 1),
            ("F", "C", 1)
        ],
        "sommet_départ": "A"
    },
    {
        "nom": "RCP101 - ED1 - Exercice 2 - Question 1",
        "noms_sommets": ["A+", "A-", "B+", "B-", "C+", "C-", "D+", "D-", "E+", "E-"],
        "liens": [
            ("A+", "B+", 1),
            ("A+", "C-", 1),
            ("A-", "B-", 1),
            ("A-", "E-", 1),
            ("B+", "A+", 1),
            ("B-", "A-", 1),
            ("B-", "D+", 1),
            ("C+", "A-", 1),
            ("C+", "D+", 1),
            ("C-", "D-", 1),
            ("D+", "C+", 1),
            ("D+", "E+", 1),
            ("D-", "B+", 1),
            ("D-", "C-", 1),
            ("E+", "A+", 1),
            ("E-", "D-", 1)
        ],
        "sommet_départ": "B-"
    },
    {
        "nom": "RCP101 - ED1 - Exercice 2 - Question 2",
        "noms_sommets": ["A+", "A-", "B+", "B-", "C+", "C-", "D+", "D-", "E+", "E-", "F+", "F-"],
        "liens": [
            ("A+", "B+", 1),
            ("A+", "C-", 1),
            ("A+", "F+", 1),
            ("A-", "B-", 1),
            ("A-", "E-", 1),
            ("B+", "A+", 1),
            ("B-", "A-", 1),
            ("B-", "D+", 1),
            ("C+", "A-", 1),
            ("C+", "D+", 1),
            ("C-", "D-", 1),
            ("D+", "C+", 1),
            ("D+", "E+", 1),
            ("D-", "B+", 1),
            ("D-", "C-", 1),
            ("D-", "F-", 1),
            ("E+", "A+", 1),
            ("E-", "D-", 1),
            ("F+", "D+", 1),
            ("F-", "A-", 1)
        ],
        "sommet_départ": "B-"
    },
    {
        "nom": "RCP101 - ED2 - Exercice 1",
        "noms_sommets": [
            "T1A0",
            "T2A0", "T2A1",
            "T3A0", "T3A1", "T3A2",
            "T4A0", "T4A1", "T4A2", "T4A3",
            "T5A0", "T5A1", "T5A2", "T5A3", "T5A4",
            "T6"
        ],
        "liens": [
            ("T1A0", "T2A0", 6000 + 13000),
            ("T1A0", "T2A1", 6000),
            ("T2A0", "T3A0", 6000 + 13000),
            ("T2A0", "T3A1", 6000),
            ("T2A1", "T3A0", 10000 + 25000),
            ("T2A1", "T3A2", 10000),
            ("T3A0", "T4A0", 6000 + 13000),
            ("T3A0", "T4A1", 6000),
            ("T3A1", "T4A0", 10000 + 25000),
            ("T3A1", "T4A2", 10000),
            ("T3A2", "T4A0", 15000 + 45000),
            ("T3A2", "T4A3", 15000),
            ("T4A0", "T5A0", 6000 + 13000),
            ("T4A0", "T5A1", 6000),
            ("T4A1", "T5A0", 10000 + 25000),
            ("T4A1", "T5A2", 10000),
            ("T4A2", "T5A0", 15000 + 45000),
            ("T4A2", "T5A3", 15000),
            ("T4A3", "T5A0", 23000 + 47500),
            ("T4A3", "T5A4", 23000),
            ("T5A0", "T6", 6000 - 37000),
            ("T5A1", "T6", 10000 - 25000),
            ("T5A2", "T6", 15000 - 5000),
            ("T5A3", "T6", 23000 - 2500),
            ("T5A4", "T6", 35000)
        ],
        "sommet_départ": "T1A0"
    },
    {
        "nom": "RCP101 - ED2 - Exercice 2",
        "noms_sommets": ["x1", "x2", "x3", "x4", "x5", "x6"],
        "liens": [
            ("x1", "x2", 2),
            ("x1", "x3", 6),
            ("x1", "x4", 9),
            ("x2", "x5", 1),
            ("x3", "x2", 1),
            ("x3", "x6", 6),
            ("x4", "x3", 1),
            ("x4", "x6", 1),
            ("x5", "x3", 2),
            ("x5", "x6", 9)
        ],
        "sommet_départ": "x1"
    },
    {
        "nom": "RCP101 - ED2 - Exercice 3 questions 1 et 2",
        "noms_sommets": ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"],
        "liens": [
            ("1", "2", 3),
            ("1", "3", 5),
            ("1", "4", 4),
            ("2", "3", 3),
            ("2", "5", 8),
            ("3", "4", 2),
            ("3", "6", 7),
            ("3", "7", 3),
            ("4", "7", 4),
            ("5", "3", 2),
            ("5", "8", 5),
            ("6", "8", 2),
            ("6", "9", 9),
            ("7", "9", 3),
            ("8", "10", 1),
            ("9", "10", -5)
        ],
        "sommet_départ": "1"
    },
    {
        "nom": "RCP101 - ED2 - Exercice 3 question 3",
        "noms_sommets": ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"],
        "liens": [
            ("1", "2", -3),
            ("1", "3", -5),
            ("1", "4", -4),
            ("2", "3", -3),
            ("2", "5", -8),
            ("3", "4", -2),
            ("3", "6", -7),
            ("3", "7", -3),
            ("4", "7", -4),
            ("5", "3", -2),
            ("5", "8", -5),
            ("6", "8", -2),
            ("6", "9", -9),
            ("7", "9", -3),
            ("8", "10", -1),
            ("9", "10", 5)
        ],
        "sommet_départ": "1"
    },
    {
        "nom": "RCP101 - ED2 - Exercice 4",
        "noms_sommets": ["A", "B", "C", "D", "E"],
        "liens": [
            ("A", "C", 3),
            ("A", "D", 2),
            ("B", "D", -2),
            ("B", "E", 5),
            ("C", "B", 2),
            ("C", "D", -1),
            ("D", "C", 2),
            ("D", "E", 3)
        ],
        "sommet_départ": "A"
    }
]
donnees_graphes_non_orientes = [
    {
        "nom": "Exemple de graphe non orienté",
        "noms_sommets": ["A", "B", "C", "D", "E", "F"],
        "liens": [
            ("A", "B"),
            ("A", "C"),
            ("A", "F"),
            ("B", "E"),
            ("C", "E"),
            ("C", "D"),
            ("D", "E"),
            ("D", "F")
        ]
    }
]

graphes_orientes = {}
listes_sommets_graphes_orientes = {}
sommets_depart_graphes_orientes = {}

for jeu_donnees_graphes_orientes in donnees_graphes_orientes:
    nom = jeu_donnees_graphes_orientes["nom"]
    noms_sommets = jeu_donnees_graphes_orientes["noms_sommets"]
    sommets = [Sommet(nom) for nom in noms_sommets]
    listes_sommets_graphes_orientes[nom] = sommets
    graphe = GrapheOriente(*sommets, commentaire=nom)
    for nom1, nom2, poids in jeu_donnees_graphes_orientes["liens"]:
        graphe.lier(sommets[noms_sommets.index(nom1)], sommets[noms_sommets.index(nom2)], poids)
    graphes_orientes[nom] = graphe
    sommets_depart_graphes_orientes[nom] = sommets[noms_sommets.index(jeu_donnees_graphes_orientes["sommet_départ"])]

graphes_non_orientes = {}
listes_sommets_graphes_non_orientes = {}

for jeu_donnees_graphes_non_orientes in donnees_graphes_non_orientes:
    nom = jeu_donnees_graphes_non_orientes["nom"]
    noms_sommets = jeu_donnees_graphes_non_orientes["noms_sommets"]
    sommets = [Sommet(nom) for nom in noms_sommets]
    listes_sommets_graphes_non_orientes[nom] = sommets
    graphe = GrapheNonOriente(*sommets, commentaire=nom)
    for nom1, nom2 in jeu_donnees_graphes_non_orientes["liens"]:
        graphe.lier(sommets[noms_sommets.index(nom1)], sommets[noms_sommets.index(nom2)])
    graphes_non_orientes[nom] = graphe
