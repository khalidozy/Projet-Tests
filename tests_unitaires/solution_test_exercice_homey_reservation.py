import unittest
from exercice_homey_reservation import propriete_disponible

class TestDisponibilitePropriete(unittest.TestCase):
    """
    Tests unitaires pour la fonction propriete_disponible avec assertTrue et assertFalse.
    
    Cette classe démontre l'utilisation des assertions assertTrue et assertFalse
    pour valider des fonctions qui retournent des valeurs booléennes.
    """
    
    def test_sejour_long_disponible(self):
        """
        Teste qu'un séjour long est disponible.
        
        assertTrue est utilisé car on s'attend à True pour les séjours >= 7 nuits.
        """
        resultat = propriete_disponible(7)
        self.assertTrue(resultat, "Un séjour de 7 nuits devrait être disponible")
        
        resultat = propriete_disponible(10)
        self.assertTrue(resultat, "Un séjour de 10 nuits devrait être disponible")
    
    def test_sejour_court_non_disponible(self):
        """
        Teste qu'un séjour court n'est pas disponible.
        
        assertFalse est utilisé car on s'attend à False pour les séjours < 7 nuits.
        """
        resultat = propriete_disponible(3)
        self.assertFalse(resultat, "Un séjour de 3 nuits ne devrait pas être disponible")
        
        resultat = propriete_disponible(6)
        self.assertFalse(resultat, "Un séjour de 6 nuits ne devrait pas être disponible")


if __name__ == "__main__":
    unittest.main(verbosity=2) 