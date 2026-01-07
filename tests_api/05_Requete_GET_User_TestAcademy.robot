*** Settings ***
Library    RequestsLibrary    # Import de la bibliothèque pour les requêtes HTTP
Library    Collections        # Import de la bibliothèque pour la manipulation de collections

*** Variables ***
${Base_URL}    https://mock-api-h0g7.onrender.com/    # URL de base de l'API
${API_KEY}     Cle-API-ReqRes-test-academy            # Clé API pour l'authentification
${UserId}      6                                      # ID de l'utilisateur à récupérer

*** Test Cases ***
Test Requete GET Single User
    # Création des en-têtes avec l'authentification
    &{headers}=    Create Dictionary    Authorization=Bearer ${API_KEY}    # Prépare l'authentification Bearer

    # Envoi de la requête GET pour récupérer un utilisateur spécifique
    ${Reponse}=    GET    ${Base_URL}api/users/${UserId}    headers=${headers}    expected_status=200    # Envoie la requête GET et attend un statut 200 OK

    # Log de la réponse pour vérification
    Log    ${Reponse.json()}    # Affiche le corps de la réponse JSON

    # Vérification que la réponse contient les données de l'utilisateur
    Dictionary Should Contain Key    ${Reponse.json()}    data    # Vérifie la présence de la clé 'data'
    
    # Validation de l'ID de l'utilisateur retourné
    ${data}=    Get From Dictionary    ${Reponse.json()}    data    # Récupère l'objet 'data'
    ${id_recu}=    Get From Dictionary    ${data}    id             # Récupère l'ID
    Should Be Equal As Integers    ${id_recu}    ${UserId}          # Vérifie que l'ID correspond à celui demandé
