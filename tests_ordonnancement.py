import unittest
from graphes_ordonnacement_exemples import graphes_MPM, listes_taches_MPM


class TestsOrdonnancementMPM(unittest.TestCase):

    def setUp(self) -> None:
        self.graphesMPM = {}
        for nom in graphes_MPM.keys():
            self.graphesMPM.update({nom: (graphes_MPM[nom], listes_taches_MPM[nom])})

    def test_calcul_dates_sans_contrainte_debut_a_debut(self):
        grapheMPM, taches = self.graphesMPM["RCP101 - ED3 - Exerice 2"]
        A, B, C, D, E, F = taches
        self.assertEqual(0.0, grapheMPM.tache_debut().plus_tot())
        self.assertEqual(0.0, A.plus_tot())
        self.assertEqual(0.0, B.plus_tot())
        self.assertEqual(2.0, C.plus_tot())
        self.assertEqual(2.0, D.plus_tot())
        self.assertEqual(6.0, E.plus_tot())
        self.assertEqual(6.0, F.plus_tot())
        self.assertEqual(8.0, grapheMPM.date_de_fin())
        self.assertEqual(0.0, A.plus_tard())
        self.assertEqual(5.0, B.plus_tard())
        self.assertEqual(6.0, C.plus_tard())
        self.assertEqual(2.0, D.plus_tard())
        self.assertEqual(7.0, E.plus_tard())
        self.assertEqual(6.0, F.plus_tard())
        self.assertEqual(0.0, grapheMPM.tache_debut().plus_tard())
        self.assertEqual(0.0, grapheMPM.tache_debut().marge_totale())
        self.assertEqual(0.0, A.marge_totale())
        self.assertEqual(5.0, B.marge_totale())
        self.assertEqual(4.0, C.marge_totale())
        self.assertEqual(0.0, D.marge_totale())
        self.assertEqual(1.0, E.marge_totale())
        self.assertEqual(0.0, F.marge_totale())
        taches_critiques = grapheMPM.taches_critiques()
        self.assertEqual({A, D, F}, set(taches_critiques))
        self.assertEqual(0.0, A.marge_libre())
        self.assertEqual(4.0, B.marge_libre())
        self.assertEqual(4.0, C.marge_libre())
        self.assertEqual(0.0, D.marge_libre())
        self.assertEqual(1.0, E.marge_libre())
        self.assertEqual(0.0, F.marge_libre())

    def test_calcul_dates_avec_contraintes_debut_a_debut(self):
        grapheMPM, taches = self.graphesMPM["RCP101 - ED3 - Exerice 1"]
        A, B, C, D, E, F, G, H, I, J, K, L, M, N, O = taches
        self.assertEqual(0.0, grapheMPM.tache_debut().plus_tot())
        self.assertEqual(0.0, A.plus_tot())
        self.assertEqual(0.0, B.plus_tot())
        self.assertEqual(20.0, C.plus_tot())
        self.assertEqual(50.0, D.plus_tot())
        self.assertEqual(45.0, E.plus_tot())
        self.assertEqual(70.0, F.plus_tot())
        self.assertEqual(190.0, grapheMPM.date_de_fin())
        self.assertEqual(0.0, A.plus_tard())
        self.assertEqual(30.0, B.plus_tard())
        self.assertEqual(20.0, C.plus_tard())
        self.assertEqual(65.0, D.plus_tard())
        self.assertEqual(45.0, E.plus_tard())
        self.assertEqual(75.0, F.plus_tard())
        self.assertEqual(0.0, grapheMPM.tache_debut().plus_tard())
        self.assertEqual(0.0, grapheMPM.tache_debut().marge_totale())
        self.assertEqual(0.0, A.marge_totale())
        self.assertEqual(30.0, B.marge_totale())
        self.assertEqual(0.0, C.marge_totale())
        self.assertEqual(15.0, D.marge_totale())
        self.assertEqual(0.0, E.marge_totale())
        self.assertEqual(5.0, F.marge_totale())
        self.assertEqual(0.0, G.marge_totale())
        self.assertEqual(25.0, H.marge_totale())
        self.assertEqual(55.0, I.marge_totale())
        self.assertEqual(5.0, J.marge_totale())
        self.assertEqual(50.0, K.marge_totale())
        self.assertEqual(0.0, L.marge_totale())
        self.assertEqual(0.0, M.marge_totale())
        self.assertEqual(5.0, N.marge_totale())
        self.assertEqual(0.0, O.marge_totale())
        taches_critiques = grapheMPM.taches_critiques()
        self.assertEqual({A, C, E, G, L, M, O}, set(taches_critiques))
        self.assertEqual(0.0, A.marge_libre())
        self.assertEqual(30.0, B.marge_libre())
        self.assertEqual(0.0, C.marge_libre())
        self.assertEqual(0.0, D.marge_libre())
        self.assertEqual(0.0, E.marge_libre())
        self.assertEqual(0.0, F.marge_libre())
        self.assertEqual(0.0, G.marge_libre())
        self.assertEqual(20.0, H.marge_libre())
        self.assertEqual(5.0, I.marge_libre())
        self.assertEqual(5.0, J.marge_libre())
        self.assertEqual(50.0, K.marge_libre())
        self.assertEqual(0.0, L.marge_libre())
        self.assertEqual(0.0, M.marge_libre())
        self.assertEqual(0.0, N.marge_libre())
        self.assertEqual(0.0, O.marge_libre())


class TestsOrdonnancementPERT(unittest.TestCase):

    def setUp(self) -> None:
        self.graphesPERT = {}
        for nom in graphe_MPM.keys():
            self.graphesMPM.update({nom: (graphe_MPM[nom], listes_taches_MPM[nom])})

