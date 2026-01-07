# Fonction à tester
def propriete_disponible(nb_nuits):
    """
    Vérifie si une propriété est disponible selon la durée du séjour.
    - Séjours de 7 nuits ou plus : disponible (True)
    - Séjours plus courts : non disponible (False)
    
    Args:
        nb_nuits (int): Nombre de nuits demandées
    
    Returns:
        bool: True si disponible, False sinon
    """
    if nb_nuits >= 7:
        return True
    else:
        return False 