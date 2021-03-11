from graphes_exemples import graphes_orientes, listes_sommets_graphes_orientes

def get_graphes_orientes(nom):
    index = list(
        map(
            lambda g: g.getCommentaire(),
            graphes_orientes
        )
    ).index(nom)
    return graphes_orientes[index], listes_sommets_graphes_orientes[index]

def chemin(pere, s1, s2):
    if s1 == s2:
        return []
    return chemin(pere, s1, pere[s2]) + [(pere[s2], s2)]

graphe, sommets = get_graphes_orientes("RCP101 - ED2 - Exercice 1")
print(graphe.getCommentaire())
T1A0 = sommets[0]
T6 = sommets[15]
pi, pere = graphe.bellman(T1A0)
print(f"plus court chemin de {T1A0} à {T6}", chemin(pere, T1A0, T6))
print("pi :", pi)
print("père :", pere)
print()

graphe, sommets = get_graphes_orientes("RCP101 - ED2 - Exercice 2")
print(graphe.getCommentaire())
x1, x2, x3, x4, x5, x6 = sommets
pi, pere = graphe.dijkstra(x1)
print("pi :", pi)
print("père :", pere)
print()
