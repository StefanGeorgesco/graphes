from ordonnancement import TacheMPM, TachePERT
from graphes_ordonnacement_exemples import graphes_MPM, graphes_PERT

print("\nCalcul par la méthode MPM :")
for nom in graphes_MPM.keys():
    graphe_ordonnancement = graphes_MPM[nom]
    print("\n" + repr(graphe_ordonnancement))
    print(graphe_ordonnancement)
    print("(Méthode MPM)\n")
    print(f"\tDate de fin : {graphe_ordonnancement.date_de_fin()}\n")
    print(f"\tTâches critiques : {graphe_ordonnancement.taches_critiques()}\n\n")
    taches = sorted(graphe_ordonnancement.taches(deb_fin=False), key=TacheMPM.__repr__)
    print("\t" + "".rjust(15), end="")
    for tache in taches:
        print(tache.nom()[:7].rjust(8), end="")
    print("\n\t" + "durée".ljust(15), end="")
    for tache in taches:
        print(repr(tache.duree()).rjust(8), end="")
    print("\n\t" + "plus tôt".ljust(15), end="")
    for tache in taches:
        print(repr(tache.plus_tot()).rjust(8), end="")
    print("\n\t" + "plus tard".ljust(15), end="")
    for tache in taches:
        print(repr(tache.plus_tard()).rjust(8), end="")
    print("\n\t" + "marge libre".ljust(15), end="")
    for tache in taches:
        print(repr(tache.marge_libre()).rjust(8), end="")
    print("\n\t" + "marge totale".ljust(15), end="")
    for tache in taches:
        print(repr(tache.marge_totale()).rjust(8), end="")
    print("\n")

print("\nCalcul par la méthode PERT :")
for nom in graphes_PERT.keys():
    graphe_ordonnancement = graphes_PERT[nom]
    print("\n" + repr(graphe_ordonnancement))
    print(graphe_ordonnancement)
    print("(Méthode PERT)\n")
    print(f"\tDate de fin : {graphe_ordonnancement.date_de_fin()}\n")
    print(f"\tTâches critiques : {graphe_ordonnancement.taches_critiques()}\n\n")
    taches = sorted(graphe_ordonnancement.taches(fictives=False), key=TachePERT.__repr__)
    print("\t" + "".rjust(15), end="")
    for tache in taches:
        print(tache.nom()[:7].rjust(8), end="")
    print("\n\t" + "durée".ljust(15), end="")
    for tache in taches:
        print(repr(tache.duree()).rjust(8), end="")
    print("\n\t" + "plus tôt".ljust(15), end="")
    for tache in taches:
        print(repr(tache.plus_tot()).rjust(8), end="")
    print("\n\t" + "plus tard".ljust(15), end="")
    for tache in taches:
        print(repr(tache.plus_tard()).rjust(8), end="")
    print("\n\t" + "marge libre".ljust(15), end="")
    for tache in taches:
        print(repr(tache.marge_libre()).rjust(8), end="")
    print("\n\t" + "marge totale".ljust(15), end="")
    for tache in taches:
        print(repr(tache.marge_totale()).rjust(8), end="")
    print("\n")
