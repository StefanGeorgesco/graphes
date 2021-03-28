import unittest
from graphes import *
from graphes_exemples import \
    graphes_non_orientes, \
    listes_sommets_graphes_non_orientes, \
    graphes_orientes, \
    listes_sommets_graphes_orientes

"""
Tests sur les graphes non orientés
"""


class TestsGraphesNonOrientes(unittest.TestCase):

    def setUp(self) -> None:
        self.graphesNonOrientes = {}
        for nom in graphes_non_orientes.keys():
            self.graphesNonOrientes.update({nom: (graphes_non_orientes[nom], listes_sommets_graphes_non_orientes[nom])})

    def chemin(self, pere, s1, s2):
        if s1 == s2:
            return []
        return self.chemin(pere, s1, pere[s2]) + [(pere[s2], s2)]

    def test_ordre_et_taille_graphe_non_oriente(self):
        s1 = Sommet("1")
        s2 = Sommet("2")
        s3 = Sommet("3")
        s4 = Sommet("4")
        graphe1 = GrapheNonOriente(s1, s2, s3, aretes=[{s1, s2}, {s1, s3}])
        self.assertEqual(3, graphe1.ordre())
        self.assertEqual(2, graphe1.taille())
        graphe2 = GrapheNonOriente(s1, s2, s3, s4)
        graphe2.lier(s1, s2)
        graphe2.lier(s1, s3)
        graphe2.lier(s2, s3)
        graphe2.lier(s2, s4)
        graphe2.lier(s3, s4)
        self.assertEqual(4, graphe2.ordre())
        self.assertEqual(5, graphe2.taille())

    def test_sommets_et_aretes_graphe_non_oriente(self):
        graphe, sommets = self.graphesNonOrientes["Exemple de graphe non orienté"]
        A, B, C, D, E, F = sommets
        self.assertEqual(set(sommets), graphe.sommets())
        aretes = graphe.aretes()
        self.assertEqual(len(aretes), 8)
        self.assertTrue({A, B} in aretes)
        self.assertTrue({A, C} in aretes)
        self.assertTrue({A, F} in aretes)
        self.assertTrue({B, E} in aretes)
        self.assertTrue({C, E} in aretes)
        self.assertTrue({C, D} in aretes)
        self.assertTrue({D, E} in aretes)
        self.assertTrue({D, F} in aretes)
        self.assertFalse({E, F} in aretes)
        self.assertFalse({B, D} in aretes)
        self.assertFalse({B, C} in aretes)
        self.assertFalse({A, D} in aretes)
        self.assertFalse({A, E} in aretes)

    def test_copie_graphe_non_oriente(self):
        graphe, sommets = self.graphesNonOrientes["Exemple de graphe non orienté"]
        A, B, C, D, E, F = sommets
        graphe.setNom("nom")
        graphe_copie = graphe.copie()
        self.assertEqual("nom", graphe_copie.nom())
        self.assertEqual("Exemple de graphe non orienté", graphe_copie.commentaire())
        self.assertEqual(set(sommets), graphe_copie.sommets())
        aretes = graphe_copie.aretes()
        self.assertEqual(len(aretes), 8)
        self.assertTrue({A, B} in aretes)
        self.assertTrue({A, C} in aretes)
        self.assertTrue({A, F} in aretes)
        self.assertTrue({B, E} in aretes)
        self.assertTrue({C, E} in aretes)
        self.assertTrue({C, D} in aretes)
        self.assertTrue({D, E} in aretes)
        self.assertTrue({D, F} in aretes)
        self.assertFalse({E, F} in aretes)
        self.assertFalse({B, D} in aretes)
        self.assertFalse({B, C} in aretes)
        self.assertFalse({A, D} in aretes)
        self.assertFalse({A, E} in aretes)

    def test_sous_graphe_graphe_non_oriente(self):
        graphe, sommets = self.graphesNonOrientes["Exemple de graphe non orienté"]
        A, B, C, D, E, F = sommets
        sous_graphe = graphe.sous_graphe({A, B, C, E, F})
        self.assertEqual(5, len(sous_graphe.sommets()))
        self.assertEqual({A, B, C, E, F}, sous_graphe.sommets())
        self.assertEqual(5, len(sous_graphe.aretes()))
        self.assertEqual([{A, B}, {A, C}, {A, F}, {B, E}, {C, E}], sous_graphe.aretes())

    def test_graphe_partiel_graphe_non_oriente(self):
        graphe, sommets = self.graphesNonOrientes["Exemple de graphe non orienté"]
        A, B, C, D, E, F = sommets
        graphe_partiel = graphe.graphe_partiel([{A, C}, {A, F}, {B, E}, {C, D}, {D, E}])
        self.assertEqual(6, len(graphe_partiel.sommets()))
        self.assertEqual({A, B, C, D, E, F}, graphe_partiel.sommets())
        self.assertEqual(5, len(graphe_partiel.aretes()))
        self.assertTrue({A, C} in graphe_partiel.aretes())
        self.assertTrue({A, F} in graphe_partiel.aretes())
        self.assertTrue({B, E} in graphe_partiel.aretes())
        self.assertTrue({C, D} in graphe_partiel.aretes())
        self.assertTrue({D, E} in graphe_partiel.aretes())

    def test_clique_et_est_clique(self):
        c = GrapheNonOriente.clique(5)
        self.assertEqual(5, len(c.sommets()))
        s1, s2, s3, s4, s5 = c.sommets()
        self.assertEqual(10, len(c.aretes()))
        self.assertTrue({s1, s2} in c.aretes())
        self.assertTrue({s1, s3} in c.aretes())
        self.assertTrue({s1, s4} in c.aretes())
        self.assertTrue({s1, s5} in c.aretes())
        self.assertTrue({s2, s3} in c.aretes())
        self.assertTrue({s2, s4} in c.aretes())
        self.assertTrue({s2, s5} in c.aretes())
        self.assertTrue({s3, s4} in c.aretes())
        self.assertTrue({s3, s5} in c.aretes())
        self.assertTrue({s4, s5} in c.aretes())
        self.assertTrue(c.estClique())


"""
Tests sur les graphes orientés
"""


class TestsGraphesOrientes(unittest.TestCase):

    def setUp(self) -> None:
        self.graphesOrientes = {}
        for nom in graphes_orientes.keys():
            self.graphesOrientes.update({nom: (graphes_orientes[nom], listes_sommets_graphes_orientes[nom])})

    def chemin(self, pere, s1, s2):
        if s1 == s2:
            return []
        return self.chemin(pere, s1, pere[s2]) + [(pere[s2], s2)]

    def test_egalite_arcs(self):
        s1 = Sommet("s1")
        s2 = Sommet("s2")
        s3 = Sommet("s3")
        a1 = Arc(s1, s2)
        a2 = Arc(s1, s2, 5.0)
        a3 = Arc(s1, s2, 2.0)
        a4 = Arc(s1, s3)
        self.assertEqual(a1, a2)
        self.assertEqual(a1, a3)
        self.assertEqual(a2, a3)
        self.assertNotEqual(a1, a4)
        self.assertNotEqual(a2, a4)
        self.assertNotEqual(a3, a4)
        self.assertNotEqual(a1, Arc(s2, s1))
        self.assertTrue(Arc(s1, s2, 7.0) in [a1, a4])
        self.assertFalse(a2 in [Arc(s2, s1), Arc(s2, s3, 12.0), a4])

    def test_initialisation_arcs(self):
        s1 = Sommet("1")
        s2 = Sommet("2")
        s3 = Sommet("3")
        s4 = Sommet("4")
        s5 = Sommet("5")
        graphe1 = GrapheOriente(
            s1, s2, s3, s4, s5,
            p={(s1, s2): 2.0, (s1, s3): 5.0, (s2, s4): -1.0, (s4, s2): 1.0, (s4, s5): 1.0, (s5, s1): -3.0}
        )
        arcs = graphe1.arcs()
        self.assertEqual(6, len(arcs))
        self.assertEqual({Arc(s1, s2), Arc(s1, s3), Arc(s2, s4), Arc(s4, s2), Arc(s4, s5), Arc(s5, s1)}, arcs)
        self.assertTrue(Arc(s2, s1) not in arcs)
        self.assertTrue(Arc(s3, s1) not in arcs)
        self.assertTrue(Arc(s5, s1) in arcs)
        valuations = set(map(lambda arc: arc.valuation(), list(arcs)))
        self.assertEqual({2.0, 5.0, -1.0, 1.0, -3.0}, valuations)
        graphe2 = GrapheOriente(s1, s2, s3, s4, s5)
        graphe2.lier(s1, s2, 2.0)
        graphe2.lier(s1, s3, 5.0)
        graphe2.lier(s2, s4, -1.0)
        graphe2.lier(s4, s2, 1.0)
        graphe2.lier(s4, s5, 1.0)
        graphe2.lier(s5, s1, -3.0)
        arcs = graphe2.arcs()
        self.assertEqual(6, len(arcs))
        self.assertEqual({Arc(s1, s2), Arc(s1, s3), Arc(s2, s4), Arc(s4, s2), Arc(s4, s5), Arc(s5, s1)}, arcs)
        self.assertTrue(Arc(s2, s1) not in arcs)
        self.assertTrue(Arc(s3, s1) not in arcs)
        self.assertTrue(Arc(s5, s1) in arcs)
        valuations = set(map(lambda arc: arc.valuation(), list(arcs)))
        self.assertEqual({2.0, 5.0, -1.0, 1.0, -3.0}, valuations)
        graphe3, sommets = self.graphesOrientes["'RCP101_Partie1_Graphes_et_Algorithmes' (RCP101), pages 25/27/33"]
        s1, s2, s5, s6, s8, s9, s18, s19 = sommets[0], sommets[1], sommets[4], sommets[5], \
                                           sommets[7], sommets[8], sommets[17], sommets[18]
        arcs = graphe3.arcs()
        self.assertEqual(40, len(arcs))
        self.assertTrue(Arc(s1, s2) in arcs)
        self.assertTrue(Arc(s2, s1) in arcs)
        self.assertFalse(Arc(s5, s6) in arcs)
        self.assertTrue(Arc(s6, s5) in arcs)
        self.assertTrue(Arc(s8, s9) in arcs)
        self.assertFalse(Arc(s9, s8) in arcs)
        self.assertTrue(Arc(s18, s19) in arcs)
        self.assertTrue(Arc(s19, s18) in arcs)
        valuations = set(map(lambda arc: arc.valuation(), list(arcs)))
        self.assertEqual({1.0, 2.0}, valuations)

    def test_ordre_et_taille_graphe_oriente(self):
        s1 = Sommet("1")
        s2 = Sommet("2")
        s3 = Sommet("3")
        s4 = Sommet("4")
        graphe1 = GrapheOriente(s1, s2, s3, p={(s1, s2): 2.0, (s1, s3): 5.0})
        self.assertEqual(3, graphe1.ordre())
        self.assertEqual(2, graphe1.taille())
        graphe2 = GrapheOriente(s1, s2, s3, s4)
        graphe2.lier(s1, s2, 5.0)
        graphe2.lier(s1, s3, 3.0)
        graphe2.lier(s2, s3, 1.0)
        graphe2.lier(s2, s4, -1.0)
        graphe2.lier(s3, s4, 0.0)
        self.assertEqual(4, graphe2.ordre())
        self.assertEqual(5, graphe2.taille())

    def test_sommets_et_arcs_graphe_oriente(self):
        graphe, sommets = self.graphesOrientes["'RCP101_Partie1_Graphes_et_Algorithmes' (RCP101), page 92"]
        A, B, C, D, E, F = sommets
        self.assertEqual(set(sommets), graphe.sommets())
        arcs = graphe.arcs_()
        self.assertEqual(len(arcs), 10)
        self.assertTrue((F, D) in arcs)
        self.assertTrue((D, B) in arcs)
        self.assertTrue((A, E) in arcs)
        self.assertTrue((C, F) in arcs)
        self.assertTrue((D, C) in arcs)
        self.assertFalse((D, F) in arcs)
        self.assertFalse((B, D) in arcs)
        self.assertFalse((E, A) in arcs)
        self.assertFalse((F, C) in arcs)
        self.assertFalse((C, D) in arcs)
        self.assertFalse((C, E) in arcs)
        self.assertFalse((B, F) in arcs)
        self.assertFalse((D, A) in arcs)

    def test_copie_graphe_oriente(self):
        graphe, sommets = self.graphesOrientes["'RCP101_Partie1_Graphes_et_Algorithmes' (RCP101), page 92"]
        A, B, C, D, E, F = sommets
        graphe.setNom("nom")
        graphe_copie = graphe.copie()
        self.assertEqual("nom", graphe_copie.nom())
        self.assertEqual("'RCP101_Partie1_Graphes_et_Algorithmes' (RCP101), page 92", graphe_copie.commentaire())
        self.assertEqual(set(sommets), graphe_copie.sommets())
        arcs = graphe_copie.arcs_()
        self.assertEqual(len(arcs), 10)
        self.assertTrue((F, D) in arcs)
        self.assertTrue((D, B) in arcs)
        self.assertTrue((A, E) in arcs)
        self.assertTrue((C, F) in arcs)
        self.assertTrue((D, C) in arcs)
        self.assertFalse((D, F) in arcs)
        self.assertFalse((B, D) in arcs)
        self.assertFalse((E, A) in arcs)
        self.assertFalse((F, C) in arcs)
        self.assertFalse((C, D) in arcs)
        self.assertFalse((C, E) in arcs)
        self.assertFalse((B, F) in arcs)
        self.assertFalse((D, A) in arcs)

    def test_sous_graphe_graphe_oriente(self):
        graphe, sommets = self.graphesOrientes["'RCP101_Partie1_Graphes_et_Algorithmes' (RCP101), page 92"]
        A, B, C, D, E, F = sommets
        sous_graphe = graphe.sous_graphe({A, B, C, E, F})
        self.assertEqual(5, len(sous_graphe.sommets()))
        self.assertEqual({A, B, C, E, F}, sous_graphe.sommets())
        self.assertEqual(6, len(sous_graphe.arcs_()))
        self.assertEqual({(A, B), (A, E), (B, E), (B, C), (F, E), (C, F)}, sous_graphe.arcs_())

    def test_graphe_partiel_graphe_oriente(self):
        graphe, sommets = self.graphesOrientes["'RCP101_Partie1_Graphes_et_Algorithmes' (RCP101), page 92"]
        A, B, C, D, E, F = sommets
        graphe_partiel = graphe.graphe_partiel({(A, B), (B, C), (C, F), (F, E), (F, D)})
        self.assertEqual(6, len(graphe_partiel.sommets()))
        self.assertEqual({A, B, C, D, E, F}, graphe_partiel.sommets())
        self.assertEqual(5, len(graphe_partiel.arcs_()))
        self.assertEqual({(A, B), (B, C), (C, F), (F, E), (F, D)}, graphe_partiel.arcs_())

    def test_successeurs(self):
        graphe, sommets = self.graphesOrientes["'RCP101_Partie1_Graphes_et_Algorithmes' (RCP101), page 92"]
        A, B, C, D, E, F = sommets
        self.assertEqual({B, E}, graphe.successeurs(A))
        self.assertEqual({C, E}, graphe.successeurs(B))
        self.assertEqual({F}, graphe.successeurs(C))
        self.assertEqual({B, C}, graphe.successeurs(D))
        self.assertEqual({D}, graphe.successeurs(E))
        self.assertEqual({D, E}, graphe.successeurs(F))

    def test_predecesseurs(self):
        graphe, sommets = self.graphesOrientes["'RCP101_Partie1_Graphes_et_Algorithmes' (RCP101), page 92"]
        A, B, C, D, E, F = sommets
        self.assertEqual(set(), graphe.predecesseurs(A))
        self.assertEqual({A, D}, graphe.predecesseurs(B))
        self.assertEqual({B, D}, graphe.predecesseurs(C))
        self.assertEqual({E, F}, graphe.predecesseurs(D))
        self.assertEqual({A, B, F}, graphe.predecesseurs(E))
        self.assertEqual({C}, graphe.predecesseurs(F))

    def test_descendants(self):
        graphe, sommets = self.graphesOrientes["'RCP101_Partie1_Graphes_et_Algorithmes' (RCP101), page 85"]
        S1, S2, S3, S4, S5, S6, S7, S8, S9 = sommets
        self.assertEqual({S3, S4, S5, S6, S7, S8, S9}, graphe.descendants(S3))
        self.assertEqual({S4, S6, S7, S8, S9}, graphe.descendants(S7))
        self.assertEqual({S4, S8}, graphe.descendants(S4))
        self.assertEqual({S8}, graphe.descendants(S8))

    def test_ascendants(self):
        graphe, sommets = self.graphesOrientes["'RCP101_Partie1_Graphes_et_Algorithmes' (RCP101), page 85"]
        S1, S2, S3, S4, S5, S6, S7, S8, S9 = sommets
        self.assertEqual({S1, S3}, graphe.ascendants(S3))
        self.assertEqual({S1, S2, S3, S5, S7}, graphe.ascendants(S7))
        self.assertEqual({S1, S2, S3, S4, S5, S7}, graphe.ascendants(S4))
        self.assertEqual({S1, S2, S3, S4, S5, S6, S7, S8, S9}, graphe.ascendants(S8))

    def test_cfc0(self):
        graphe, sommets = self.graphesOrientes["RCP101 - ED1 - Exercice 1"]
        A, B, C, D, E, F = sommets
        self.assertEqual({D, C}, graphe.cfc(D))
        self.assertEqual({A, B, E, F}, graphe.cfc(B))

    def test_cfcs0(self):
        graphe, sommets = self.graphesOrientes["RCP101 - ED1 - Exercice 1"]
        A, B, C, D, E, F = sommets
        cfcs = graphe.cfcs()
        self.assertEqual(2, len(cfcs))
        self.assertTrue({D, C} in cfcs)
        self.assertTrue({A, B, E, F} in cfcs)
        self.assertFalse(graphe.estFortementConnexe())

    def test_cfc1(self):
        graphe, sommets = self.graphesOrientes["RCP101 - ED1 - Exercice 2 - Question 1"]
        Ap, Am, Bp, Bm, Cp, Cm, Dp, Dm, Ep, Em = sommets
        self.assertEqual({Bm, Am, Dp, Cp}, graphe.cfc(Bm))
        self.assertEqual({Bp, Ap, Dm, Cm}, graphe.cfc(Bp))
        self.assertEqual({Ep}, graphe.cfc(Ep))
        self.assertEqual({Em}, graphe.cfc(Em))

    def test_cfcs1(self):
        graphe, sommets = self.graphesOrientes["RCP101 - ED1 - Exercice 2 - Question 1"]
        Ap, Am, Bp, Bm, Cp, Cm, Dp, Dm, Ep, Em = sommets
        cfcs = graphe.cfcs()
        self.assertEqual(4, len(cfcs))
        self.assertTrue({Bm, Am, Dp, Cp} in cfcs)
        self.assertTrue({Bp, Ap, Dm, Cm} in cfcs)
        self.assertTrue({Ep} in cfcs)
        self.assertTrue({Em} in cfcs)
        self.assertFalse(graphe.estFortementConnexe())

    def test_cfc2(self):
        graphe, sommets = self.graphesOrientes["RCP101 - ED1 - Exercice 2 - Question 2"]
        Ap, Am, Bp, Bm, Cp, Cm, Dp, Dm, Ep, Em, Fp, Fm = sommets
        self.assertEqual(set(sommets), graphe.cfc(Bm))
        self.assertEqual(set(sommets), graphe.cfc(Bp))
        self.assertEqual(set(sommets), graphe.cfc(Ep))
        self.assertEqual(set(sommets), graphe.cfc(Em))

    def test_cfcs2(self):
        graphe, sommets = self.graphesOrientes["RCP101 - ED1 - Exercice 2 - Question 2"]
        cfcs = graphe.cfcs()
        self.assertEqual(1, len(cfcs))
        self.assertEqual(set(sommets), cfcs[0])
        self.assertTrue(graphe.estFortementConnexe())
        self.assertTrue(graphe.estFortementConnexe())

    def test_dijkstra(self):
        graphe, sommets = self.graphesOrientes["'RCP101_Partie1_Graphes_et_Algorithmes' (RCP101), page 74"]
        S1, S2, S3, S4, S5, S6, S7, S8 = sommets
        pi, pere = graphe.dijkstra(S1)
        self.assertEqual([(S1, S3), (S3, S4), (S4, S2)], self.chemin(pere, S1, S2))
        self.assertEqual([(S1, S3), (S3, S5), (S5, S6), (S6, S7), (S7, S8)], self.chemin(pere, S1, S8))
        self.assertEqual(5, pi[S8])
        self.assertEqual(4, pi[S7])
        self.assertEqual(3, pi[S6])
        self.assertEqual(6, pi[S2])

    def test_numerotation_topolgique_graphe_oriente(self):
        graphe, sommets = self.graphesOrientes["'RCP101_Partie1_Graphes_et_Algorithmes' (RCP101), page 85"]
        num = graphe.numerotation_topolgique()
        self.assertEqual(set(sommets), set(num.keys()))
        self.assertEqual({1, 2, 3, 4, 5, 6, 7, 8, 9}, set(num.values()))

    def test_bellman(self):
        graphe, sommets = self.graphesOrientes["RCP101 - ED2 - Exercice 3 questions 1 et 2"]
        S1, S2, S3, S4, S5, S6, S7, S8, S9, S10 = sommets
        pi, pere = graphe.bellman(S1)
        self.assertEqual(S7, pere[S9])
        self.assertEqual(S1, pere[S3])
        self.assertEqual(S1, pere[S4])
        self.assertEqual(6, pi[S10])
        self.assertEqual(14, pi[S8])
        self.assertEqual(11, pi[S5])
        pi, pere = graphe.bellman(S1, plus_long=True)
        self.assertEqual(S6, pere[S9])
        self.assertEqual(S5, pere[S3])
        self.assertEqual(S3, pere[S4])
        self.assertEqual(24, pi[S10])
        self.assertEqual(22, pi[S8])
        self.assertEqual(11, pi[S5])
        graphe, sommets = self.graphesOrientes["'RCP101_Partie1_Graphes_et_Algorithmes' (RCP101), page 85"]
        S1, S2, S3, S4, S5, S6, S7, S8, S9 = sommets
        pi, pere = graphe.bellman(S1)
        self.assertEqual([(S1, S3), (S3, S5), (S5, S7), (S7, S6), (S6, S9)], self.chemin(pere, S1, S9))
        self.assertEqual([(S1, S3), (S3, S5), (S5, S7), (S7, S8)], self.chemin(pere, S1, S8))
        self.assertEqual(1, pi[S9])
        self.assertEqual(-2, pi[S8])
        self.assertEqual(1, pi[S7])
        self.assertEqual(0, pi[S6])

    def test_bellman_ford(self):
        graphe, sommets = self.graphesOrientes["RCP101 - ED2 - Exercice 3 questions 1 et 2"]
        S1, S2, S3, S4, S5, S6, S7, S8, S9, S10 = sommets
        pi, pere = graphe.bellman_ford(S1)
        self.assertEqual(S7, pere[S9])
        self.assertEqual(S1, pere[S3])
        self.assertEqual(S1, pere[S4])
        self.assertEqual(6, pi[S10])
        self.assertEqual(14, pi[S8])
        self.assertEqual(11, pi[S5])
        pi, pere = graphe.bellman_ford(S1, plus_long=True)
        self.assertEqual(S6, pere[S9])
        self.assertEqual(S5, pere[S3])
        self.assertEqual(S3, pere[S4])
        self.assertEqual(24, pi[S10])
        self.assertEqual(22, pi[S8])
        self.assertEqual(11, pi[S5])
        graphe, sommets = self.graphesOrientes["RCP101 - ED2 - Exercice 4"]
        A, B, C, D, E = sommets
        pi, pere = graphe.bellman_ford(A)
        self.assertEqual([(A, D), (D, E)], self.chemin(pere, A, E))
        self.assertEqual(5, pi[E])
        pi, pere = graphe.bellman_ford(C)
        self.assertEqual([(C, D), (D, E)], self.chemin(pere, C, E))
        self.assertEqual(2, pi[E])
        pi, pere = graphe.bellman_ford(B)
        self.assertEqual([(B, D), (D, E)], self.chemin(pere, B, E))
        self.assertEqual(1, pi[E])

    def test_ford(self):
        graphe, sommets = self.graphesOrientes["RCP101 - ED2 - Exercice 3 questions 1 et 2"]
        S1, S2, S3, S4, S5, S6, S7, S8, S9, S10 = sommets
        pi, pere = graphe.ford(S1)
        self.assertEqual(S7, pere[S9])
        self.assertEqual(S1, pere[S3])
        self.assertEqual(S1, pere[S4])
        self.assertEqual(6, pi[S10])
        self.assertEqual(14, pi[S8])
        self.assertEqual(11, pi[S5])
        pi, pere = graphe.ford(S1, plus_long=True)
        self.assertEqual(S6, pere[S9])
        self.assertEqual(S5, pere[S3])
        self.assertEqual(S3, pere[S4])
        self.assertEqual(24, pi[S10])
        self.assertEqual(22, pi[S8])
        self.assertEqual(11, pi[S5])
        graphe, sommets = self.graphesOrientes["'RCP101_Partie1_Graphes_et_Algorithmes' (RCP101), page 92"]
        A, B, C, D, E, F = sommets
        pi, pere = graphe.ford(A)
        self.assertEqual([(A, B), (B, C), (C, F)], self.chemin(pere, A, F))
        self.assertEqual(-1, pi[F])
        self.assertEqual([(A, B), (B, E)], self.chemin(pere, A, E))
        self.assertEqual(2, pi[E])
        self.assertEqual([(A, B), (B, C), (C, F), (F, D)], self.chemin(pere, A, D))
        self.assertEqual(0, pi[D])

    def test_floyd_warshall(self):
        graphe, sommets = self.graphesOrientes["RCP101 - ED2 - Exercice 3 questions 1 et 2"]
        S1, S2, S3, S4, S5, S6, S7, S8, S9, S10 = sommets
        M, P = graphe.floyd_warshall()
        self.assertEqual(S7, P[S1, S9])
        self.assertEqual(S1, P[S1, S3])
        self.assertEqual(S1, P[S1, S4])
        self.assertEqual(6, M[S1, S10])
        self.assertEqual(14, M[S1, S8])
        self.assertEqual(11, M[S1, S5])
        M, P = graphe.floyd_warshall(plus_long=True)
        self.assertEqual(S6, P[S1, S9])
        self.assertEqual(S5, P[S1, S3])
        self.assertEqual(S3, P[S1, S4])
        self.assertEqual(24, M[S1, S10])
        self.assertEqual(22, M[S1, S8])
        self.assertEqual(11, M[S1, S5])
        graphe, sommets = self.graphesOrientes["RCP101 - ED2 - Exercice 4"]
        A, B, C, D, E = sommets
        M, P = graphe.floyd_warshall()
        self.assertEqual(5, M[A, B])
        self.assertEqual(1, M[B, E])
        self.assertEqual(-1, M[C, D])
        self.assertEqual(0, M[B, C])
        self.assertEqual(float('inf'), M[C, A])
        self.assertEqual(C, P[A, B])
        self.assertEqual(D, P[B, E])
        self.assertEqual(C, P[C, D])
        self.assertEqual(D, P[B, C])
        self.assertEqual(None, P[C, A])

    def test_chemin_optimal(self):
        graphe, sommets = self.graphesOrientes["RCP101 - ED2 - Exercice 3 questions 1 et 2"]
        S1, S2, S3, S4, S5, S6, S7, S8, S9, S10 = sommets
        chemin, longueur = graphe.chemin_optimal(S1, S8)
        self.assertEqual(3, len(chemin))
        self.assertEqual([(S1, S3), (S3, S6), (S6, S8)], chemin)
        self.assertEqual(14, longueur)
        chemin, longueur = graphe.chemin_optimal(S1, S8, plus_long=True)
        self.assertEqual(5, len(chemin))
        self.assertEqual([(S1, S2), (S2, S5), (S5, S3), (S3, S6), (S6, S8)], chemin)
        self.assertEqual(22, longueur)
        graphe, sommets = self.graphesOrientes["'RCP101_Partie1_Graphes_et_Algorithmes' (RCP101), page 92"]
        A, B, C, D, E, F = sommets
        chemin, longueur = graphe.chemin_optimal(A, D)
        self.assertEqual(4, len(chemin))
        self.assertEqual([(A, B), (B, C), (C, F), (F, D)], chemin)
        self.assertEqual(0, longueur)
        chemin, longueur = graphe.chemin_optimal(B, D)
        self.assertEqual(3, len(chemin))
        self.assertEqual([(B, C), (C, F), (F, D)], chemin)
        self.assertEqual(-4, longueur)

    def test_classe_chemin_optimal(self):
        graphe, sommets = self.graphesOrientes["RCP101 - ED2 - Exercice 3 questions 1 et 2"]
        S1, S2, S3, S4, S5, S6, S7, S8, S9, S10 = sommets

        chemin, longueur = CheminOptimal().calculer(graphe, S1, S8)
        self.assertEqual(3, len(chemin))
        self.assertEqual([(S1, S3), (S3, S6), (S6, S8)], chemin)
        self.assertEqual(14, longueur)
        chemin, longueur = CheminOptimal().calculer(graphe, S1, S8, plus_long=True)
        self.assertEqual(5, len(chemin))
        self.assertEqual([(S1, S2), (S2, S5), (S5, S3), (S3, S6), (S6, S8)], chemin)
        self.assertEqual(22, longueur)

        chemin, longueur = CheminOptimal(Bellman()).calculer(graphe, S1, S8)
        self.assertEqual(3, len(chemin))
        self.assertEqual([(S1, S3), (S3, S6), (S6, S8)], chemin)
        self.assertEqual(14, longueur)
        chemin, longueur = CheminOptimal(Bellman()).calculer(graphe, S1, S8, plus_long=True)
        self.assertEqual(5, len(chemin))
        self.assertEqual([(S1, S2), (S2, S5), (S5, S3), (S3, S6), (S6, S8)], chemin)
        self.assertEqual(22, longueur)

        chemin, longueur = CheminOptimal(BellmanFord()).calculer(graphe, S1, S8)
        self.assertEqual(3, len(chemin))
        self.assertEqual([(S1, S3), (S3, S6), (S6, S8)], chemin)
        self.assertEqual(14, longueur)
        chemin, longueur = CheminOptimal(BellmanFord()).calculer(graphe, S1, S8, plus_long=True)
        self.assertEqual(5, len(chemin))
        self.assertEqual([(S1, S2), (S2, S5), (S5, S3), (S3, S6), (S6, S8)], chemin)
        self.assertEqual(22, longueur)

        chemin, longueur = CheminOptimal(Ford()).calculer(graphe, S1, S8)
        self.assertEqual(3, len(chemin))
        self.assertEqual([(S1, S3), (S3, S6), (S6, S8)], chemin)
        self.assertEqual(14, longueur)
        chemin, longueur = CheminOptimal(Ford()).calculer(graphe, S1, S8, plus_long=True)
        self.assertEqual(5, len(chemin))
        self.assertEqual([(S1, S2), (S2, S5), (S5, S3), (S3, S6), (S6, S8)], chemin)
        self.assertEqual(22, longueur)

        graphe, sommets = self.graphesOrientes["'RCP101_Partie1_Graphes_et_Algorithmes' (RCP101), page 92"]
        A, B, C, D, E, F = sommets

        chemin, longueur = CheminOptimal().calculer(graphe, A, D)
        self.assertEqual(4, len(chemin))
        self.assertEqual([(A, B), (B, C), (C, F), (F, D)], chemin)
        self.assertEqual(0, longueur)
        chemin, longueur = CheminOptimal().calculer(graphe, B, D)
        self.assertEqual(3, len(chemin))
        self.assertEqual([(B, C), (C, F), (F, D)], chemin)
        self.assertEqual(-4, longueur)

        chemin, longueur = CheminOptimal(BellmanFord()).calculer(graphe, A, D)
        self.assertEqual(4, len(chemin))
        self.assertEqual([(A, B), (B, C), (C, F), (F, D)], chemin)
        self.assertEqual(0, longueur)
        chemin, longueur = CheminOptimal(BellmanFord()).calculer(graphe, B, D)
        self.assertEqual(3, len(chemin))
        self.assertEqual([(B, C), (C, F), (F, D)], chemin)
        self.assertEqual(-4, longueur)

        chemin, longueur = CheminOptimal(Ford()).calculer(graphe, A, D)
        self.assertEqual(4, len(chemin))
        self.assertEqual([(A, B), (B, C), (C, F), (F, D)], chemin)
        self.assertEqual(0, longueur)
        chemin, longueur = CheminOptimal(Ford()).calculer(graphe, B, D)
        self.assertEqual(3, len(chemin))
        self.assertEqual([(B, C), (C, F), (F, D)], chemin)
        self.assertEqual(-4, longueur)

        graphe, sommets = self.graphesOrientes["'RCP101_Partie1_Graphes_et_Algorithmes' (RCP101), page 74"]
        S1, S2, S3, S4, S5, S6, S7, S8 = sommets

        chemin, longueur = CheminOptimal().calculer(graphe, S1, S8)
        self.assertEqual(5, len(chemin))
        self.assertEqual([(S1, S3), (S3, S5), (S5, S6), (S6, S7), (S7, S8)], chemin)
        self.assertEqual(5, longueur)

        chemin, longueur = CheminOptimal(Dijkstra()).calculer(graphe, S1, S8)
        self.assertEqual(5, len(chemin))
        self.assertEqual([(S1, S3), (S3, S5), (S5, S6), (S6, S7), (S7, S8)], chemin)
        self.assertEqual(5, longueur)

        chemin, longueur = CheminOptimal(BellmanFord()).calculer(graphe, S1, S8)
        self.assertEqual(5, len(chemin))
        self.assertEqual([(S1, S3), (S3, S5), (S5, S6), (S6, S7), (S7, S8)], chemin)
        self.assertEqual(5, longueur)

        chemin, longueur = CheminOptimal(Ford()).calculer(graphe, S1, S8)
        self.assertEqual(5, len(chemin))
        self.assertEqual([(S1, S3), (S3, S5), (S5, S6), (S6, S7), (S7, S8)], chemin)
        self.assertEqual(5, longueur)


if __name__ == '__main__':
    unittest.main()
