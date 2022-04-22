from graphes import *

S1 = Sommet("1")
S2 = Sommet("2")
S3 = Sommet("3")
S4 = Sommet("4")
S5 = Sommet("5")
S6 = Sommet("6")
S7 = Sommet("7")
S8 = Sommet("8")

graphe = GrapheOriente(S1, S2, S3, S4, S5, S6, S7, S8)

graphe.lier(S1, S2, 8)
graphe.lier(S1, S3, 1)
graphe.lier(S2, S3, 1)
graphe.lier(S3, S4, 2)
graphe.lier(S3, S5, 1)
graphe.lier(S4, S2, 3)
graphe.lier(S4, S8, 3)
graphe.lier(S5, S6, 1)
graphe.lier(S6, S4, 1)
graphe.lier(S6, S7, 1)
graphe.lier(S6, S8, 3)
graphe.lier(S7, S8, 1)

pi, pere = graphe.dijkstra(S1)

print("graphe :\n", graphe)
print("pi :", pi)
print("pere :", pere)


def chemin(s1, s2):
    if s1 == s2:
        return []
    else:
        return chemin(s1, pere[s2]) + [(pere[s2], s2)]


print(f"chemin de {S1} à {S2} : {chemin(S1, S2)}")
print(f"longueur du chemin de {S1} à {S2} : {pi[S2]}")
