# Fonction à tester
def calculer_prix_total(nb_nuits, prix_par_nuit):
    """
    Calcule le prix total d'un séjour sur la plateforme Homey.
    - Si nb_nuits est négatif, lève ValueError
    - Si prix_par_nuit est négatif ou nul, lève ValueError
    
    Args:
        nb_nuits (int): Nombre de nuits du séjour
        prix_par_nuit (float): Prix par nuit de la propriété
    
    Returns:
        float: Prix total du séjour
    """
    if nb_nuits < 0:
        raise ValueError("Le nombre de nuits ne peut pas être négatif")
    
    if prix_par_nuit <= 0:
        raise ValueError("Le prix par nuit doit être positif")
    
    return nb_nuits * prix_par_nuit 