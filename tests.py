import unittest
from graphes import Sommet, GrapheNonOriente, GrapheOriente
from graphes_exemples import \
    graphes_non_orientes, \
    listes_sommets_graphes_non_orientes, \
    graphes_orientes, \
    listes_sommets_graphes_orientes

class TestStringMethods(unittest.TestCase):

    def test_ordre_et_taille_graphe_non_oriente(self):
        s1 = Sommet("1")
        s2 = Sommet("2")
        s3 = Sommet("3")
        s4 = Sommet("4")
        graphe1 = GrapheNonOriente(s1, s2, s3, aretes=[{s1,s2}, {s1,s3}])
        self.assertEqual(3, graphe1.ordre())
        self.assertEqual(2, graphe1.taille())
        graphe2 = GrapheNonOriente(s1, s2, s3, s4)
        graphe2.lier(s1,s2)
        graphe2.lier(s1,s3)
        graphe2.lier(s2,s3)
        graphe2.lier(s2,s4)
        graphe2.lier(s3,s4)
        self.assertEqual(4, graphe2.ordre())
        self.assertEqual(5, graphe2.taille())

    def test_sommets_et_aretes_graphe_non_oriente(self):
        graphe, sommets = self.get_graphes_non_orientes("Exemple de graphe non orienté")
        A, B, C, D, E, F = sommets
        self.assertEqual(set(sommets), graphe.getSommets())
        aretes = graphe.getAretes()
        self.assertEqual(len(aretes), 8)
        self.assertTrue({A, B} in aretes)
        self.assertTrue({A, C} in aretes)
        self.assertTrue({A, F} in aretes)
        self.assertTrue({B, E} in aretes)
        self.assertTrue({C, E} in aretes)
        self.assertTrue({C, D} in aretes)
        self.assertTrue({D, E} in aretes)
        self.assertTrue({D, F} in aretes)
        self.assertFalse({E,F} in aretes)
        self.assertFalse({B,D} in aretes)
        self.assertFalse({B,C} in aretes)
        self.assertFalse({A, D} in aretes)
        self.assertFalse({A, E} in aretes)

    def test_copie_graphe_non_oriente(self):
        graphe, sommets = self.get_graphes_non_orientes("Exemple de graphe non orienté")
        A, B, C, D, E, F = sommets
        graphe.setNom("nom")
        graphe_copie = graphe.copie()
        self.assertEqual("nom", graphe_copie.getNom())
        self.assertEqual("Exemple de graphe non orienté", graphe_copie.getCommentaire())
        self.assertEqual(set(sommets), graphe_copie.getSommets())
        aretes = graphe_copie.getAretes()
        self.assertEqual(len(aretes), 8)
        self.assertTrue({A, B} in aretes)
        self.assertTrue({A, C} in aretes)
        self.assertTrue({A, F} in aretes)
        self.assertTrue({B, E} in aretes)
        self.assertTrue({C, E} in aretes)
        self.assertTrue({C, D} in aretes)
        self.assertTrue({D, E} in aretes)
        self.assertTrue({D, F} in aretes)
        self.assertFalse({E,F} in aretes)
        self.assertFalse({B,D} in aretes)
        self.assertFalse({B,C} in aretes)
        self.assertFalse({A, D} in aretes)
        self.assertFalse({A, E} in aretes)

    def test_sous_graphe_graphe_non_oriente(self):
        graphe, sommets = self.get_graphes_non_orientes("Exemple de graphe non orienté")
        A, B, C, D, E, F = sommets
        sous_graphe = graphe.sous_graphe({A, B, C, E, F})
        self.assertEqual(5, len(sous_graphe.getSommets()))
        self.assertEqual({A, B, C, E, F}, sous_graphe.getSommets())
        self.assertEqual(5, len(sous_graphe.getAretes()))
        self.assertEqual([{A,B}, {A,C}, {A,F}, {B,E}, {C,E}], sous_graphe.getAretes())

    def test_graphe_partiel_graphe_non_oriente(self):
        graphe, sommets = self.get_graphes_non_orientes("Exemple de graphe non orienté")
        A, B, C, D, E, F = sommets
        graphe_partiel = graphe.graphe_partiel([{A,C}, {A,F}, {B,E}, {C,D}, {D,E}])
        self.assertEqual(6, len(graphe_partiel.getSommets()))
        self.assertEqual({A, B, C, D, E, F}, graphe_partiel.getSommets())
        self.assertEqual(5, len(graphe_partiel.getAretes()))
        self.assertTrue({A,C} in graphe_partiel.getAretes())
        self.assertTrue({A,F} in graphe_partiel.getAretes())
        self.assertTrue({B,E} in graphe_partiel.getAretes())
        self.assertTrue({C,D} in graphe_partiel.getAretes())
        self.assertTrue({D,E} in graphe_partiel.getAretes())

    def test_clique_et_est_clique(self):
        c = GrapheNonOriente.clique(5)
        self.assertEqual(5, len(c.getSommets()))
        s1, s2, s3, s4, s5 = c.getSommets()
        self.assertEqual(10, len(c.getAretes()))
        self.assertTrue({s1, s2} in c.getAretes())
        self.assertTrue({s1, s3} in c.getAretes())
        self.assertTrue({s1, s4} in c.getAretes())
        self.assertTrue({s1, s5} in c.getAretes())
        self.assertTrue({s2, s3} in c.getAretes())
        self.assertTrue({s2, s4} in c.getAretes())
        self.assertTrue({s2, s5} in c.getAretes())
        self.assertTrue({s3, s4} in c.getAretes())
        self.assertTrue({s3, s5} in c.getAretes())
        self.assertTrue({s4, s5} in c.getAretes())
        self.assertTrue(c.estClique())

    def test_ordre_et_taille_graphe_oriente(self):
        s1 = Sommet("1")
        s2 = Sommet("2")
        s3 = Sommet("3")
        s4 = Sommet("4")
        graphe1 = GrapheOriente(s1, s2, s3, p={(s1, s2):2, (s1, s3):5})
        self.assertEqual(3, graphe1.ordre())
        self.assertEqual(2, graphe1.taille())
        graphe2 = GrapheOriente(s1, s2, s3, s4)
        graphe2.lier(s1,s2,5)
        graphe2.lier(s1,s3,3)
        graphe2.lier(s2,s3,1)
        graphe2.lier(s2,s4,-1)
        graphe2.lier(s3,s4,0)
        self.assertEqual(4, graphe2.ordre())
        self.assertEqual(5, graphe2.taille())

    def test_sommets_et_arcs_graphe_oriente(self):
        graphe, sommets = self.get_graphes_orientes("'RCP101_Partie1_Graphes_et_Algorithmes' (RCP101), page 92")
        A, B, C, D, E, F = sommets
        self.assertEqual(set(sommets), graphe.getSommets())
        arcs = graphe.arcs()
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
        graphe, sommets = self.get_graphes_orientes("'RCP101_Partie1_Graphes_et_Algorithmes' (RCP101), page 92")
        A, B, C, D, E, F = sommets
        graphe.setNom("nom")
        graphe_copie = graphe.copie()
        self.assertEqual("nom", graphe_copie.getNom())
        self.assertEqual("'RCP101_Partie1_Graphes_et_Algorithmes' (RCP101), page 92", graphe_copie.getCommentaire())
        self.assertEqual(set(sommets), graphe_copie.getSommets())
        arcs = graphe_copie.arcs()
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
        graphe, sommets = self.get_graphes_orientes("'RCP101_Partie1_Graphes_et_Algorithmes' (RCP101), page 92")
        A, B, C, D, E, F = sommets
        sous_graphe = graphe.sous_graphe({A, B, C, E, F})
        self.assertEqual(5, len(sous_graphe.getSommets()))
        self.assertEqual({A, B, C, E, F}, sous_graphe.getSommets())
        self.assertEqual(6, len(sous_graphe.arcs()))
        self.assertEqual({(A,B), (A,E), (B,E), (B,C), (F,E), (C,F)}, sous_graphe.arcs())

    def test_graphe_partiel_graphe_oriente(self):
        graphe, sommets = self.get_graphes_orientes("'RCP101_Partie1_Graphes_et_Algorithmes' (RCP101), page 92")
        A, B, C, D, E, F = sommets
        graphe_partiel = graphe.graphe_partiel({(A,B), (B,C), (C,F), (F,E), (F,D)})
        self.assertEqual(6, len(graphe_partiel.getSommets()))
        self.assertEqual({A, B, C, D, E, F}, graphe_partiel.getSommets())
        self.assertEqual(5, len(graphe_partiel.arcs()))
        self.assertEqual({(A,B), (B,C), (C,F), (F,E), (F,D)}, graphe_partiel.arcs())

    def test_successeurs(self):
        graphe, sommets = self.get_graphes_orientes("'RCP101_Partie1_Graphes_et_Algorithmes' (RCP101), page 92")
        A, B, C, D, E, F = sommets
        self.assertEqual({B,E}, graphe.successeurs(A))
        self.assertEqual({C, E}, graphe.successeurs(B))
        self.assertEqual({F}, graphe.successeurs(C))
        self.assertEqual({B,C}, graphe.successeurs(D))
        self.assertEqual({D}, graphe.successeurs(E))
        self.assertEqual({D, E}, graphe.successeurs(F))

    def test_predecesseurs(self):
        graphe, sommets = self.get_graphes_orientes("'RCP101_Partie1_Graphes_et_Algorithmes' (RCP101), page 92")
        A, B, C, D, E, F = sommets
        self.assertEqual(set(), graphe.predecesseurs(A))
        self.assertEqual({A,D}, graphe.predecesseurs(B))
        self.assertEqual({B,D}, graphe.predecesseurs(C))
        self.assertEqual({E,F}, graphe.predecesseurs(D))
        self.assertEqual({A,B,F}, graphe.predecesseurs(E))
        self.assertEqual({C}, graphe.predecesseurs(F))

    def test_descendants(self):
        graphe, sommets = self.get_graphes_orientes("'RCP101_Partie1_Graphes_et_Algorithmes' (RCP101), page 85")
        S1, S2, S3, S4, S5, S6, S7, S8, S9 = sommets
        self.assertEqual({S3, S4, S5, S6, S7, S8, S9}, graphe.descendants(S3))
        self.assertEqual({S4, S6, S7, S8, S9}, graphe.descendants(S7))
        self.assertEqual({S4, S8}, graphe.descendants(S4))
        self.assertEqual({S8}, graphe.descendants(S8))

    def test_ascendants(self):
        graphe, sommets = self.get_graphes_orientes("'RCP101_Partie1_Graphes_et_Algorithmes' (RCP101), page 85")
        S1, S2, S3, S4, S5, S6, S7, S8, S9 = sommets
        self.assertEqual({S1, S3}, graphe.ascendants(S3))
        self.assertEqual({S1, S2, S3, S5, S7}, graphe.ascendants(S7))
        self.assertEqual({S1, S2, S3, S4, S5, S7}, graphe.ascendants(S4))
        self.assertEqual({S1, S2, S3, S4, S5, S6, S7, S8, S9}, graphe.ascendants(S8))

    def test_cfc0(self):
        graphe, sommets = self.get_graphes_orientes("RCP101 - ED1 - Exercice 1")
        A, B, C, D, E, F = sommets
        self.assertEqual({D,C}, graphe.cfc(D))
        self.assertEqual({A,B,E,F}, graphe.cfc(B))

    def test_cfcs0(self):
        graphe, sommets = self.get_graphes_orientes("RCP101 - ED1 - Exercice 1")
        A, B, C, D, E, F = sommets
        cfcs = graphe.cfcs()
        self.assertEqual(2, len(cfcs))
        self.assertTrue({D,C} in cfcs)
        self.assertTrue({A,B,E,F} in cfcs)
        self.assertFalse(graphe.estFortementConnexe())

    def test_cfc1(self):
        graphe, sommets = self.get_graphes_orientes("RCP101 - ED1 - Exercice 2 - Question 1")
        Ap, Am, Bp, Bm, Cp, Cm, Dp, Dm, Ep, Em = sommets
        self.assertEqual({Bm,Am, Dp, Cp}, graphe.cfc(Bm))
        self.assertEqual({Bp, Ap, Dm, Cm}, graphe.cfc(Bp))
        self.assertEqual({Ep}, graphe.cfc(Ep))
        self.assertEqual({Em}, graphe.cfc(Em))

    def test_cfcs1(self):
        graphe, sommets = self.get_graphes_orientes("RCP101 - ED1 - Exercice 2 - Question 1")
        Ap, Am, Bp, Bm, Cp, Cm, Dp, Dm, Ep, Em = sommets
        cfcs = graphe.cfcs()
        self.assertEqual(4, len(cfcs))
        self.assertTrue({Bm,Am, Dp, Cp} in cfcs)
        self.assertTrue({Bp, Ap, Dm, Cm} in cfcs)
        self.assertTrue({Ep} in cfcs)
        self.assertTrue({Em} in cfcs)
        self.assertFalse(graphe.estFortementConnexe())

    def test_cfc2(self):
        graphe, sommets = self.get_graphes_orientes("RCP101 - ED1 - Exercice 2 - Question 2")
        Ap, Am, Bp, Bm, Cp, Cm, Dp, Dm, Ep, Em, Fp, Fm = sommets
        self.assertEqual(set(sommets), graphe.cfc(Bm))
        self.assertEqual(set(sommets), graphe.cfc(Bp))
        self.assertEqual(set(sommets), graphe.cfc(Ep))
        self.assertEqual(set(sommets), graphe.cfc(Em))

    def test_cfcs2(self):
        graphe, sommets = self.get_graphes_orientes("RCP101 - ED1 - Exercice 2 - Question 2")
        cfcs = graphe.cfcs()
        self.assertEqual(1, len(cfcs))
        self.assertEqual(set(sommets), cfcs[0])
        self.assertTrue(graphe.estFortementConnexe())
        self.assertTrue(graphe.estFortementConnexe())

    def test_dijkstra(self):
        graphe, sommets = self.get_graphes_orientes("'RCP101_Partie1_Graphes_et_Algorithmes' (RCP101), page 74")
        S1, S2, S3, S4, S5, S6, S7, S8 = sommets
        pi, pere = graphe.dijkstra(S1)
        def chemin(s1,s2):
            if s1 == s2:
                return []
            return chemin(s1, pere[s2]) + [(pere[s2], s2)]
        self.assertEqual([(S1, S3), (S3, S4), (S4, S2)], chemin(S1,S2))
        self.assertEqual([(S1, S3), (S3, S5), (S5, S6), (S6, S7), (S7, S8)], chemin(S1,S8))
        self.assertEqual(5, pi[S8])
        self.assertEqual(4, pi[S7])
        self.assertEqual(3, pi[S6])
        self.assertEqual(6, pi[S2])

    def test_numerotation_topolgique_graphe_oriente(self):
        graphe, sommets = self.get_graphes_orientes("'RCP101_Partie1_Graphes_et_Algorithmes' (RCP101), page 85")
        num = graphe.numerotation_topolgique()
        self.assertEqual(set(sommets), set(num.keys()))
        self.assertEqual({1,2,3,4,5,6,7,8,9}, set(num.values()))

    def test_bellman(self):
        graphe, sommets = self.get_graphes_orientes("'RCP101_Partie1_Graphes_et_Algorithmes' (RCP101), page 85")
        S1, S2, S3, S4, S5, S6, S7, S8, S9 = sommets
        pere = graphe.bellman(S1)
        def chemin(s1,s2):
            if s1 == s2:
                return []
            return chemin(s1, pere[s2]) + [(pere[s2], s2)]
        self.assertEqual([(S1, S3), (S3, S5), (S5, S7), (S7, S6), (S6, S9)], chemin(S1, S9))
        self.assertEqual([(S1, S3), (S3, S5), (S5, S7), (S7, S8)], chemin(S1,S8))

    def test_plus_court_chemin(self):
        graphe, sommets = self.get_graphes_orientes("'RCP101_Partie1_Graphes_et_Algorithmes' (RCP101), page 92")
        A, B, C, D, E, F = sommets
        chemin, longueur = graphe.plus_court_chemin(A, D)
        self.assertEqual(4, len(chemin))
        self.assertEqual([(A,B), (B,C), (C,F), (F,D)], chemin)
        self.assertEqual(0, longueur)
        chemin, longueur = graphe.plus_court_chemin(B, D)
        self.assertEqual(3, len(chemin))
        self.assertEqual([(B,C), (C,F), (F,D)], chemin)
        self.assertEqual(-4, longueur)

    def get_graphes_orientes(self, nom):
        index = list(
            map(
                lambda g: g.getCommentaire(),
                graphes_orientes
            )
        ).index(nom)
        return graphes_orientes[index], listes_sommets_graphes_orientes[index]

    def get_graphes_non_orientes(self, nom):
        index = list(
            map(
                lambda g: g.getCommentaire(),
                graphes_non_orientes
            )
        ).index(nom)
        return graphes_non_orientes[index], listes_sommets_graphes_non_orientes[index]


if __name__ == '__main__':
    unittest.main()