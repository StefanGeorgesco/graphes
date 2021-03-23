from graphesMPM_exemples import graphes_MPM

for nom in graphes_MPM.keys():
    graphe_MPM = graphes_MPM[nom]
    print(graphe_MPM)
    print(f"\tDate de fin : {graphe_MPM.date_de_fin()}\n")
    print(f"\tTâches critiques : {graphe_MPM.taches_critiques()}\n\n")