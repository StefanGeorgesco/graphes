import unittest
from ordonnancement import *


class TestsOrdonnancement(unittest.TestCase):

    def test_calcul_dates(self):
        A = Tache("A", 2.0)
        B = Tache("B", 2.0)
        C = Tache("C", 2.0)
        D = Tache("D", 4.0)
        E = Tache("E", 1.0)
        F = Tache("F", 2.0)
        grapheMPM = GrapheMPM(A, B, C, D, E, F, prec=[(A,C), (A,D), (B,E), (D,E), (D,F)], nom="test", commentaire="test")
        grapheMPM.calculer_dates()
        self.assertEqual(0, grapheMPM._tache_debut.getPlus_tot())
        self.assertEqual(0, A.getPlus_tot())
        self.assertEqual(0, B.getPlus_tot())
        self.assertEqual(2, C.getPlus_tot())
        self.assertEqual(2, D.getPlus_tot())
        self.assertEqual(6, E.getPlus_tot())
        self.assertEqual(6, F.getPlus_tot())
        self.assertEqual(8, grapheMPM.date_de_fin())
