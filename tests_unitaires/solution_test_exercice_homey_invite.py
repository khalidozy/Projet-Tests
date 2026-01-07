import unittest
from exercice_homey_invite import obtenir_responsable_proprietaire

class TestResponsablePropriete(unittest.TestCase):
    """
    Tests unitaires pour la fonction obtenir_responsable_proprietaire avec assertIsNone et assertIsNotNone.
    
    Cette classe démontre l'utilisation des assertions pour tester :
    - assertIsNone : quand on s'attend à recevoir None
    - assertIsNotNone : quand on s'attend à recevoir un objet
    """
    
    def test_propriete_avec_responsable(self):
        """
        Teste qu'une propriété avec responsable retourne un objet.
        
        assertIsNotNone est utilisé car on s'attend à recevoir un dictionnaire
        avec les informations du responsable.
        """
        resultat = obtenir_responsable_proprietaire(1)
        self.assertIsNotNone(resultat, "Propriété ID 1 devrait avoir un responsable")
        
        resultat = obtenir_responsable_proprietaire(2)
        self.assertIsNotNone(resultat, "Propriété ID 2 devrait avoir un responsable")
    
    def test_propriete_sans_responsable(self):
        """
        Teste qu'une propriété sans responsable retourne None.
        
        assertIsNone est utilisé car on s'attend à None pour les propriétés
        sans responsable assigné.
        """
        resultat = obtenir_responsable_proprietaire(3)
        self.assertIsNone(resultat, "Propriété ID 3 ne devrait pas avoir de responsable")
        
        resultat = obtenir_responsable_proprietaire(99)
        self.assertIsNone(resultat, "Propriété ID 99 ne devrait pas avoir de responsable")


if __name__ == "__main__":
    unittest.main(verbosity=2) 