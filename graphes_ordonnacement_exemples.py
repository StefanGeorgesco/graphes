from ordonnancement import *

donnees = [
    {
        "nom": "'RCP101_Partie1_Graphes_et_Algorithmes' (RCP101), page 102",
        "noms_tâches": ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l"],
        "durées": [1.0, 2.0, 1.0, 1.0, 2.0, 1.0, 2.0, 2.0, 1.0, 2.0, 1.0, 2.0],
        "liens": [
            ("a", "b"),
            ("a", "e"),
            ("b", "c"),
            ("c", "d"),
            ("c", "h"),
            ("d", "k"),
            ("e", "f"),
            ("f", "g"),
            ("f", "h"),
            ("g", "i"),
            ("h", "j"),
            ("i", "j"),
            ("j", "k"),
            ("k", "l")
        ]
    },
    {
        "nom": "RCP101 - ED3 - Exerice 1",
        "noms_tâches": ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O"],
        "durées": [70.0, 15.0, 25.0, 10.0, 60.0, 15.0, 70.0, 15.0, 5.0, 5.0, 30.0, 30.0, 40.0, 10.0, 15.0],
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
        "durées": [2.0, 2.0, 2.0, 4.0, 1.0, 2.0],
        "liens": [
            ("A", "C"),
            ("A", "D"),
            ("B", "E"),
            ("D", "E"),
            ("D", "F")
        ]
    },
    {
        "nom": "RCP101 - ED3 - Exerice 3",
        "noms_tâches": ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K"],
        "durées": [4.0, 6.0, 2.0, 6.0, 1.0, 4.0, 3.0, 5.0, 6.0, 3.0, 4.0],
        "liens": [
            ("A", "B"),
            ("None", "C", 2.0),
            ("B", "E"),
            ("C", "F"),
            ("B", "G"),
            ("D", "G"),
            ("E", "H"),
            ("G", "H"),
            ("B", "I"),
            ("F", "I"),
            ("I", "J"),
            ("H", "J"),
            ("I", "K"),
            ("H", "K")
        ]
    },
    {
        "nom": "RCP101 - Annale 2018-2919 S2",
        "noms_tâches": ["a", "b", "c", "d", "e", "f", "g"],
        "durées": [3.0, 4.0, 2.0, 8.0, 5.0, 1.0, 1.0],
        "liens": [
            ("None", "a", 2.0),
            ("b", "d"),
            ("c", "d"),
            ("b", "e"),
            ("a", "f"),
            ("d", "f"),
            ("e", "f"),
            ("d", "g")
        ]
    }

]

graphes_MPM = {}
listes_taches_MPM = {}
graphes_PERT = {}
listes_taches_PERT = {}

for jeu_donnees in donnees:
    nom = jeu_donnees["nom"]
    noms_taches = jeu_donnees["noms_tâches"]
    durees = jeu_donnees["durées"]
    taches_MPM = [TacheMPM(noms_taches[i], float(durees[i])) for i in range(len(noms_taches))]
    listes_taches_MPM[nom] = taches_MPM
    taches_PERT = [TachePERT(noms_taches[i], float(durees[i])) for i in range(len(noms_taches))]
    listes_taches_PERT[nom] = taches_PERT
    p_MPM = []
    p_PERT = []
    for description_lien in jeu_donnees["liens"]:
        if len(description_lien) == 2:
            nom_t1, nom_t2 = description_lien
            p_MPM.append((taches_MPM[noms_taches.index(nom_t1)], taches_MPM[noms_taches.index(nom_t2)]))
            p_PERT.append((taches_PERT[noms_taches.index(nom_t1)], taches_PERT[noms_taches.index(nom_t2)]))
        else:
            nom_t1, nom_t2, duree = description_lien
            p_MPM.append(
                (
                    None if nom_t1 == "None" else taches_MPM[noms_taches.index(nom_t1)],
                    taches_MPM[noms_taches.index(nom_t2)],
                    duree
                )
            )
            p_PERT.append(
                (
                    None if nom_t1 == "None" else taches_PERT[noms_taches.index(nom_t1)],
                    taches_PERT[noms_taches.index(nom_t2)],
                    duree
                )
            )
    graphes_MPM[nom] = GrapheMPM(*taches_MPM, prec=p_MPM, nom=nom)
    graphes_PERT[nom] = GraphePERT(*taches_PERT, prec=p_PERT, nom=nom)
