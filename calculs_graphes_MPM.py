from graphesMPM_exemples import graphes_MPM, Tache

for nom in graphes_MPM.keys():
    graphe_MPM = graphes_MPM[nom]
    print(graphe_MPM)
    print(f"\tDate de fin : {graphe_MPM.date_de_fin()}\n")
    print(f"\tTâches critiques : {graphe_MPM.taches_critiques()}\n\n")
    for tache in sorted(graphe_MPM.getTaches(), key=Tache.__repr__):
        print(f"\tTâche {tache}, marge libre : {tache.getMarge_libre()}, marge totale : {tache.marge_totale()}")