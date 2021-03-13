from graphes_exemples import graphes_orientes, listes_sommets_graphes_orientes

def get_graphes_orientes(nom):
    return graphes_orientes[nom], listes_sommets_graphes_orientes[nom]

def chemin(pere, s1, s2):
    if s1 == s2:
        return []
    return chemin(pere, s1, pere[s2]) + [(pere[s2], s2)]

def chemin2(P, s1, s2):
    if s1 == s2:
        return []
    return chemin2(P, s1, P[s1, s2]) + [(P[s1, s2], s2)]

def afficheMatrice(sommets, M):
    M = dict(M)
    print("\t" + "".ljust(5), end="")
    for j in sommets:
        print(repr(j).ljust(5), end="")
    print()
    for i in sommets:
        print("\t" + repr(i).ljust(5), end="")
        for j in sommets:
            print(repr(M[i, j]).ljust(5), end="")
        print()
    print()

graphe, sommets = get_graphes_orientes("RCP101 - ED2 - Exercice 1")
print(graphe.getCommentaire())
print()
T1A0 = sommets[0]
T6 = sommets[15]
pi, pere = graphe.bellman(T1A0)
print(f"plus court chemin de {T1A0} à {T6} :", chemin(pere, T1A0, T6))
print("pi :", pi)
print("père :", pere)
print()

graphe, sommets = get_graphes_orientes("RCP101 - ED2 - Exercice 2")
print(graphe.getCommentaire())
print()
x1, x2, x3, x4, x5, x6 = sommets
pi, pere = graphe.dijkstra(x1)
print("pi :", pi)
print("père :", pere)
print()

graphe, sommets = get_graphes_orientes("RCP101 - ED2 - Exercice 3 questions 1 et 2")
print(graphe.getCommentaire())
print()
S1 = sommets[0]
S10 = sommets[9]
pi, pere = graphe.bellman(S1)
print(f"plus court chemin de {S1} à {S10} :", chemin(pere, S1, S10))
print(f"distance de {S1} à {S10} :", pi[S10])
print("pi :", pi)
print("père :", pere)
print()

graphe, sommets = get_graphes_orientes("RCP101 - ED2 - Exercice 3 question 3")
print(graphe.getCommentaire())
print()
S1 = sommets[0]
S10 = sommets[9]
pi, pere = graphe.bellman(S1)
print(f"plus court chemin de {S1} à {S10} :", chemin(pere, S1, S10))
print(f"distance de {S1} à {S10} :", pi[S10])
print("pi :", pi)
print("père :", pere)
print()

graphe, sommets = get_graphes_orientes("RCP101 - ED2 - Exercice 4")
print(graphe.getCommentaire())
print()
try:
    M, P = graphe.floyd_warshall()
    print("\tMatrice M de Floyd-Warshall :")
    afficheMatrice(sommets, M)
    print("\tMatrice P de Floyd-Warshall :")
    afficheMatrice(sommets, P)
    for s1, s2 in [(x, y) for x in sommets for y in sommets if x != y]:
        if M[s1, s2] == float('inf'):
            print(f"Il n'y a pas de plus court chemin de {s1} à {s2}.")
        else:
            print(f"Plus court chemin de {s1} à {s2} :", chemin2(P, s1, s2), "- distance :", M[s1, s2])
except Exception as e:
    print("\tIl y a un circuit absorbant. Fin de l'algorithme de Floyd-Warshall : " + repr(e))
