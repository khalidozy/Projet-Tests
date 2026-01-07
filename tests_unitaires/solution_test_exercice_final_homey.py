# Solution complète pour les tests du système de gestion Homey

import unittest
from exercice_final_homey import HomeyManager, Propriete

class TestHomeyManagerSolution(unittest.TestCase):
    """
    Solution complète des tests unitaires pour le système de gestion Homey.
    
    Cette classe démontre l'utilisation de tous les types d'assertions apprises
    dans un contexte d'application réelle mais simplifié.
    """
    
    def setUp(self):
        """
        Prépare un HomeyManager et quelques propriétés de test avant chaque test.
        
        Utilisation de setUp() pour éviter la duplication de code.
        """
        self.manager = HomeyManager()
        
        # Ajout de propriétés de test
        self.propriete1 = self.manager.ajouter_propriete(1, "Villa Sunset", 150.0)
        self.propriete2 = self.manager.ajouter_propriete(2, "Appartement Centre", 120.0)
        self.propriete3 = self.manager.ajouter_propriete(3, "Studio Plage", 80.0)
    
    def test_ajouter_propriete_valide(self):
        """
        Teste qu'une propriété valide peut être ajoutée avec succès.
        
        Utilise assertEqual pour vérifier les attributs de la propriété créée.
        """
        propriete = self.manager.ajouter_propriete(4, "Maison Campagne", 100.0)
        
        self.assertEqual(propriete.nom, "Maison Campagne")
        self.assertEqual(propriete.prix_par_nuit, 100.0)
        self.assertTrue(propriete.est_disponible)
    
    def test_ajouter_propriete_id_double(self):
        """
        Teste qu'ajouter une propriété avec un ID existant lève ValueError.
        
        Utilise assertRaises pour vérifier qu'une exception est levée.
        """
        with self.assertRaises(ValueError):
            self.manager.ajouter_propriete(1, "Propriété en double", 90.0)
    
    def test_ajouter_propriete_prix_negatif(self):
        """
        Teste qu'ajouter une propriété avec un prix négatif lève ValueError.
        """
        with self.assertRaises(ValueError):
            self.manager.ajouter_propriete(10, "Propriété gratuite", -50.0)
    
    def test_supprimer_propriete_existante(self):
        """
        Teste la suppression d'une propriété existante.
        
        Utilise assertTrue pour vérifier le succès.
        """
        resultat = self.manager.supprimer_propriete(1)
        self.assertTrue(resultat)
        
        # Vérification que la propriété n'existe plus
        propriete_supprimee = self.manager.obtenir_propriete(1)
        self.assertIsNone(propriete_supprimee)
    
    def test_supprimer_propriete_inexistante(self):
        """
        Teste la suppression d'une propriété inexistante.
        
        Utilise assertFalse pour vérifier l'échec de l'opération.
        """
        resultat = self.manager.supprimer_propriete(999)
        self.assertFalse(resultat)
    
    def test_obtenir_propriete_existante(self):
        """
        Teste l'obtention d'une propriété existante.
        
        Utilise assertIsNotNone pour vérifier le résultat.
        """
        propriete = self.manager.obtenir_propriete(2)
        self.assertIsNotNone(propriete)
        self.assertEqual(propriete.nom, "Appartement Centre")
    
    def test_obtenir_propriete_inexistante(self):
        """
        Teste l'obtention d'une propriété inexistante.
        
        Utilise assertIsNone pour vérifier qu'aucune propriété n'est retournée.
        """
        propriete = self.manager.obtenir_propriete(999)
        self.assertIsNone(propriete)
    
    def test_rechercher_par_nom_existant(self):
        """
        Teste la recherche de propriétés par nom.
        
        Utilise assertIn pour vérifier que les bonnes propriétés sont trouvées.
        """
        proprietes_villa = self.manager.rechercher_par_nom("Villa")
        
        self.assertIn(self.propriete1, proprietes_villa)
        self.assertNotIn(self.propriete2, proprietes_villa)
    
    def test_rechercher_par_nom_inexistant(self):
        """
        Teste la recherche d'un nom qui n'existe pas.
        """
        proprietes_inexistantes = self.manager.rechercher_par_nom("Château")
        self.assertEqual(len(proprietes_inexistantes), 0)
    
    def test_reserver_propriete_valide(self):
        """
        Teste une réservation valide.
        
        Utilise assertTrue et assertFalse pour vérifier le changement d'état.
        """
        resultat = self.manager.reserver_propriete(1)
        self.assertTrue(resultat)
        
        # Vérification que la propriété est maintenant indisponible
        self.assertFalse(self.propriete1.est_disponible)
    
    def test_reserver_propriete_inexistante(self):
        """
        Teste la réservation d'une propriété inexistante.
        
        Utilise assertFalse pour vérifier l'échec.
        """
        resultat = self.manager.reserver_propriete(999)
        self.assertFalse(resultat)
    
    def test_reserver_propriete_deja_reservee(self):
        """
        Teste la réservation d'une propriété déjà réservée.
        """
        # Première réservation
        premiere_reservation = self.manager.reserver_propriete(2)
        self.assertTrue(premiere_reservation)
        
        # Tentative de deuxième réservation
        deuxieme_reservation = self.manager.reserver_propriete(2)
        self.assertFalse(deuxieme_reservation)
    
    def test_obtenir_proprietes_disponibles(self):
        """
        Teste l'obtention de toutes les propriétés disponibles.
        
        Utilise assertIn et assertEqual pour vérifier le contenu de la liste.
        """
        # Toutes les propriétés sont initialement disponibles
        proprietes_disponibles = self.manager.obtenir_proprietes_disponibles()
        
        self.assertEqual(len(proprietes_disponibles), 3)
        self.assertIn(self.propriete1, proprietes_disponibles)
        self.assertIn(self.propriete2, proprietes_disponibles)
        self.assertIn(self.propriete3, proprietes_disponibles)
        
        # Réserve une propriété et teste à nouveau
        self.manager.reserver_propriete(1)
        proprietes_disponibles = self.manager.obtenir_proprietes_disponibles()
        
        self.assertEqual(len(proprietes_disponibles), 2)
        self.assertNotIn(self.propriete1, proprietes_disponibles)
    
    def test_obtenir_proprietes_reservees(self):
        """
        Teste l'obtention de toutes les propriétés réservées.
        """
        # Initialement, aucune propriété n'est réservée
        proprietes_reservees = self.manager.obtenir_proprietes_reservees()
        self.assertEqual(len(proprietes_reservees), 0)
        
        # Réserve une propriété
        self.manager.reserver_propriete(1)
        
        proprietes_reservees = self.manager.obtenir_proprietes_reservees()
        self.assertEqual(len(proprietes_reservees), 1)
        self.assertIn(self.propriete1, proprietes_reservees)
        self.assertNotIn(self.propriete2, proprietes_reservees)


if __name__ == "__main__":
    unittest.main(verbosity=2) 