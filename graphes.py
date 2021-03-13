class Sommet:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name


class GrapheNonOriente:
    def __init__(self, *sommets, aretes=None, nom="", commentaire=""):
        for sommet in sommets:
            if not isinstance(sommet, Sommet):
                raise Exception("Les sommets doivent appartenir au type Sommet")
        self._sommets = set(sommets)
        if aretes is None:
            aretes = []
        aretesUniques = []
        for arete in aretes:
            if arete not in aretesUniques:
                aretesUniques.append(arete)
        if not all(
                map(
                    lambda x: isinstance(x, set) and \
                              len(x) == 2 and \
                              x.issubset(self._sommets),
                    aretesUniques
                )
        ):
            raise Exception("les arêtes doivent être des ensembles de 2 sommets de 'sommets'")
        self._aretes = aretesUniques
        self._nom = nom
        self._commentaire = commentaire

    def __repr__(self):
        return f"GrapheNonOrienté {self._nom} ({self._sommets}, {self._aretes})"

    def lier(self, sommet1, sommet2):
        if sommet1 not in self._sommets or sommet2 not in self._sommets:
            raise Exception("les sommets doivent appartenir au graphe")
        if {sommet1,sommet2} not in self._aretes:
            self._aretes.append({sommet1,sommet2})

    def getSommets(self):
        return set(self._sommets)

    def getAretes(self):
        return list(map(lambda a: a, self._aretes))

    def getNom(self):
        return self._nom

    def getCommentaire(self):
        return self._commentaire

    def setNom(self, nom):
        if not isinstance(nom, str):
            raise Exception("'nom' doit être de type 'str'")
        self._nom = nom

    def setCommentaire(self, commentaire):
        if not isinstance(commentaire, str):
            raise Exception("'commentaire' doit être de type 'str'")
        self._commentaire = commentaire

    def ordre(self):
        return len(self._sommets)

    def taille(self):
        return len(self._aretes)

    def copie(self):
        return GrapheNonOriente(
            *self.getSommets(),
            aretes=self.getAretes(),
            nom=self.getNom(),
            commentaire=self.getCommentaire()
        )

    def sous_graphe(self, sommets):
        for sommet in sommets:
            if not isinstance(sommet, Sommet):
                raise Exception("Les sommets doivent appartenir au type Sommet")
        sommetsUniques = []
        for sommet in sommets:
            if sommet not in sommetsUniques:
                sommetsUniques.append(sommet)
        if not all(
            map(
                lambda s: s in self._sommets,
                sommetsUniques
            )
        ):
            raise Exception("Les sommets doivent appartenir au graphe")
        aretes = list(
                filter(
                lambda arete: arete.issubset(sommetsUniques),
                self._aretes
            )
        )
        return GrapheNonOriente(*sommetsUniques, aretes=aretes)

    def graphe_partiel(self, aretes):
        aretesUniques = []
        for arete in aretes:
            if arete not in aretesUniques:
                aretesUniques.append(arete)
        if not all(
            map(
                lambda a: a in self._aretes,
                aretesUniques
            )
        ):
            raise Exception("Les arêtes doivent appartenir au graphe")
        return GrapheNonOriente(*list(self._sommets), aretes=aretesUniques)

    def clique(n):
        if not isinstance(n, int) or n < 1:
            raise Exception("n doit être un entier strictement positif")
        sommets = [Sommet(str(i+1)) for i in range(n)]
        listeAretes = [{x,y} for x in sommets for y in sommets if x != y]
        aretes = []
        for arete in listeAretes:
            if arete not in aretes:
                aretes.append(arete)
        return GrapheNonOriente(*sommets, aretes=aretes)

    def estClique(self):
        return all(
            map(
                lambda arete: arete in self._aretes,
                [{x,y} for x in self._sommets for y in self._sommets if x!=y]
            )
        )


class GrapheOriente:
    def __init__(self, *sommets, p=None, nom="", commentaire=""):
        for sommet in sommets:
            if not isinstance(sommet, Sommet):
                raise Exception("Les sommets doivent appartenir au type Sommet")
        self._sommets = set(sommets)
        if p is None:
            p = {}
        if not isinstance(p, dict):
            raise Exception("p doit être un dict")
        if not all(
                map(
                    lambda x: isinstance(x, tuple) and \
                              len(x) == 2 and \
                              x[0] in sommets and \
                              x[1] in sommets,
                    p.keys()
                )
        ):
            raise Exception("les clés de p doivent être des 2-tuples de sommets de 'sommets'")
        if not all(
            map(
                lambda x: isinstance(x,int) or \
                          isinstance(x,float),
                p.values()
            )
        ):
            raise Exception("les valeurs de p doivent être des entiers ou des flottants")
        self._p = dict(p)
        self._nom = nom
        self._commentaire = commentaire

    def __repr__(self):
        return f"GrapheOrienté {self._nom} ({self._sommets}, {self._p})"

    def lier(self, sommet1, sommet2, poids):
        if sommet1 not in self._sommets or sommet2 not in self._sommets:
            raise Exception("les sommets doivent appartenir au graphe")
        self._p[(sommet1,sommet2)] = poids

    def getSommets(self):
        return set(self._sommets)

    def getP(self):
        return dict(self._p)

    def getNom(self):
        return self._nom

    def getCommentaire(self):
        return self._commentaire

    def setNom(self, nom):
        if not isinstance(nom, str):
            raise Exception("'nom' doit être de type 'str'")
        self._nom = nom

    def setCommentaire(self, commentaire):
        if not isinstance(commentaire, str):
            raise Exception("'commentaire' doit être de type 'str'")
        self._commentaire = commentaire

    def arcs(self):
        return set(self._p.keys())

    def ordre(self):
        return len(self._sommets)

    def taille(self):
        return len(self.arcs())

    def copie(self):
        return GrapheOriente(
            *self.getSommets(),
            p=self.getP(),
            nom=self.getNom(),
            commentaire=self.getCommentaire()
        )

    def sous_graphe(self, sommets):
        for sommet in sommets:
            if not isinstance(sommet, Sommet):
                raise Exception("Les sommets doivent appartenir au type Sommet")
        sommets = list(sommets)
        if not all(
            map(
                lambda s: s in self._sommets,
                sommets
            )
        ):
            raise Exception("Les sommets doivent appartenir au graphe")
        arcs = filter(
            lambda arc: arc[0] in sommets and arc[1] in sommets,
            self.arcs()
        )
        p = {}
        for arc in arcs:
            p.update({tuple(arc): self._p[arc]})
        return GrapheOriente(*sommets, p=p)

    def graphe_partiel(self, arcs):
        if not all(
            map(
                lambda a: a in self.arcs(),
                arcs
            )
        ):
            raise Exception("Les arcs doivent appartenir au graphe")
        p = {}
        for arc in arcs:
            p.update({tuple(arc): self._p[arc]})
        return GrapheOriente(*self.getSommets(), p=p)

    def successeurs(self, sommet):
        if sommet not in self._sommets:
            raise Exception("Le sommet n'est pas dans le graphe")
        arcs = self.getP().keys()
        return set(
            map(
                lambda x: x[1],
                filter(
                    lambda x: x[0] == sommet,
                    arcs
                )
            )
        )

    def predecesseurs(self, sommet):
        if sommet not in self._sommets:
            raise Exception("Le sommet n'est pas dans le graphe")
        arcs = self.getP().keys()
        return set(
            map(
                lambda x: x[0],
                filter(
                    lambda x: x[1] == sommet,
                    arcs
                )
            )
        )

    def descendants(self, sommet):
        if sommet not in self._sommets:
            raise Exception("Le sommet n'est pas dans le graphe")
        descendants = {sommet}
        examines = set()
        while descendants - examines:
            x = list((descendants - examines))[0]
            examines.add(x)
            descendants.update(self.successeurs(x))
        return descendants

    def ascendants(self, sommet):
        if sommet not in self._sommets:
            raise Exception("Le sommet n'est pas dans le graphe")
        ascendants = {sommet}
        examines = set()
        while ascendants - examines:
            x = list((ascendants - examines))[0]
            examines.add(x)
            ascendants.update(self.predecesseurs(x))
        return ascendants

    def cfc(self, sommet):
        if sommet not in self._sommets:
            raise Exception("Le sommet n'est pas dans le graphe")
        return self.descendants(sommet).intersection(self.ascendants(sommet))

    def cfcs(self):
        result = []
        sommets = set(self._sommets)
        while sommets:
            sommet = list(sommets)[0]
            cfc = self.cfc(sommet)
            result.append(cfc)
            sommets = sommets - cfc
        return result

    def estFortementConnexe(self):
        return len(self.cfcs()) == 1

    def dijkstra(self, r):
        if r not in self._sommets:
            raise Exception("'sommet' doit être un sommet du graphe")
        if any(
            map(
                lambda x: x < 0,
                self._p.values()
            )
        ):
            raise Exception("Les valuations du graphe ne sont pas toutes positives")
        A = {r}
        pivot = r
        pi = {r:0}
        pere = {}
        p = self.getP()
        n = self.ordre()
        sommets = self._sommets
        for x in sommets - {r}:
            pi[x] = float('inf')
        if n < 2:
            return pi, pere
        for j in range(1, n):
            for y in (sommets - A).intersection(self.successeurs(pivot)):
                if pi[pivot] + p[pivot,y] < pi[y]:
                    pi[y] = pi[pivot] + p[pivot,y]
                    pere[y] = pivot
            mini = min([pi[z] for z in sommets - A])
            pivot = list(
                filter(
                    lambda z: pi[z] == mini,
                    sommets - A
                )
            )[0]
            A.add(pivot)
        return pi, pere

    def numerotation_topolgique(self):
        num = {}
        graphe = self.copie()
        n = graphe.ordre()
        if n < 1:
            return num
        for i in range(1, n + 1):
            sommet = None
            for s in graphe.getSommets():
                if len(graphe.predecesseurs(s)) == 0:
                    sommet = s
                    break
            if sommet is None:
                raise Exception("Ce graphe comporte un circuit")
            num[sommet] = i
            graphe = graphe.sous_graphe(graphe.getSommets() - {sommet})
        return num

    def bellman(self, r):
        if r not in self._sommets:
            raise Exception("'sommet' doit être un sommet du graphe")
        num = self.numerotation_topolgique()
        if num[r] != 1:
            raise Exception("'sommet' n'est pas racine du graphe")
        A = {r}
        pi = {r:0}
        pere = {}
        p = self.getP()
        n = self.ordre()
        for sommet in self._sommets - {r}:
            pi[sommet] = float('inf')
        if n < 2:
            return pi, pere
        for j in range(2, n + 1):
            y = list(num.keys())[list(num.values()).index(j)]
            pi[y] = min([pi[x] + p[x,y] for x in A if x in self.predecesseurs(y)])
            x0 = list(
                    filter(
                        lambda x: (x,y) in p and pi[y] == pi[x] + p[x,y],
                        list(A)
                )
            )[0]
            pere[y] = x0
            A.add(y)
        return pi, pere

    def bellman_ford(self, r):
        if r not in self._sommets:
            raise Exception("'sommet' doit être un sommet du graphe")
        pi = {r:0}
        pere = {}
        p = self.getP()
        n = self.ordre()
        sommets = self._sommets
        for sommet in sommets - {r}:
            if sommet in self.successeurs(r):
                pi[sommet] = p[r, sommet]
                pere[sommet] = r
            else:
                pi[sommet] = float('inf')
        if n < 3:
            return pi, pere
        for k in range(1, n - 1):
            for sommet in sommets - {r}:
                mini = min([pi[y] + p[y, sommet] for y in self.predecesseurs(sommet)])
                x0 = list(
                    filter(
                        lambda y: pi[y] + p[y, sommet] == mini,
                        self.predecesseurs(sommet)
                    )
                )[0]
                if pi[x0] + p[x0, sommet] < pi[sommet]:
                    pi[sommet] = pi[x0] + p[x0, sommet]
                    pere[sommet] = x0
        return pi, pere

    def ford(self, r):
        if r not in self._sommets:
            raise Exception("'sommet' doit être un sommet du graphe")
        k = 0
        pi = {0: {r: 0}}
        pere = {}
        p = self.getP()
        n = self.ordre()
        sommets = self._sommets
        for sommet in sommets - {r}:
            pi[0].update({sommet: float('inf')})
        while True:
            changement = False
            k += 1
            for sommet in sommets:
                predecesseurs = self.predecesseurs(sommet)
                if len(predecesseurs) > 0:
                    mini = min(
                        pi[k-1][sommet],
                        min([pi[k-1][y] + p[y,sommet] for y in predecesseurs])
                    )
                else:
                    mini = pi[k-1][sommet]
                if k in pi.keys():
                    pi[k].update({sommet: mini})
                else:
                    pi.update({k: {sommet: mini}})
                if pi[k-1][sommet] != pi[k][sommet]:
                    pere[sommet] = list(
                        filter(
                            lambda y: pi[k-1][y] + p[y,sommet] == mini,
                            self.predecesseurs(sommet)
                        )
                    )[0]
                    changement = True
            if k == n or not changement:
                break
        if changement:
            raise Exception(f"Il existe un circuit absorbant accessible depuis {r}")
        return pi[k], pere

    def floyd_warshall(self):
        n = len(self._sommets)
        M = {}
        P = {}
        sommets = self._sommets
        for x in sommets:
            for y in sommets:
                M[x,y] = self._p[x,y] if x != y and (x,y) in self.arcs() \
                    else min(0, self._p[(x,y)]) if x == y and (x,y) in self.arcs() \
                    else 0 if x == y and (x,y) not in self.arcs() \
                    else float('inf')
                P[x,y] = x if x != y and (x,y) in self.arcs() else None
        for k in sommets:
            for i in sommets:
                for j in sommets:
                    if M[i,k] + M[k,j] < M[i,j]:
                        M[i,j] = M[i,k] + M[k,j]
                        P[i,j] = P[k,j]
                    if i == j and M[i,j] < 0:
                        raise Exception("il existe un circuit absorbant au niveau de " + repr(i))

        return (M,P)

    def plus_court_chemin(self, sommet1, sommet2):
        M,P = self.floyd_warshall()

        def chemin_rec(s1,s2):
            if s1 == s2:
                return []
            return chemin_rec(s1,P[s1,s2]) + [(P[s1,s2],s2)]

        if sommet1 not in self._sommets or sommet2 not in self._sommets:
            raise Exception("les sommets doivent appartenir au graphe")
        if M[sommet1,sommet2] == float('inf'):
            raise Exception("il n'y a pas de plus court chemin entre " + repr(sommet1) + " et " + repr(sommet2))

        return chemin_rec(sommet1,sommet2), M[sommet1,sommet2]
