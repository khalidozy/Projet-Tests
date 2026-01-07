# Contexte : Homey calcule un prix par nuit pour une réservation.
# Règles simplifiées :
# - week_end : +15 % (vendredi/samedi/dimanche)
# - long_sejour : -10 % (séjour >= 7 nuits)
# NB : pas de "else" -> chaque if a 2 issues (Vrai/Faux)

def devis_par_nuit(tarif_base: float, week_end: bool, long_sejour: bool) -> float:
    total = tarif_base
    if week_end:        # Décision 1 (Vrai / Faux)
        total += tarif_base * 0.15
    if long_sejour:     # Décision 2 (Vrai / Faux)
        total -= tarif_base * 0.10
    # Arrondi commercial façon Homey (2 décimales)
    return round(total, 2)