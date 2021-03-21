from graphes import GrapheOriente, Sommet


class Tache(Sommet):
    def __init__(self, nom: str, duree: float):
        super().__init__(nom)
        self._duree: float = duree
        self._plus_tot: float = 0.0
        self._plus_tard: float = 0.0
        self._marge_libre: float = 0.0

    def __repr__(self):
        return super().__repr__() + f"({self.getPlus_tot()},{self.getPlus_tard()})"

    def getDuree(self) -> float:
        return self._duree

    def getPlus_tot(self) -> float:
        return self._plus_tot

    def getPlus_tard(self) -> float:
        return self._plus_tard

    def getMarge_libre(self) -> float:
        return self._marge_libre

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


class GrapheMPM(GrapheOriente):
    def __init__(self, *taches, prec=None, nom="", commentaire=""):
        for tache in taches:
            if not isinstance(tache, Tache):
                raise Exception(f"Les tâches doivent appartenir au type '{Tache.__name__}'")
        liste_taches = list(taches)
        p = {}
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
            self._tache_debut = Tache("Début", 0.0)
            self._tache_fin = Tache("Fin", 0.0)
            liste_taches.append(self._tache_debut)
            liste_taches.append(self._tache_fin)
            for x in prec:
                if len(x) == 2:
                    t1, t2 = x
                    p.update({(t1, t2): t1.getDuree()})
                else:
                    t1, t2, d = x
                    if t1 is None:
                        t1 = self._tache_debut
                    p.update({(t1, t2): d})
            for tache in set(taches) - set(map(lambda x: x[1], prec)):
                p.update({(self._tache_debut, tache): 0.0})
            for tache in set(taches) - set(map(lambda x: x[0], prec)):
                p.update({(tache, self._tache_fin): tache.getDuree()})
        super().__init__(*liste_taches, p=p, nom=nom, commentaire=commentaire)
        self._calculer_dates()

    def __repr__(self) -> str:
        return f"GrapheMPM {self._nom} ({self._sommets}, {self._p})"

    def __str__(self) -> str:
        s = f"GrapheMPM {self._nom}\nTaches :\n"
        for tache in self.getTaches():
            s += f"\t{tache}\n"
        s += "Liens :\n"
        p = self.getP()
        for lien in p.keys():
            s += f"\t{lien}: {p[lien]}\n"
        return s

    def getTaches(self) -> list:
        return self.getSommets()

    def getTache_debut(self) -> Tache:
        return self._tache_debut

    def getTache_fin(self) -> Tache:
        return self._tache_fin

    def _calculer_dates(self) -> None:
        pi, pere = self.bellman(self._tache_debut, plus_long=True)
        for tache in self._sommets:
            tache.setPlus_tot(pi[tache])
        p = self.getP()
        p2 = {}
        for t1, t2 in p.keys():
            p2.update({(t2, t1): p[(t1, t2)]})
        graphe = GrapheOriente(*self._sommets, p=p2)
        pi, _ = graphe.bellman(self._tache_fin, plus_long=True)
        date_de_fin = self._tache_fin.getPlus_tot()
        for tache in self._sommets:
            tache.setPlus_tard(date_de_fin - pi[tache])
            if tache != self._tache_fin:
                tache.setMarge_libre(
                    min(
                        [
                            succ.getPlus_tot() - tache.getPlus_tot() - p[tache, succ]
                            for succ in self.successeurs(tache)
                        ]
                    )
                )

    def date_de_fin(self) -> float:
        return self._tache_fin.getPlus_tot()

    def taches_critiques(self) -> list:
        return list(
            set(
                filter(
                    lambda tache: tache.marge_totale() == 0.0,
                    self.getTaches()
                )
            ) - {self._tache_debut, self._tache_fin}
        )
