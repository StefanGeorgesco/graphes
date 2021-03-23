from graphesMPM_exemples import graphes_MPM

for nom in graphes_MPM.keys():
    graphe_MPM = graphes_MPM[nom]
    print(graphe_MPM)
    print(f"Date de fin : {graphe_MPM.date_de_fin()}")
    print(f"Taches critiques : {graphe_MPM.taches_critiques()}")