import unittest
from exercice_homey_pricing import calculer_prix_base, appliquer_reduction

class TestPrixSejour(unittest.TestCase):
    """
    Tests unitaires pour les fonctions de prix avec utilisation de setUp.
    
    Cette classe démontre l'utilisation de la méthode setUp() pour :
    - Initialiser des variables communes à plusieurs tests
    - Éviter la duplication de code
    """

    def setUp(self):
        """
        Initialisation des variables communes utilisées dans plusieurs tests.
        
        La méthode setUp() est appelée automatiquement avant CHAQUE test.
        """
        # Variables communes utilisées dans plusieurs tests
        self.prix_nuit = 100.0
        self.nb_nuits_court = 3    # Pas de réduction
        self.nb_nuits_long = 7     # Avec réduction

    def test_calcul_prix_base(self):
        """
        Teste le calcul du prix de base.
        
        Utilise les variables du setUp() au lieu de valeurs en dur.
        """
        prix = calculer_prix_base(self.nb_nuits_court, self.prix_nuit)
        self.assertEqual(prix, 300.0, "3 nuits à 100€ = 300€")

    def test_pas_de_reduction_sejour_court(self):
        """
        Teste qu'aucune réduction n'est appliquée pour les séjours courts.
        """
        prix_base = calculer_prix_base(self.nb_nuits_court, self.prix_nuit)
        prix_final = appliquer_reduction(prix_base, self.nb_nuits_court)
        self.assertEqual(prix_final, prix_base, "Pas de réduction pour séjour court")

    def test_reduction_sejour_long(self):
        """
        Teste qu'une réduction est appliquée pour les séjours longs.
        """
        prix_base = calculer_prix_base(self.nb_nuits_long, self.prix_nuit)
        prix_final = appliquer_reduction(prix_base, self.nb_nuits_long)
        prix_attendu = prix_base * 0.9  # 10% de réduction
        self.assertEqual(prix_final, prix_attendu, "10% de réduction pour 7+ nuits")


if __name__ == "__main__":
    unittest.main(verbosity=2) 