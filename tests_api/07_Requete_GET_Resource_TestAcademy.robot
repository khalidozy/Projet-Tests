*** Settings ***
Library    RequestsLibrary    # Import de la bibliothèque pour les requêtes HTTP
Library    Collections        # Import de la bibliothèque pour la manipulation de collections

*** Variables ***
${Base_URL}      https://mock-api-h0g7.onrender.com/    # URL de base de l'API
${API_KEY}       Cle-API-ReqRes-test-academy            # Clé API pour l'authentification
${ResourceId}    2                                      # ID de la ressource à récupérer

*** Test Cases ***
Test Requete GET Single Resource
    # Création des en-têtes avec l'authentification
    &{headers}=    Create Dictionary    Authorization=Bearer ${API_KEY}    # Prépare l'authentification Bearer

    # Envoi de la requête GET pour récupérer une ressource spécifique
    ${Reponse}=    GET    ${Base_URL}api/unknown/${ResourceId}    headers=${headers}    expected_status=200    # Envoie la requête GET et attend un statut 200 OK

    # Log de la réponse pour vérification
    Log    ${Reponse.json()}    # Affiche le corps de la réponse JSON

    # Vérification que la réponse contient les données de la ressource
    Dictionary Should Contain Key    ${Reponse.json()}    data    # Vérifie la présence de la clé 'data'
    
    # Validation de l'ID de la ressource retournée
    ${data}=    Get From Dictionary    ${Reponse.json()}    data      # Récupère l'objet 'data'
    ${id_recu}=    Get From Dictionary    ${data}    id               # Récupère l'ID
    Should Be Equal As Integers    ${id_recu}    ${ResourceId}        # Vérifie que l'ID correspond à celui demandé
    
    # Validation du nom de la ressource (exemple pour l'ID 2)
    ${name}=    Get From Dictionary    ${data}    name                # Récupère le nom
    Should Be Equal As Strings    ${name}    fuchsia rose             # Vérifie le nom (attendu pour l'ID 2)
