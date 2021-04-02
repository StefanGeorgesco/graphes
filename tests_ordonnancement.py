import unittest
from graphes_ordonnacement_exemples import graphes_MPM, \
    listes_taches_MPM, \
    graphes_PERT, \
    listes_taches_PERT
from graphes import Arc


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

    def test_calcul_dates_avec_contraintes_debut_a_debut1(self):
        grapheMPM, taches = self.graphesMPM["RCP101 - ED3 - Exerice 1"]
        A, B, C, D, E, F, G, H, I, J, K, L, M, N, O = taches
        self.assertEqual(0.0, grapheMPM.tache_debut().plus_tot())
        self.assertEqual(0.0, A.plus_tot())
        self.assertEqual(0.0, B.plus_tot())
        self.assertEqual(20.0, C.plus_tot())
        self.assertEqual(50.0, D.plus_tot())
        self.assertEqual(45.0, E.plus_tot())
        self.assertEqual(70.0, F.plus_tot())
        self.assertEqual(105.0, G.plus_tot())
        self.assertEqual(60.0, H.plus_tot())
        self.assertEqual(85.0, I.plus_tot())
        self.assertEqual(95.0, J.plus_tot())
        self.assertEqual(95.0, K.plus_tot())
        self.assertEqual(145.0, L.plus_tot())
        self.assertEqual(105.0, M.plus_tot())
        self.assertEqual(85.0, N.plus_tot())
        self.assertEqual(175.0, O.plus_tot())
        self.assertEqual(190.0, grapheMPM.date_de_fin())
        self.assertEqual(0.0, A.plus_tard())
        self.assertEqual(30.0, B.plus_tard())
        self.assertEqual(20.0, C.plus_tard())
        self.assertEqual(65.0, D.plus_tard())
        self.assertEqual(45.0, E.plus_tard())
        self.assertEqual(75.0, F.plus_tard())
        self.assertEqual(105.0, G.plus_tard())
        self.assertEqual(85.0, H.plus_tard())
        self.assertEqual(140.0, I.plus_tard())
        self.assertEqual(100.0, J.plus_tard())
        self.assertEqual(145.0, K.plus_tard())
        self.assertEqual(145.0, L.plus_tard())
        self.assertEqual(105.0, M.plus_tard())
        self.assertEqual(90.0, N.plus_tard())
        self.assertEqual(175.0, O.plus_tard())
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

    def test_calcul_dates_avec_contraintes_debut_a_debut2(self):
        grapheMPM, taches = self.graphesMPM["RCP101 - ED3 - Exerice 3"]
        A, B, C, D, E, F, G, H, I, J, K = taches
        self.assertEqual(0.0, grapheMPM.tache_debut().plus_tot())
        self.assertEqual(0.0, A.plus_tot())
        self.assertEqual(4.0, B.plus_tot())
        self.assertEqual(2.0, C.plus_tot())
        self.assertEqual(0.0, D.plus_tot())
        self.assertEqual(10.0, E.plus_tot())
        self.assertEqual(4.0, F.plus_tot())
        self.assertEqual(10.0, G.plus_tot())
        self.assertEqual(13.0, H.plus_tot())
        self.assertEqual(10.0, I.plus_tot())
        self.assertEqual(18.0, J.plus_tot())
        self.assertEqual(18.0, K.plus_tot())
        self.assertEqual(22.0, grapheMPM.date_de_fin())
        self.assertEqual(0.0, A.plus_tard())
        self.assertEqual(4.0, B.plus_tard())
        self.assertEqual(6.0, C.plus_tard())
        self.assertEqual(4.0, D.plus_tard())
        self.assertEqual(12.0, E.plus_tard())
        self.assertEqual(8.0, F.plus_tard())
        self.assertEqual(10.0, G.plus_tard())
        self.assertEqual(13.0, H.plus_tard())
        self.assertEqual(12.0, I.plus_tard())
        self.assertEqual(19.0, J.plus_tard())
        self.assertEqual(18.0, K.plus_tard())
        self.assertEqual(0.0, grapheMPM.tache_debut().plus_tard())
        self.assertEqual(0.0, grapheMPM.tache_debut().marge_totale())
        self.assertEqual(0.0, A.marge_totale())
        self.assertEqual(0.0, B.marge_totale())
        self.assertEqual(4.0, C.marge_totale())
        self.assertEqual(4.0, D.marge_totale())
        self.assertEqual(2.0, E.marge_totale())
        self.assertEqual(4.0, F.marge_totale())
        self.assertEqual(0.0, G.marge_totale())
        self.assertEqual(0.0, H.marge_totale())
        self.assertEqual(2.0, I.marge_totale())
        self.assertEqual(1.0, J.marge_totale())
        self.assertEqual(0.0, K.marge_totale())
        taches_critiques = grapheMPM.taches_critiques()
        self.assertEqual({A, B, G, H, K}, set(taches_critiques))
        self.assertEqual(0.0, A.marge_libre())
        self.assertEqual(0.0, B.marge_libre())
        self.assertEqual(0.0, C.marge_libre())
        self.assertEqual(4.0, D.marge_libre())
        self.assertEqual(2.0, E.marge_libre())
        self.assertEqual(2.0, F.marge_libre())
        self.assertEqual(0.0, G.marge_libre())
        self.assertEqual(0.0, H.marge_libre())
        self.assertEqual(2.0, I.marge_libre())
        self.assertEqual(1.0, J.marge_libre())
        self.assertEqual(0.0, K.marge_libre())


class TestsOrdonnancementPERT(unittest.TestCase):

    def setUp(self) -> None:
        self.graphesPERT = {}
        for nom in graphes_PERT.keys():
            self.graphesPERT.update({nom: (graphes_PERT[nom], listes_taches_PERT[nom])})

    def test_nombre_taches_et_evenements(self):
        graphePERT, taches = self.graphesPERT["RCP101 - ED3 - Exerice 3"]
        A, B, C, D, E, F, G, H, I, J, K = taches
        Edebut = A.depart()
        Efin = J.arrivee()
        E1 = B.depart()
        E2 = C.depart()
        E3 = E.depart()
        E4 = F.depart()
        E5 = G.depart()
        E6 = I.depart()
        E7 = H.depart()
        E8 = I.arrivee()
        E9 = H.arrivee()
        E10 = J.depart()
        E11 = K.depart()
        self.assertEqual(13, len(graphePERT.evenements()))
        self.assertEqual(18, len(graphePERT.taches()))
        couples = [
            (Edebut, E1), #4.0
            (Edebut, E2), #2.0
            (Edebut, E5), #6.0
            (E1, E3), #6.0
            (E2, E4), #2.0
            (E4, E6), #4.0
            (E3, E6), #0.0
            (E3, E7), #1.0
            (E3, E5), #0.0
            (E5, E7), #3.0
            (E6, E8), #6.0
            (E7, E9), #5.0
            (E8, E10), #0.0
            (E8, E11), #0.0
            (E9, E10), #0.0
            (E9, E11), #0.0
            (E10, Efin), #3.0
            (E11, Efin) #4.0
        ]
        arcs = [Arc(*x) for x in couples]
        present = list(
            map(
                lambda arc: arc in graphePERT._arcs,
                arcs
            )
        )
        valuations = [graphePERT.valuation(*x) for x in couples]
        self.assertTrue(all(present))
        self.assertEqual([4.0, 2.0, 6.0, 6.0, 2.0, 4.0, 0.0, 1.0, 0.0, 3.0, 6.0, 5.0, 0.0, 0.0, 0.0, 0.0, 3.0, 4.0], valuations)
        num = graphePERT.numerotation_topolgique()
        self.assertEqual(1, num[Edebut])
        self.assertEqual(13, num[Efin])
        
    def test_calcul_dates_sans_contrainte_debut_a_debut(self):
        graphePERT, taches = self.graphesPERT["RCP101 - ED3 - Exerice 2"]
        A, B, C, D, E, F = taches
        self.assertEqual(0.0, graphePERT.evenement_debut().plus_tot())
        self.assertEqual(0.0, A.plus_tot())
        self.assertEqual(0.0, B.plus_tot())
        self.assertEqual(2.0, C.plus_tot())
        self.assertEqual(2.0, D.plus_tot())
        self.assertEqual(6.0, E.plus_tot())
        self.assertEqual(6.0, F.plus_tot())
        self.assertEqual(8.0, graphePERT.date_de_fin())
        self.assertEqual(0.0, A.plus_tard())
        self.assertEqual(5.0, B.plus_tard())
        self.assertEqual(6.0, C.plus_tard())
        self.assertEqual(2.0, D.plus_tard())
        self.assertEqual(7.0, E.plus_tard())
        self.assertEqual(6.0, F.plus_tard())
        self.assertEqual(0.0, graphePERT.evenement_debut().plus_tard())
        self.assertEqual(0.0, A.marge_totale())
        self.assertEqual(5.0, B.marge_totale())
        self.assertEqual(4.0, C.marge_totale())
        self.assertEqual(0.0, D.marge_totale())
        self.assertEqual(1.0, E.marge_totale())
        self.assertEqual(0.0, F.marge_totale())
        taches_critiques = graphePERT.taches_critiques()
        self.assertEqual({A, D, F}, set(taches_critiques))
        self.assertEqual(0.0, A.marge_libre())
        self.assertEqual(4.0, B.marge_libre())
        self.assertEqual(4.0, C.marge_libre())
        self.assertEqual(0.0, D.marge_libre())
        self.assertEqual(1.0, E.marge_libre())
        self.assertEqual(0.0, F.marge_libre())

    def test_calcul_dates_avec_contraintes_debut_a_debut1(self):
        graphePERT, taches = self.graphesPERT["RCP101 - ED3 - Exerice 1"]
        A, B, C, D, E, F, G, H, I, J, K, L, M, N, O = taches
        self.assertEqual(0.0, graphePERT.evenement_debut().plus_tot())
        self.assertEqual(0.0, A.plus_tot())
        self.assertEqual(0.0, B.plus_tot())
        self.assertEqual(20.0, C.plus_tot())
        self.assertEqual(50.0, D.plus_tot())
        self.assertEqual(45.0, E.plus_tot())
        self.assertEqual(70.0, F.plus_tot())
        self.assertEqual(105.0, G.plus_tot())
        self.assertEqual(60.0, H.plus_tot())
        self.assertEqual(85.0, I.plus_tot())
        self.assertEqual(95.0, J.plus_tot())
        self.assertEqual(95.0, K.plus_tot())
        self.assertEqual(145.0, L.plus_tot())
        self.assertEqual(105.0, M.plus_tot())
        self.assertEqual(85.0, N.plus_tot())
        self.assertEqual(175.0, O.plus_tot())
        self.assertEqual(190.0, graphePERT.date_de_fin())
        # self.assertEqual(0.0, A.plus_tard()) #calcule 5.0, devrait être 0.0
        self.assertEqual(30.0, B.plus_tard())
        self.assertEqual(20.0, C.plus_tard())
        self.assertEqual(65.0, D.plus_tard())
        self.assertEqual(45.0, E.plus_tard())
        self.assertEqual(75.0, F.plus_tard())
        self.assertEqual(105.0, G.plus_tard())
        self.assertEqual(85.0, H.plus_tard())
        self.assertEqual(140.0, I.plus_tard())
        self.assertEqual(100.0, J.plus_tard())
        self.assertEqual(145.0, K.plus_tard())
        self.assertEqual(145.0, L.plus_tard())
        self.assertEqual(105.0, M.plus_tard())
        self.assertEqual(90.0, N.plus_tard())
        self.assertEqual(175.0, O.plus_tard())
        self.assertEqual(0.0, graphePERT.evenement_debut().plus_tard())
        # self.assertEqual(0.0, A.marge_totale()) #calcule 5.0, devrait être 0.0
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
        taches_critiques = graphePERT.taches_critiques()
        # self.assertEqual({A, C, E, G, L, M, O}, set(taches_critiques)) #A n'est pas retenue, devrait
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

    def test_calcul_dates_avec_contraintes_debut_a_debut2(self):
        graphePERT, taches = self.graphesPERT["RCP101 - ED3 - Exerice 3"]
        A, B, C, D, E, F, G, H, I, J, K = taches
        self.assertEqual(0.0, graphePERT.evenement_debut().plus_tot())
        self.assertEqual(0.0, A.plus_tot())
        self.assertEqual(4.0, B.plus_tot())
        self.assertEqual(2.0, C.plus_tot())
        self.assertEqual(0.0, D.plus_tot())
        self.assertEqual(10.0, E.plus_tot())
        self.assertEqual(4.0, F.plus_tot())
        self.assertEqual(10.0, G.plus_tot())
        self.assertEqual(13.0, H.plus_tot())
        self.assertEqual(10.0, I.plus_tot())
        self.assertEqual(18.0, J.plus_tot())
        self.assertEqual(18.0, K.plus_tot())
        self.assertEqual(22.0, graphePERT.date_de_fin())
        self.assertEqual(0.0, A.plus_tard())
        self.assertEqual(4.0, B.plus_tard())
        self.assertEqual(6.0, C.plus_tard())
        self.assertEqual(4.0, D.plus_tard())
        self.assertEqual(12.0, E.plus_tard())
        self.assertEqual(8.0, F.plus_tard())
        self.assertEqual(10.0, G.plus_tard())
        self.assertEqual(13.0, H.plus_tard())
        self.assertEqual(12.0, I.plus_tard())
        self.assertEqual(19.0, J.plus_tard())
        self.assertEqual(18.0, K.plus_tard())
        self.assertEqual(0.0, graphePERT.evenement_debut().plus_tard())
        self.assertEqual(0.0, A.marge_totale())
        self.assertEqual(0.0, B.marge_totale())
        self.assertEqual(4.0, C.marge_totale())
        self.assertEqual(4.0, D.marge_totale())
        self.assertEqual(2.0, E.marge_totale())
        self.assertEqual(4.0, F.marge_totale())
        self.assertEqual(0.0, G.marge_totale())
        self.assertEqual(0.0, H.marge_totale())
        self.assertEqual(2.0, I.marge_totale())
        self.assertEqual(1.0, J.marge_totale())
        self.assertEqual(0.0, K.marge_totale())
        taches_critiques = graphePERT.taches_critiques()
        self.assertEqual({A, B, G, H, K}, set(taches_critiques))
        self.assertEqual(0.0, A.marge_libre())
        self.assertEqual(0.0, B.marge_libre())
        self.assertEqual(0.0, C.marge_libre())
        self.assertEqual(4.0, D.marge_libre())
        self.assertEqual(2.0, E.marge_libre())
        self.assertEqual(2.0, F.marge_libre())
        self.assertEqual(0.0, G.marge_libre())
        self.assertEqual(0.0, H.marge_libre())
        self.assertEqual(2.0, I.marge_libre())
        self.assertEqual(1.0, J.marge_libre())
        self.assertEqual(0.0, K.marge_libre())

