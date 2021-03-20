import unittest
from ordonnancement import *
from graphesMPM_exemples import graphes_MPM, listes_taches


class TestsOrdonnancement(unittest.TestCase):

    def setUp(self) -> None:
        self.graphesMPM = {}
        for nom in graphes_MPM.keys():
            self.graphesMPM.update({nom: (graphes_MPM[nom], listes_taches[nom])})

    def test_calcul_dates_sans_contrainte_debut_a_debut(self):
        grapheMPM, taches = self.graphesMPM["RCP101 - ED3 - Exerice 2"]
        A, B, C, D, E, F = taches
        self.assertEqual(0, grapheMPM.getTache_debut().getPlus_tot())
        self.assertEqual(0, A.getPlus_tot())
        self.assertEqual(0, B.getPlus_tot())
        self.assertEqual(2, C.getPlus_tot())
        self.assertEqual(2, D.getPlus_tot())
        self.assertEqual(6, E.getPlus_tot())
        self.assertEqual(6, F.getPlus_tot())
        self.assertEqual(8, grapheMPM.date_de_fin())
        self.assertEqual(0, A.getPlus_tard())
        self.assertEqual(5, B.getPlus_tard())
        self.assertEqual(6, C.getPlus_tard())
        self.assertEqual(2, D.getPlus_tard())
        self.assertEqual(7, E.getPlus_tard())
        self.assertEqual(6, F.getPlus_tard())
        self.assertEqual(0, grapheMPM.getTache_debut().getPlus_tard())
        self.assertEqual(0, grapheMPM.getTache_debut().marge_totale())
        self.assertEqual(0, A.marge_totale())
        self.assertEqual(5, B.marge_totale())
        self.assertEqual(4, C.marge_totale())
        self.assertEqual(0, D.marge_totale())
        self.assertEqual(1, E.marge_totale())
        self.assertEqual(0, F.marge_totale())
        taches_critiques = grapheMPM.taches_critiques()
        self.assertEqual({A,D,F}, set(taches_critiques))
        self.assertEqual(0, A.getMarge_libre())
        self.assertEqual(4, B.getMarge_libre())
        self.assertEqual(4, C.getMarge_libre())
        self.assertEqual(0, D.getMarge_libre())
        self.assertEqual(1, E.getMarge_libre())
        self.assertEqual(0, F.getMarge_libre())

