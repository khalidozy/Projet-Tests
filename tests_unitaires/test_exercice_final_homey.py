# Tests unitaires pour le système de gestion Homey - À compléter par les étudiants

import unittest
from exercice_final_homey import HomeyManager, Propriete

class TestHomeyManager(unittest.TestCase):
    """
    Classe de tests unitaires pour le système de gestion Homey.
    
    TODO: Complétez les tests en utilisant toutes les assertions apprises :
    - assertEqual, assertTrue, assertFalse  
    - assertIsNone, assertIsNotNone
    - assertIn, assertNotIn
    - assertRaises
    """
    
    def setUp(self):
        """Prépare un HomeyManager et quelques propriétés de test avant chaque test."""
        # TODO: Initialiser self.manager et ajouter quelques propriétés de test
        pass
    
    # TODO: Tests pour ajouter_propriete()
    # 1. Test ajout propriété valide (assertEqual)
    # 2. Test ajout propriété avec ID en double (assertRaises)
    # 3. Test ajout propriété avec prix négatif (assertRaises)
    
    # TODO: Tests pour supprimer_propriete()
    # 4. Test suppression propriété existante (assertTrue)
    # 5. Test suppression propriété inexistante (assertFalse)
    
    # TODO: Tests pour obtenir_propriete()
    # 6. Test obtention propriété existante (assertIsNotNone)
    # 7. Test obtention propriété inexistante (assertIsNone)
    
    # TODO: Tests pour rechercher_par_nom()
    # 8. Test recherche nom existant (assertIn)
    # 9. Test recherche nom inexistant (liste vide)
    
    # TODO: Tests pour reserver_propriete()
    # 10. Test réservation valide (assertTrue)
    # 11. Test réservation propriété inexistante (assertFalse)
    # 12. Test réservation propriété déjà réservée (assertFalse)
    
    # TODO: Tests pour les listes de propriétés
    # 13. Test obtenir propriétés disponibles (assertIn/assertNotIn)
    # 14. Test obtenir propriétés réservées (assertIn/assertNotIn)


if __name__ == "__main__":
    unittest.main() 