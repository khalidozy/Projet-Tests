# Fonction à tester
def obtenir_equipements_propriete(standing):
    """
    Retourne les équipements selon le standing de la propriété Homey.
    - Standard : ["WiFi", "Parking"]
    - Premium : ["WiFi", "Parking", "Piscine"]
    
    Args:
        standing (str): Standing de la propriété ("Standard" ou "Premium")
    
    Returns:
        list: Liste des équipements disponibles
    """
    equipements = ["WiFi", "Parking"]
    
    if standing == "Premium":
        equipements.append("Piscine")
    
    return equipements 