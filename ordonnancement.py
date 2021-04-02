from graphes import Sommet, Arc, GrapheOriente


class Tache:
    def __init__(self, nom: str, duree: float):
        self._nom = nom
        self._duree = duree
        self._plus_tot: float = 0.0
        self._plus_tard: float = 0.0
        self._marge_libre: float = 0.0

    def __repr__(self):
        return self._nom

    def __str__(self):
        return f"Tâche {self._nom} (durée : {self._duree}, \
plus tôt : {self._plus_tot}, plus tard : {self._plus_tard}, \
marge totale : {self.marge_totale()}, marge libre : {self._marge_libre})"

    def nom(self) -> str:
        return self._nom

    def duree(self) -> float:
        return self._duree

    def plus_tot(self) -> float:
        return self._plus_tot

    def plus_tard(self) -> float:
        return self._plus_tard

    def marge_libre(self) -> float:
        return self._marge_libre

    def setNom(self, nom: str) -> None:
        self._nom = nom

    def setDuree(self, duree: float) -> None:
        self._duree = duree

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
        Tache.__init__(self, nom, duree)
        Sommet.__init__(self, nom)

    def __repr__(self):
        return Tache.__repr__(self)

    def __str__(self):
        return Tache.__str__(self)


class EvenementPERT(Sommet):
    def __init__(self, nom: str):
        super().__init__(nom)
        self._plus_tot: float = 0.0
        self._plus_tard: float = 0.0

    def __repr__(self):
        return f"|{self._nom}|"

    def __str__(self):
        return f"Evénement {self._nom} (plus tôt : {self._plus_tot}, plus tard : {self._plus_tard})"

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
        Tache.__init__(self, nom, duree)
        Arc.__init__(self, EvenementPERT("déb " + nom), EvenementPERT("fin " + nom), duree)


class TachePERTFictive(TachePERT):
    def __init__(self, nom: str = 'fictive', duree: float = 0.0):
        super().__init__(nom, duree)


class GraphePERT(GrapheOriente):
    def __init__(self, *taches, prec=None, nom="", commentaire=""):
        for tache in taches:
            if not isinstance(tache, TachePERT):
                raise Exception(f"Les tâches doivent appartenir au type '{TachePERT.__name__}'")
        liste_taches = list(taches)
        self._evenement_debut = EvenementPERT(".Début")
        self._evenement_fin = EvenementPERT(".Fin")
        if prec is None:
            prec = []
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
            tache_suivante = [x[1] for x in prec if x[0] is not None and x[0] == tache]
            if len(taches_precedentes) == 0:
                tache_fictive = TachePERTFictive()
                tache_fictive.arrivee().setNom("début " + tache.nom())
                tache_fictive.setDepart(self._evenement_debut)
                tache.setDepart(tache_fictive.arrivee())
                liste_taches.append(tache_fictive)
            elif len(taches_precedentes) == 1:
                if taches_precedentes[0][0] is None:
                    tache_fictive = TachePERTFictive(duree=taches_precedentes[0][1])
                    tache_fictive.arrivee().setNom("début " + tache.nom())
                    tache_fictive.setDepart(self._evenement_debut)
                    tache.setDepart(tache_fictive.arrivee())
                    liste_taches.append(tache_fictive)
                else:
                    if taches_precedentes[0][1] > 0.0:
                        tache_fictive = TachePERTFictive(duree=taches_precedentes[0][1])
                        tache_fictive.arrivee().setNom("début " + tache.nom())
                        tache_fictive.setDepart(taches_precedentes[0][0].depart())
                        tache.setDepart(tache_fictive.arrivee())
                        liste_taches.append(tache_fictive)
                    else:
                        tache.setDepart(taches_precedentes[0][0].arrivee())
                        tache.depart().setNom("début " + tache.nom())
            else:
                evenement_commun = None
                for t, d in taches_precedentes:
                    tache_fictive = TachePERTFictive(duree=d)
                    if t is None:
                        tache_fictive.setDepart(self._evenement_debut)
                    else:
                        if d > 0.0:
                            tache_fictive.setDepart(t.depart())
                        else:
                            tache_fictive.setDepart(t.arrivee())
                    if evenement_commun is None:
                        evenement_commun = tache_fictive.arrivee()
                        evenement_commun.setNom("début " + tache.nom())
                    tache.setDepart(evenement_commun)
                    tache_fictive.setArrivee(evenement_commun)
                    liste_taches.append(tache_fictive)
            if not tache_suivante:
                tache_fictive = TachePERTFictive()
                tache_fictive.setDepart(tache.arrivee())
                tache_fictive.setArrivee(self._evenement_fin)
                liste_taches.append(tache_fictive)
        liste_sommets = list(
            set(
                map(
                    lambda tache: tache.depart(),
                    liste_taches
                )
            ).union(
                set(
                    map(
                        lambda tache: tache.arrivee(),
                        liste_taches
                    )
                )
            )
        )
        super().__init__(*liste_sommets, arcs=set(liste_taches), nom=nom, commentaire=commentaire)
        self._evenements = self._sommets
        self._simplifier()
        self._calculer_dates()

    def __repr__(self):
        return f"{self.__class__.__name__} {self._nom} \
\n({sorted(list(self.evenements()), key=EvenementPERT.__repr__)}, \
 \n{sorted(self.taches(), key=Tache.__repr__)})"

    def __str__(self):
        s = f"{self.__class__.__name__} {self._nom}\n\nTaches :\n"
        for tache in sorted(list(self.taches()), key=Tache.__repr__):
            s += f"\t{str(tache)}\n"
        s += "\nEvénements :\n"
        for ev in sorted(list(self.evenements()), key=EvenementPERT.__repr__):
            s += f"\t{str(ev)}\n"
        return s

    def evenements(self):
        return self._evenements

    def taches(self, fictives=True):
        if fictives:
            return self._arcs
        else:
            return set(
                filter(
                    lambda a: not isinstance(a, TachePERTFictive),
                    self._arcs
                )
            )

    def _simplifier(self):
        evenements_a_retirer = []
        for evenement in self._evenements:
            if len(self.successeurs(evenement)) == 1 and len(self.predecesseurs(evenement)) == 1:
                predecesseur = list(self.predecesseurs(evenement))[0]
                successeur = list(self.successeurs(evenement))[0]
                arc_avant = self.arc(predecesseur, evenement)
                arc_apres = self.arc(evenement, successeur)
                if isinstance(arc_avant, TachePERTFictive) and arc_avant.duree() == 0.0:
                    self._arcs.discard(arc_apres)
                    arc_apres.setDepart(predecesseur)
                    self._arcs.add(arc_apres)
                    self._arcs.discard(arc_avant)
                    evenements_a_retirer.append(evenement)
                elif isinstance(arc_apres, TachePERTFictive) and arc_apres.duree() == 0.0:
                    self._arcs.discard(arc_avant)
                    arc_avant.setArrivee(successeur)
                    self._arcs.add(arc_avant)
                    self._arcs.discard(arc_apres)
                    evenements_a_retirer.append(evenement)
        for evenement in evenements_a_retirer:
            self._evenements.discard(evenement)

    def evenement_debut(self) -> EvenementPERT:
        return self._evenement_debut

    def evenement_fin(self) -> EvenementPERT:
        return self._evenement_fin

    def _calculer_dates(self):
        pi, _ = self.bellman(self._evenement_debut, plus_long=True)
        for evenement in self.evenements():
            evenement.setPlus_tot(pi[evenement])
        arcs = set()
        for arc in self._arcs:
            depart, arrivee = arc.depart(), arc.arrivee()
            arcs.add(Arc(arrivee, depart, self.valuation(depart, arrivee)))
        graphe = GrapheOriente(*self._sommets, arcs=arcs)
        pi, _ = graphe.bellman(self._evenement_fin, plus_long=True)
        date_de_fin = self._evenement_fin.plus_tot()
        for evenement in self.evenements():
            evenement.setPlus_tard(date_de_fin - pi[evenement])
        taches = self.taches()
        for tache in taches:
            tache.setPlus_tot(tache.depart().plus_tot())
            tache.setPlus_tard(tache.arrivee().plus_tard() - tache.valuation())
            taches_suivantes = list(
                filter(
                    lambda t: t.depart() == tache.arrivee(),
                    taches
                )
            )
            if taches_suivantes and \
                    all(
                        map(
                            lambda t: isinstance(t, TachePERTFictive),
                            taches_suivantes
                        )
                    ):
                date_plus_tot = min(
                    [t.arrivee().plus_tot() - t.valuation() for t in taches_suivantes]
                )
            else:
                date_plus_tot = tache.arrivee().plus_tot()
            tache.setMarge_libre(date_plus_tot - tache.depart().plus_tot() - tache.duree())

    def date_de_fin(self) -> float:
        return self._evenement_fin.plus_tot()

    def taches_critiques(self) -> list:
        return sorted(
            list(
                set(
                    filter(
                        lambda tache: tache.marge_totale() == 0.0,
                        self.taches(fictives=False)
                    )
                )
            ),
            key=Tache.__repr__
        )


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
        s = f"{self.__class__.__name__} {self._nom}\n\nTaches :\n"
        for tache in sorted(list(self.taches()), key=Tache.__repr__):
            s += f"\t{str(tache)}\n"
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
