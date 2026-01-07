import unittest
from exercice_homey_equipements import obtenir_equipements_propriete

class TestEquipementsPropriete(unittest.TestCase):
    """
    Tests unitaires pour la fonction obtenir_equipements_propriete avec assertIn et assertNotIn.
    
    Cette classe démontre l'utilisation des assertions pour tester la présence
    ou l'absence d'éléments dans des collections.
    """
    
    def test_equipements_standard(self):
        """
        Teste qu'une propriété Standard contient les équipements de base.
        
        assertIn vérifie que les équipements sont présents dans la liste.
        """
        equipements = obtenir_equipements_propriete("Standard")
        
        self.assertIn("WiFi", equipements, "WiFi devrait être disponible en Standard")
        self.assertIn("Parking", equipements, "Parking devrait être disponible en Standard")
        self.assertNotIn("Piscine", equipements, "Piscine ne devrait pas être disponible en Standard")
    
    def test_equipements_premium(self):
        """
        Teste qu'une propriété Premium contient tous les équipements.
        
        assertIn vérifie que les équipements de base + premium sont présents.
        """
        equipements = obtenir_equipements_propriete("Premium")
        
        self.assertIn("WiFi", equipements, "WiFi devrait être disponible en Premium")
        self.assertIn("Parking", equipements, "Parking devrait être disponible en Premium")
        self.assertIn("Piscine", equipements, "Piscine devrait être disponible en Premium")


if __name__ == "__main__":
    unittest.main(verbosity=2) 