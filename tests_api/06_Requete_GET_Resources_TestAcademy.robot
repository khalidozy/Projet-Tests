*** Settings ***
Library    RequestsLibrary    # Import de la bibliothèque pour les requêtes HTTP
Library    Collections        # Import de la bibliothèque pour la manipulation de collections

*** Variables ***
${Base_URL}    https://mock-api-h0g7.onrender.com/    # URL de base de l'API
${API_KEY}     Cle-API-ReqRes-test-academy            # Clé API pour l'authentification

*** Test Cases ***
Test Requete GET List Resources
    # Création des en-têtes avec l'authentification
    &{headers}=    Create Dictionary    Authorization=Bearer ${API_KEY}    # Prépare l'authentification Bearer

    # Envoi de la requête GET pour récupérer la liste des ressources
    ${Reponse}=    GET    ${Base_URL}api/unknown    headers=${headers}    expected_status=200    # Envoie la requête GET et attend un statut 200 OK

    # Log de la réponse pour vérification
    Log    ${Reponse.json()}    # Affiche le corps de la réponse JSON

    # Vérification que la réponse contient la pagination et les données
    Dictionary Should Contain Key    ${Reponse.json()}    page        # Vérifie la présence de la clé 'page'
    Dictionary Should Contain Key    ${Reponse.json()}    data        # Vérifie la présence de la clé 'data'
    
    # Vérification que la liste des ressources n'est pas vide
    ${data}=    Get From Dictionary    ${Reponse.json()}    data    # Récupère la liste 'data'
    Should Not Be Empty    ${data}    # Vérifie que la liste contient des éléments
