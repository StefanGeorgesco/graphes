from graphesMPM_exemples import graphes_MPM, Tache

for nom in graphes_MPM.keys():
    graphe_MPM = graphes_MPM[nom]
    print(graphe_MPM)
    print(f"\tDate de fin : {graphe_MPM.date_de_fin()}\n")
    print(f"\tTâches critiques : {graphe_MPM.taches_critiques()}\n\n")
    taches = sorted(graphe_MPM.getTaches(deb_fin=False), key=Tache.__repr__)
    print("\t" + "".ljust(15), end="")
    for tache in taches:
        print(tache.getNom()[:4].ljust(5), end="")
    print("\n\t" + "durée".ljust(15), end="")
    for tache in taches:
        print(repr(tache.getDuree()).ljust(5), end="")
    print("\n\t" + "plus tôt".ljust(15), end="")
    for tache in taches:
        print(repr(tache.getPlus_tot()).ljust(5), end="")
    print("\n\t" + "plus tard".ljust(15), end="")
    for tache in taches:
        print(repr(tache.getPlus_tard()).ljust(5), end="")
    print("\n\t" + "marge libre".ljust(15), end="")
    for tache in taches:
        print(repr(tache.getMarge_libre()).ljust(5), end="")
    print("\n\t" + "marge totale".ljust(15), end="")
    for tache in taches:
        print(repr(tache.marge_totale()).ljust(5), end="")
