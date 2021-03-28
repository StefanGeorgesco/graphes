import operator


class Sommet:
    def __init__(self, nom: str):
        self._nom = nom

    def __repr__(self):
        return self._nom

    def nom(self):
        return self._nom


class GrapheNonOriente:
    def __init__(self, *sommets, aretes=None, nom="", commentaire=""):
        for sommet in sommets:
            if not isinstance(sommet, Sommet):
                raise Exception(f"Les sommets doivent appartenir au type '{Sommet.__name__}'")
        self._sommets = set(sommets)
        if aretes is None:
            aretes = []
        aretesUniques = []
        for arete in aretes:
            if arete not in aretesUniques:
                if not isinstance(arete, set) or \
                        len(arete) != 2 or \
                        not arete.issubset(self._sommets):
                    raise Exception(f"Les arêtes doivent être des ensembles de 2 sommets de {sommets}")
                aretesUniques.append(arete)
        self._aretes = aretesUniques
        self.setNom(nom)
        self.setCommentaire(commentaire)

    def __repr__(self):
        return f"GrapheNonOrienté {self._nom} \
({sorted(list(self._sommets), key=Sommet.__repr__)}, {self._aretes})"

    def lier(self, sommet1, sommet2):
        if sommet1 not in self._sommets or sommet2 not in self._sommets:
            raise Exception("les sommets doivent appartenir au graphe")
        if {sommet1, sommet2} not in self._aretes:
            self._aretes.append({sommet1, sommet2})

    def sommets(self):
        return set(self._sommets)

    def aretes(self):
        return list(self._aretes)

    def nom(self):
        return self._nom

    def commentaire(self):
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
            *self.sommets(),
            aretes=self.aretes(),
            nom=self.nom(),
            commentaire=self.commentaire()
        )

    def sous_graphe(self, sommets):
        for sommet in sommets:
            if not isinstance(sommet, Sommet):
                raise Exception(f"Les sommets doivent appartenir au type '{Sommet.__name__}'")
        sommetsUniques = []
        for sommet in sommets:
            if sommet not in sommetsUniques:
                if sommet not in self._sommets:
                    raise Exception("Les sommets doivent appartenir au graphe")
                sommetsUniques.append(sommet)
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
                if arete not in self._aretes:
                    raise Exception("Les arêtes doivent appartenir au graphe")
                aretesUniques.append(arete)
        return GrapheNonOriente(*self.sommets(), aretes=aretesUniques)

    @classmethod
    def clique(cls, n):
        if not isinstance(n, int) or n < 1:
            raise Exception("n doit être un entier strictement positif")
        sommets = [Sommet(str(i + 1)) for i in range(n)]
        listeAretes = [{x, y} for x in sommets for y in sommets if x != y]
        aretes = []
        for arete in listeAretes:
            if arete not in aretes:
                aretes.append(arete)
        return cls(*sommets, aretes=aretes)

    def estClique(self):
        return all(
            map(
                lambda arete: arete in self._aretes,
                [{x, y} for x in self._sommets for y in self._sommets if x != y]
            )
        )


class Arc:
    def __init__(self, depart: Sommet, arrivee: Sommet, valuation: float = 1.0):
        self._depart = depart
        self._arrivee = arrivee
        self._valuation = valuation

    def __hash__(self):
        return (self._depart.__hash__(), self._arrivee.__hash__()).__hash__()

    def __eq__(self, other):
        return (self._depart.__hash__(), self._arrivee.__hash__()) == \
               (other.depart().__hash__(), other.arrivee().__hash__())

    def __repr__(self):
        return f"({self._depart},{self._arrivee},{self._valuation})"

    def depart(self):
        return self._depart

    def arrivee(self):
        return self._arrivee

    def valuation(self):
        return self._valuation

    def setValuation(self, valuation: float):
        self._valuation = valuation


class GrapheOriente:
    def __init__(self, *sommets, arcs=None, nom="", commentaire=""):
        for sommet in sommets:
            if not isinstance(sommet, Sommet):
                raise Exception(f"Les sommets doivent appartenir au type '{Sommet.__name__}'")
        self._sommets = set(sommets)
        if arcs is None:
            self._arcs = set()
        else:
            if not isinstance(arcs, set):
                raise Exception("Le paramètre 'arcs' doit être un 'set'.")
            if not all(
                    map(
                        lambda arc: isinstance(arc, Arc) and \
                                    arc.depart() in sommets and \
                                    arc.arrivee() in sommets,
                        list(arcs)
                    )
            ):
                raise Exception(f"Les arcs doivent être de type 'Arc' et lier des sommets de {sommets}")
            self._arcs = arcs
        self.setNom(nom)
        self.setCommentaire(commentaire)

    def __repr__(self):
        return f"GrapheOrienté {self._nom} \
({sorted(list(self._sommets), key=Sommet.__repr__)}, {sorted(self._arcs, key=Arc.__repr__)})"

    def lier(self, sommet1, sommet2, poids):
        if sommet1 not in self._sommets or sommet2 not in self._sommets:
            raise Exception("Les sommets doivent appartenir au graphe")
        self._arcs.discard(Arc(sommet1, sommet2))
        self._arcs.add(Arc(sommet1, sommet2, poids))

    def sommets(self):
        return set(self._sommets)

    def arcs(self):
        return set(self._arcs)

    def arc(self, depart: Sommet, arrivee: Sommet):
        arcs = list(
            filter(
                lambda arc: arc.depart() == depart and arc.arrivee() == arrivee,
                self._arcs
            )
        )
        if arcs:
            return arcs[0]
        else:
            return None

    def valuation(self, depart: Sommet, arrivee: Sommet):
        return self.arc(depart, arrivee).valuation()

    def nom(self):
        return self._nom

    def commentaire(self):
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
        return len(self.arcs())

    def copie(self):
        sommets = {}
        for sommet in self._sommets:
            sommets.update({sommet: Sommet(sommet.nom())})
        arcs = set(
            map(
                lambda arc: Arc(sommets[arc.depart()], sommets[arc.arrivee()], arc.valuation()),
                list(self._arcs)
            )
        )
        return GrapheOriente(
            *sommets.values(),
            arcs=arcs,
            nom="Copie de " + self.nom(),
            commentaire=self.commentaire()
        )

    def sous_graphe(self, sommets):
        sommets = list(sommets)
        if not all(
                map(
                    lambda s: s in self._sommets,
                    sommets
                )
        ):
            raise Exception("Les sommets doivent appartenir au graphe")
        arcs = filter(
            lambda arc: arc.depart() in sommets and arc.arrivee() in sommets,
            self._arcs
        )
        return GrapheOriente(*sommets, arcs=set(arcs))

    def graphe_partiel(self, arcs):
        if not isinstance(arcs, set):
            raise Exception("Le paramètre 'arcs' doit être un set")
        if not all(
                map(
                    lambda arc: arc in self.arcs(),
                    list(arcs)
                )
        ):
            raise Exception("Les arcs doivent appartenir au graphe")
        selection_arcs = filter(
            lambda arc: arc in arcs,
            self._arcs
        )
        return GrapheOriente(*self.sommets(), arcs=set(selection_arcs))

    def successeurs(self, sommet):
        if sommet not in self._sommets:
            raise Exception("Le sommet n'est pas dans le graphe")
        return set(
            map(
                lambda arc: arc.arrivee(),
                filter(
                    lambda arc: arc.depart() == sommet,
                    self._arcs
                )
            )
        )

    def predecesseurs(self, sommet):
        if sommet not in self._sommets:
            raise Exception("Le sommet n'est pas dans le graphe")
        return set(
            map(
                lambda arc: arc.depart(),
                filter(
                    lambda arc: arc.arrivee() == sommet,
                    self._arcs
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
                    lambda arc: arc.valuation() < 0,
                    self._arcs
                )
        ):
            raise Exception("Les valuations du graphe ne sont pas toutes positives")
        A = {r}
        pivot = r
        pi = {r: 0}
        pere = {}
        n = self.ordre()
        sommets = self._sommets
        for x in sommets - {r}:
            pi[x] = float('inf')
        if n < 2:
            return pi, pere
        for j in range(1, n):
            for y in (sommets - A).intersection(self.successeurs(pivot)):
                if pi[pivot] + self.valuation(pivot, y) < pi[y]:
                    pi[y] = pi[pivot] + self.valuation(pivot, y)
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
        graphe = self
        n = graphe.ordre()
        if n < 1:
            return num
        for i in range(1, n + 1):
            sommet = None
            for s in graphe.sommets():
                if len(graphe.predecesseurs(s)) == 0:
                    sommet = s
                    break
            if sommet is None:
                raise Exception("Ce graphe comporte un circuit")
            num[sommet] = i
            graphe = graphe.sous_graphe(graphe.sommets() - {sommet})
        return num

    def bellman(self, r, plus_long=False):
        if r not in self._sommets:
            raise Exception("'sommet' doit être un sommet du graphe")
        num = self.numerotation_topolgique()
        if num[r] != 1:
            raise Exception("'sommet' n'est pas racine du graphe")
        f = max if plus_long else min
        A = {r}
        pi = {r: 0}
        pere = {}
        n = self.ordre()
        for sommet in self._sommets - {r}:
            pi[sommet] = float('inf')
        if n < 2:
            return pi, pere
        for j in range(2, n + 1):
            y = list(num.keys())[list(num.values()).index(j)]
            pi[y] = f([pi[x] + self.valuation(x, y) for x in A if x in self.predecesseurs(y)])
            x0 = list(
                filter(
                    lambda x: Arc(x, y) in self._arcs and pi[y] == pi[x] + self.valuation(x, y),
                    A
                )
            )[0]
            pere[y] = x0
            A.add(y)
        return pi, pere

    def bellman_ford(self, r, plus_long=False):
        if r not in self._sommets:
            raise Exception("'sommet' doit être un sommet du graphe")
        f = max if plus_long else min
        op = operator.__gt__ if plus_long else operator.__lt__
        limit = -float('inf') if plus_long else float('inf')
        pi = {r: 0}
        pere = {}
        n = self.ordre()
        sommets = self._sommets
        for sommet in sommets - {r}:
            if sommet in self.successeurs(r):
                pi[sommet] = self.valuation(r, sommet)
                pere[sommet] = r
            else:
                pi[sommet] = limit
        if n < 3:
            return pi, pere
        for k in range(1, n - 1):
            for sommet in sommets - {r}:
                predecesseurs = self.predecesseurs(sommet)
                if len(predecesseurs) > 0:
                    val = f([pi[y] + self.valuation(y, sommet) for y in predecesseurs])
                    x0 = list(
                        filter(
                            lambda y: pi[y] + self.valuation(y, sommet) == val,
                            predecesseurs
                        )
                    )[0]
                    if op(pi[x0] + self.valuation(x0, sommet), pi[sommet]):
                        pi[sommet] = pi[x0] + self.valuation(x0, sommet)
                        pere[sommet] = x0
        return pi, pere

    def ford(self, r, plus_long=False):
        if r not in self._sommets:
            raise Exception("'sommet' doit être un sommet du graphe")
        f = max if plus_long else min
        limit = -float('inf') if plus_long else float('inf')
        k = 0
        pi = {0: {r: 0}}
        pere = {}
        n = self.ordre()
        sommets = self._sommets
        for sommet in sommets - {r}:
            pi[0].update({sommet: limit})
        while True:
            changement = False
            k += 1
            for sommet in sommets:
                predecesseurs = self.predecesseurs(sommet)
                if len(predecesseurs) > 0:
                    val = f(
                        pi[k - 1][sommet],
                        f([pi[k - 1][y] + self.valuation(y, sommet) for y in predecesseurs])
                    )
                else:
                    val = pi[k - 1][sommet]
                if k in pi.keys():
                    pi[k].update({sommet: val})
                else:
                    pi.update({k: {sommet: val}})
                if pi[k - 1][sommet] != pi[k][sommet]:
                    pere[sommet] = list(
                        filter(
                            lambda y: pi[k - 1][y] + self.valuation(y, sommet) == val,
                            self.predecesseurs(sommet)
                        )
                    )[0]
                    changement = True
            if k == n or not changement:
                break
        if changement:
            raise Exception(f"Il existe un circuit absorbant accessible depuis {r}")
        return pi[k], pere

    def floyd_warshall(self, plus_long=False):
        f = max if plus_long else min
        op = operator.__gt__ if plus_long else operator.__lt__
        limit = -float('inf') if plus_long else float('inf')
        M = {}
        P = {}
        sommets = self._sommets
        for x in sommets:
            for y in sommets:
                M[x, y] = self.valuation(x, y) if x != y and Arc(x, y) in self._arcs \
                    else f(0, self.valuation(x, y)) if x == y and Arc(x, y) in self._arcs \
                    else 0 if x == y and Arc(x, y) not in self._arcs \
                    else limit
                P[x, y] = x if x != y and Arc(x, y) in self._arcs else None
        for k in sommets:
            for i in sommets:
                for j in sommets:
                    if op(M[i, k] + M[k, j], M[i, j]):
                        M[i, j] = M[i, k] + M[k, j]
                        P[i, j] = P[k, j]
                    if i == j and op(M[i, j], 0):
                        raise Exception(f"Il existe un circuit absorbant au niveau de {i}")
        return (M, P)

    def chemin_optimal(self, sommet1, sommet2, plus_long=False):
        M, P = self.floyd_warshall(plus_long)

        def chemin_rec(s1, s2):
            if s1 == s2:
                return []
            return chemin_rec(s1, P[s1, s2]) + [(P[s1, s2], s2)]

        if sommet1 not in self._sommets or sommet2 not in self._sommets:
            raise Exception("les sommets doivent appartenir au graphe")
        if M[sommet1, sommet2] == float('inf'):
            raise Exception(f"Il n'y a pas de chemin optimal entre {sommet1} et {sommet2}")
        return chemin_rec(sommet1, sommet2), M[sommet1, sommet2]


class Algorithme:
    def calculer_pi_pere(self, graphe: GrapheOriente, racine: Sommet, plus_long=False) -> (dict, dict):
        return {}, {}


class Dijkstra(Algorithme):
    def calculer_pi_pere(self, graphe: GrapheOriente, racine: Sommet, plus_long=False) -> (dict, dict):
        if plus_long:
            raise Exception("L'algorithme de Dijkstra ne calcule que des plus courts chemins")
        return graphe.dijkstra(racine)


class Bellman(Algorithme):
    def calculer_pi_pere(self, graphe: GrapheOriente, racine: Sommet, plus_long=False) -> (dict, dict):
        return graphe.bellman(racine, plus_long=plus_long)


class BellmanFord(Algorithme):
    def calculer_pi_pere(self, graphe: GrapheOriente, racine: Sommet, plus_long=False) -> (dict, dict):
        return graphe.bellman_ford(racine, plus_long=plus_long)


class Ford(Algorithme):
    def calculer_pi_pere(self, graphe: GrapheOriente, racine: Sommet, plus_long=False) -> (dict, dict):
        return graphe.ford(racine, plus_long=plus_long)


class FloydWarshall(Algorithme):
    def calculer_pi_pere(self, graphe: GrapheOriente, racine: Sommet, plus_long=False) -> (dict, dict):
        M, P = graphe.floyd_warshall(plus_long=plus_long)
        pi, pere = {}, {}
        for sommet in graphe.sommets() - {racine}:
            pi.update({sommet: M[racine, sommet]})
            pere.update({sommet: P[racine, sommet]})
        return pi, pere


class CheminOptimal:
    def __init__(self, algorithme: Algorithme = FloydWarshall()):
        self._algorithme = algorithme

    def calculer(self, graphe: GrapheOriente, sommet1: Sommet, sommet2: Sommet, plus_long=False):
        if sommet1 not in graphe.sommets() or sommet2 not in graphe.sommets():
            raise Exception("Les sommets doivent appartenir au graphe")
        pi, pere = self._algorithme.calculer_pi_pere(graphe, sommet1, plus_long=plus_long)

        def chemin(s1, s2):
            if s1 == s2:
                return []
            else:
                return chemin(s1, pere[s2]) + [(pere[s2], s2)]

        if pi[sommet2] == float('inf'):
            raise Exception(f"Il n'y a pas de chemin optimal entre {sommet1} et {sommet2}")
        return chemin(sommet1, sommet2), pi[sommet2]
