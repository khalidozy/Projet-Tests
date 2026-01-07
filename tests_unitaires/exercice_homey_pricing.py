# Fonction à tester
def calculer_prix_nuit(prix_base, nb_nuits, frais_menage=50):
    """
    Calcule le prix total d'un séjour sur la plateforme Homey :
    - Un prix de base par nuit
    - Le nombre de nuits
    - Des frais de ménage (par défaut 50€)
    """
    return (prix_base * nb_nuits) + frais_menage


# TODO : Écrire une classe de tests unitaires avec unittest
# 1. Tester un prix de base sans frais de ménage supplémentaires.
# 2. Tester un prix de base avec des frais de ménage personnalisés.
# 3. Tester un séjour de plusieurs nuits.

if __name__ == "__main__":
    pass

