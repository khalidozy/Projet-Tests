# Fonctions à tester
def calculer_prix_base(nb_nuits, prix_par_nuit):
    """Calcule le prix de base d'un séjour."""
    return nb_nuits * prix_par_nuit


def appliquer_reduction(prix_base, nb_nuits):
    """
    Applique une réduction pour les séjours longs :
    - 7 nuits ou plus : 10% de réduction
    - Sinon : pas de réduction
    """
    if nb_nuits >= 7:
        return prix_base * 0.9  # 10% de réduction
    else:
        return prix_base


import unittest

# Classe de tests unitaires (à compléter)
class TestPrixSejour(unittest.TestCase):

    def setUp(self):
        """Initialisation des variables communes utilisées dans plusieurs tests."""
        # TODO : Initialiser les variables communes ici
        # Exemple :
        # - self.prix_nuit = 100.0
        # - self.nb_nuits_court = 3
        # - self.nb_nuits_long = 7
        pass


    # TODO : Ajouter les tests unitaires ici
    # 1. Écrire la fonction setUp() pour initialiser les variables communes.
    # 2. Tester le calcul du prix de base.
    # 3. Tester l'application de la réduction pour séjour long.
    # 4. Tester qu'il n'y a pas de réduction pour séjour court.

if __name__ == "__main__":
    unittest.main() 