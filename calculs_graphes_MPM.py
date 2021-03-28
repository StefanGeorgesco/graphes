from graphesMPM_exemples import graphes_MPM, TacheMPM

for nom in graphes_MPM.keys():
    graphe_MPM = graphes_MPM[nom]
    print("\n" + repr(graphe_MPM))
    print(graphe_MPM)
    print(f"\tDate de fin : {graphe_MPM.date_de_fin()}\n")
    print(f"\tTâches critiques : {graphe_MPM.taches_critiques()}\n\n")
    taches = sorted(graphe_MPM.taches(deb_fin=False), key=TacheMPM.__repr__)
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
