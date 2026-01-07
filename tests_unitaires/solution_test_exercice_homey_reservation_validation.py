import unittest
from exercice_homey_reservation_validation import calculer_prix_total

class TestCalculPrix(unittest.TestCase):
    """
    Tests unitaires pour la fonction calculer_prix_total avec assertRaises.
    
    Cette classe démontre l'utilisation de assertRaises pour tester que
    les fonctions lèvent les bonnes exceptions dans les bonnes conditions.
    """
    
    def test_calcul_prix_normal(self):
        """
        Teste le calcul normal du prix sans exception.
        
        Ce test vérifie d'abord que la fonction fonctionne correctement.
        """
        prix_total = calculer_prix_total(5, 80.0)
        self.assertEqual(prix_total, 400.0, "5 nuits à 80€ devraient coûter 400€")
    
    def test_nombre_nuits_negatif(self):
        """
        Teste qu'un nombre de nuits négatif lève une ValueError.
        
        assertRaises vérifie qu'une exception ValueError est levée.
        """
        with self.assertRaises(ValueError) as context:
            calculer_prix_total(-3, 80.0)
        
        self.assertIn("négatif", str(context.exception))
    
    def test_prix_par_nuit_negatif(self):
        """
        Teste qu'un prix par nuit négatif lève une ValueError.
        """
        with self.assertRaises(ValueError):
            calculer_prix_total(5, -50.0)
    
    def test_prix_par_nuit_zero(self):
        """
        Teste qu'un prix par nuit de zéro lève une ValueError.
        """
        self.assertRaises(ValueError, calculer_prix_total, 3, 0.0)


if __name__ == "__main__":
    unittest.main(verbosity=2) 