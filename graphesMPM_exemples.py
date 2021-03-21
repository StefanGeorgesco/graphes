from ordonnancement import *

donnees = [
    {
        "nom": "'RCP101_Partie1_Graphes_et_Algorithmes' (RCP101), page 102",
        "noms_tâches": ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l"],
        "durées": [1.0, 2.0, 1.0, 1.0, 2.0, 1.0, 2.0, 2.0, 1.0, 2.0, 1.0, 2.0],
        "liens": [
            ("a", "b", 1.0),
            ("a", "e", 1.0),
            ("b", "c", 2.0),
            ("c", "d", 1.0),
            ("c", "h", 1.0),
            ("d", "k", 1.0),
            ("e", "f", 2.0),
            ("f", "g", 1.0),
            ("f", "h", 1.0),
            ("g", "i", 2.0),
            ("h", "j", 2.0),
            ("i", "j", 1.0),
            ("j", "k", 2.0),
            ("k", "l", 1.0)
        ]
    },
    {
        "nom": "RCP101 - ED3 - Exerice 1",
        "noms_tâches": ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O"],
        "durées" : [70.0, 15.0, 25.0, 10.0, 60.0, 15.0, 70.0, 15.0, 5.0, 5.0, 30.0, 30.0, 40.0, 10.0, 15.0],
        "liens": [
            ("A", "C", 20.0),
            ("None", "D", 50.0),
            ("B", "E"),
            ("C", "E"),
            ("A", "F"),
            ("D", "F"),
            ("E", "G"),
            ("D", "H"),
            ("F", "I"),
            ("H", "J"),
            ("N", "J"),
            ("I", "K"),
            ("N", "K"),
            ("I", "L"),
            ("M", "L"),
            ("E", "M"),
            ("J", "M"),
            ("F", "N"),
            ("G", "O"),
            ("K", "O"),
            ("L", "O")
        ]
    },
    {
        "nom": "RCP101 - ED3 - Exerice 2",
        "noms_tâches": ["A", "B", "C", "D", "E", "F"],
        "durées" : [2.0, 2.0, 2.0, 4.0, 1.0, 2.0],
        "liens": [
            ("A", "C"),
            ("A", "D"),
            ("B", "E"),
            ("D", "E"),
            ("D", "F")
        ]
    }

]

graphes_MPM = {}
listes_taches = {}

for jeu_donnees in donnees:
    nom = jeu_donnees["nom"]
    noms_taches = jeu_donnees["noms_tâches"]
    durees = jeu_donnees["durées"]
    taches = [Tache(noms_taches[i], float(durees[i])) for i in range(len(noms_taches))]
    listes_taches[nom] = taches
    p = []
    for description_lien in jeu_donnees["liens"]:
        if len(description_lien) == 2:
            nom_t1, nom_t2 = description_lien
            p.append((taches[noms_taches.index(nom_t1)], taches[noms_taches.index(nom_t2)]))
        else:
            nom_t1, nom_t2, duree = description_lien
            p.append(
                (
                    None if nom_t1 == "None" else taches[noms_taches.index(nom_t1)],
                    taches[noms_taches.index(nom_t2)],
                    duree
                )
            )
    graphes_MPM[nom] = GrapheMPM(*taches, prec=p, nom=nom)
