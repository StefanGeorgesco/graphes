from graphes import Sommet, Arc, GrapheOriente


class Tache:
    def __init__(self):
        self._plus_tot: float = 0.0
        self._plus_tard: float = 0.0
        self._marge_libre: float = 0.0

    def __repr__(self):
        return f"({self.plus_tot()},{self.plus_tard()})"

    def plus_tot(self) -> float:
        return self._plus_tot

    def plus_tard(self) -> float:
        return self._plus_tard

    def marge_libre(self) -> float:
        return self._marge_libre

    def setPlus_tot(self, plus_tot: float) -> None:
        self._plus_tot = plus_tot

    def setPlus_tard(self, plus_tard: float) -> None:
        self._plus_tard = plus_tard

    def setMarge_libre(self, marge_libre: float) -> None:
        self._marge_libre = marge_libre

    def marge_totale(self) -> float:
        return self._plus_tard - self._plus_tot


class TacheMPM(Tache, Sommet):
    def __init__(self, nom: str, duree: float):
        Tache.__init__(self)
        Sommet.__init__(self, nom)
        self._duree: float = duree

    def __repr__(self):
        return Sommet.__repr__(self) + Tache.__repr__(self)

    def nom(self):
        return self._nom

    def duree(self) -> float:
        return self._duree

    def setDuree(self, duree: float) -> None:
        self._duree = duree


class EvenementPERT(Sommet):
    def __init__(self, nom: str):
        super().__init__(nom)
        self._plus_tot: float = 0.0
        self._plus_tard: float = 0.0

    def plus_tot(self) -> float:
        return self._plus_tot

    def plus_tard(self) -> float:
        return self._plus_tard

    def setPlus_tot(self, plus_tot: float) -> None:
        self._plus_tot = plus_tot

    def setPlus_tard(self, plus_tard: float) -> None:
        self._plus_tard = plus_tard


class TachePERT(Tache, Arc):
    def __init__(self, nom: str, duree: float):
        Tache.__init__(self)
        Arc.__init__(self, EvenementPERT("début " + nom), EvenementPERT("fin " + nom), duree)
        self._nom = nom

    def __repr__(self):
        return self._nom + Tache.__repr__(self)

    def duree(self) -> float:
        return self._valuation

    def setDuree(self, duree: float) -> None:
        self.setValuation(duree)

class TachePERTFictive(TachePERT):
    def __init__(self, nom : str='fictive', duree: float=0.0):
        super().__init__(nom, duree)

    def __repr__(self):
        return f"{self._nom} {repr(self.depart())} {repr(self.arrivee())}"


class GraphePERT(GrapheOriente):
    def __init__(self, *taches, prec=None, nom="", commentaire=""):
        for tache in taches:
            if not isinstance(tache, TachePERT):
                raise Exception(f"Les tâches doivent appartenir au type '{TachePERT.__name__}'")
        liste_taches = list(taches)
        self._evenement_debut = EvenementPERT(".Début")
        self._evenement_fin = EvenementPERT(".Fin")
        if prec is not None:
            if not isinstance(prec, list):
                raise Exception(f"{prec} doit être une liste")
            if not all(
                    map(
                        lambda x: isinstance(x, tuple) and \
                                  x[1] in taches and \
                                  (len(x) == 2 and x[0] in taches or
                                   len(x) == 3 and (x[0] is None or x[0] in taches) and
                                   isinstance(x[2], float)),
                        prec
                    )
            ):
                raise Exception(f"Les éléments de {prec} doivent être du type \
(t1,t2) ou (t1,t2,durée), où t1,t2 sont dans {taches} et durée est un flottant")
            for tache in taches:
                taches_precedentes = [(x[0], x[2] if len(x) == 3 else 0.0) for x in prec if x[1] == tache]
                if len(taches_precedentes) == 0:
                    tache.setDepart(self._evenement_debut)
                elif len(taches_precedentes) == 1:
                    if taches_precedentes[0][0] is None:
                        tache_fictive = TachePERTFictive(duree=taches_precedentes[0][1])
                        tache_fictive.setDepart(self._evenement_debut)
                        tache.setDepart(tache_fictive.arrivee())
                        liste_taches.append(tache_fictive)
                    else:
                        if taches_precedentes[0][1] > 0:
                            tache_fictive = TachePERTFictive(duree=taches_precedentes[0][1])
                            tache_fictive.setDepart(taches_precedentes[0][0].depart())
                            tache.setDepart(tache_fictive.arrivee())
                            liste_taches.append(tache_fictive)
                        else:
                            tache.setDepart(taches_precedentes[0][0].arrivee())
                else:
                    for t, d in taches_precedentes:
                        tache_fictive = TachePERTFictive(duree=d)
                        tache_fictive.setDepart(t.arrivee())
                        tache.setDepart(tache_fictive.arrivee())
                        liste_taches.append(tache_fictive)
        for tache in set(taches) - set([x[0] for x in prec if x[0] is not None]):
            tache_fictive = TachePERTFictive()
            tache_fictive.setDepart(tache.arrivee())
            tache_fictive.setArrivee(self._evenement_fin)
            liste_taches.append(tache_fictive)
        liste_sommets = list(
            set(
                map(
                    lambda arc: arc.depart(),
                    liste_taches
                )
            ).union(
                set(
                    map(
                        lambda arc: arc.arrivee(),
                        liste_taches
                    )
                )
            )
        )
        super().__init__(*liste_sommets, arcs=set(liste_taches), nom=nom, commentaire=commentaire)
        self._evenements = self._sommets
        self._simplifier()
        # self._calculer_dates()

    def evenements(self):
        return self._evenements

    def _simplifier(self):
        for evenement in self._evenements:
            if len(self.successeurs(evenement)) == 1 and len(self.predecesseurs(evenement)) == 1:
                predecesseur = list(self.predecesseurs(evenement))[0]
                successeur = list(self.successeurs(evenement))[0]
                arc_avant = self.arc(predecesseur, evenement)
                arc_apres = self.arc(evenement, successeur)
                if isinstance(arc_avant, TachePERTFictive) and arc_avant.duree() == 0:
                    arc_apres.setDepart(predecesseur)
                    self._arcs.discard(arc_avant)
                elif isinstance(arc_apres, TachePERTFictive) and arc_apres.duree() == 0:
                    arc_avant.setArrivee(successeur)
                    self._arcs.discard(arc_apres)


class GrapheMPM(GrapheOriente):
    def __init__(self, *taches, prec=None, nom="", commentaire=""):
        for tache in taches:
            if not isinstance(tache, TacheMPM):
                raise Exception(f"Les tâches doivent appartenir au type '{TacheMPM.__name__}'")
        self._tache_debut = TacheMPM(".Début", 0.0)
        self._tache_fin = TacheMPM(".Fin", 0.0)
        liste_taches = list(taches)
        liste_taches.append(self._tache_debut)
        liste_taches.append(self._tache_fin)
        arcs = set()
        if prec is not None:
            if not isinstance(prec, list):
                raise Exception(f"{prec} doit être une liste")
            if not all(
                    map(
                        lambda x: isinstance(x, tuple) and \
                                  x[1] in taches and \
                                  (len(x) == 2 and x[0] in taches or
                                   len(x) == 3 and (x[0] in taches or x[0] is None) and
                                   isinstance(x[2], float)),
                        prec
                    )
            ):
                raise Exception(f"Les éléments de {prec} doivent être du type \
(t1,t2) ou (t1,t2,durée), où t1,t2 sont dans {taches} et durée est un flottant")
            for x in prec:
                if len(x) == 2:
                    t1, t2 = x
                    arcs.add(Arc(t1, t2, t1.duree()))
                else:
                    t1, t2, d = x
                    if t1 is None:
                        t1 = self._tache_debut
                    arcs.add(Arc(t1, t2, d))
        for tache in set(taches) - set(map(lambda x: x[1], prec)):
            arcs.add(Arc(self._tache_debut, tache, 0.0))
        for tache in set(taches) - set(map(lambda x: x[0], prec)):
            arcs.add(Arc(tache, self._tache_fin, tache.duree()))
        super().__init__(*liste_taches, arcs=arcs, nom=nom, commentaire=commentaire)
        self._calculer_dates()

    def __repr__(self) -> str:
        return f"GrapheMPM {self._nom} ({sorted(list(self._sommets), key=Sommet.__repr__)}, \
{sorted(self._arcs, key=Arc.__repr__)})"

    def __str__(self) -> str:
        s = f"GrapheMPM {self._nom}\n\nTaches :\n"
        for tache in sorted(list(self.taches()), key=TacheMPM.__repr__):
            s += f"\t{tache}\n"
        s += "\nLiens :\n"
        for arc in self._arcs:
            s += f"\t{(arc.depart(), arc.arrivee(), arc.valuation())}\n"
        return s

    def taches(self, deb_fin=True) -> list:
        if deb_fin:
            return self.sommets()
        else:
            return self.sommets() - {self.tache_debut(), self.tache_fin()}

    def tache_debut(self) -> TacheMPM:
        return self._tache_debut

    def tache_fin(self) -> TacheMPM:
        return self._tache_fin

    def _calculer_dates(self) -> None:
        pi, pere = self.bellman(self._tache_debut, plus_long=True)
        for tache in self._sommets:
            tache.setPlus_tot(pi[tache])
        arcs = set()
        for arc in self._arcs:
            depart, arrivee = arc.depart(), arc.arrivee()
            arcs.add(Arc(arrivee, depart, self.valuation(depart, arrivee)))
        graphe = GrapheOriente(*self._sommets, arcs=arcs)
        pi, _ = graphe.bellman(self._tache_fin, plus_long=True)
        date_de_fin = self._tache_fin.plus_tot()
        for tache in self._sommets:
            tache.setPlus_tard(date_de_fin - pi[tache])
            if tache != self._tache_fin:
                tache.setMarge_libre(
                    min(
                        [
                            succ.plus_tot() - tache.plus_tot() - self.valuation(tache, succ)
                            for succ in self.successeurs(tache)
                        ]
                    )
                )

    def date_de_fin(self) -> float:
        return self._tache_fin.plus_tot()

    def taches_critiques(self) -> list:
        return sorted(
            list(
                set(
                    filter(
                        lambda tache: tache.marge_totale() == 0.0,
                        self.taches()
                    )
                ) - {self._tache_debut, self._tache_fin}
            ),
            key=TacheMPM.__repr__
        )


