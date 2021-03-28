from ordonnancement import Tache
from graphes_ordonnacement_exemples import graphes_MPM, graphes_PERT

for nom in graphes_MPM.keys():
    graphe_ordonnancement = graphes_MPM[nom]
    print("\n" + repr(graphe_ordonnancement))
    print(graphe_ordonnancement)
    print(f"\tDate de fin : {graphe_ordonnancement.date_de_fin()}\n")
    print(f"\tTâches critiques : {graphe_ordonnancement.taches_critiques()}\n\n")
    taches = sorted(graphe_ordonnancement.taches(deb_fin=False), key=Tache.__repr__)
    print("\t" + "".ljust(15), end="")
    for tache in taches:
        print(tache.nom()[:4].ljust(5), end="")
    print("\n\t" + "durée".ljust(15), end="")
    for tache in taches:
        print(repr(tache.duree()).ljust(5), end="")
    print("\n\t" + "plus tôt".ljust(15), end="")
    for tache in taches:
        print(repr(tache.plus_tot()).ljust(5), end="")
    print("\n\t" + "plus tard".ljust(15), end="")
    for tache in taches:
        print(repr(tache.plus_tard()).ljust(5), end="")
    print("\n\t" + "marge libre".ljust(15), end="")
    for tache in taches:
        print(repr(tache.marge_libre()).ljust(5), end="")
    print("\n\t" + "marge totale".ljust(15), end="")
    for tache in taches:
        print(repr(tache.marge_totale()).ljust(5), end="")
    print("\n")

for nom in graphes_PERT.keys():
    graphe_ordonnancement = graphes_PERT[nom]
    print("\n" + repr(graphe_ordonnancement))
    for arc in graphe_ordonnancement.arcs():
        print(f"arc : {arc}")
        print(f"départ : {arc.depart()}")
        print(f"arrivée : {arc.arrivee()}")
        print(f"durée : {arc.valuation()}")
        print()
    print(f"\nnombre d'événements : {graphe_ordonnancement.ordre()}")
    print(f"\nnombre de taches : {graphe_ordonnancement.taille()}")
