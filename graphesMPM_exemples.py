from ordonnancement import *

donnees = [
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
            p.append((taches[noms_taches.index(nom_t1)], taches[noms_taches.index(nom_t2)], duree))
    graphes_MPM[nom] = GrapheMPM(*taches, prec=p, nom=nom)
