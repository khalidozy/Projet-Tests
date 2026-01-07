# Fonction à tester
def obtenir_responsable_proprietaire(id_propriete):
    """
    Retourne le responsable d'une propriété selon son ID.
    - ID 1 ou 2 : retourne un responsable (dict)
    - Autres ID : pas de responsable assigné (None)
    
    Args:
        id_propriete (int): Identifiant de la propriété
    
    Returns:
        dict ou None: Informations du responsable ou None
    """
    if id_propriete in [1, 2]:
        return {"nom": "Jean Dupont", "telephone": "0123456789"}
    else:
        return None 