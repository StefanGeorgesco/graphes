from graphes_exemples import graphes_orientes, \
    listes_sommets_graphes_orientes, \
    sommets_depart_graphes_orientes

if __name__ == '__main__':
    """
    Déroulement des tests
    """
    for i in range(len(graphes_orientes)):
        graphe = graphes_orientes[i]
        sommets = listes_sommets_graphes_orientes[i]
        depart = sommets_depart_graphes_orientes[i]
        titre = graphe.getCommentaire()
        print()
        print("Cas", i, ":", titre)
        print()

        """
        Graphe
        """
        print("\t" + repr(graphe))
        print("\tnombre de sommets :", graphe.ordre())
        print("\tnombre d'arcs ou d'arêtes :", graphe.taille())
        print()

        """
        Forte connexité
        """
        print("\tComposantes fortement connexes :", graphe.cfcs())
        print("\tCe graphe " + ("est" if graphe.estFortementConnexe() else "n'est pas") + " fortement connexe.")
        print()

        """
        Matrices M et P de Floyd-Warshall
        """

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

        try:
            M,P = graphe.floyd_warshall()
            print("\tMatrice M de Floyd-Warshall :")
            afficheMatrice(sommets, M)
            print("\tMatrice P de Floyd-Warshall :")
            afficheMatrice(sommets, P)
        except Exception as e:
            print("\tIl y a un circuit absorbant. Fin de l'algorithme de Floyd-Warshall : " + repr(e))
        """
        Sommet de depart choisi pour le test
        """
        print("\t" + "sommet de depart".ljust(30), " :", repr(depart))

        """
        Chemins
        """
        for y in set(sommets) - {depart}:
            try:
                c, d = graphe.plus_court_chemin(depart, y)
                print("\t" + ("chemin jusqu'à " + repr(y)).ljust(30), " :", c)
                print("\t" + ("distance du chemin jusqu'à " + repr(y)).ljust(30), " :", d)
            except Exception as e:
                print("\t" + ("chemin jusqu'à " + repr(y)).ljust(30), " : pas de plus court chemin : " + repr(e))
                print("\t" + ("distance du chemin jusqu'à " + repr(y)).ljust(30), " : pas de plus court chemin : " + repr(e))
