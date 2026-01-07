*** Settings ***
Library    RequestsLibrary    # Import de la bibliothèque pour les requêtes HTTP
Library    Collections        # Import de la bibliothèque pour la manipulation de collections

*** Variables ***
${Base_URL}           https://mock-api-h0g7.onrender.com/    # URL de base de l'API
${API_KEY}            Cle-API-ReqRes-test-academy            # Clé API pour l'authentification
${Id_Utilisateur}     7                                     # ID de l'utilisateur à mettre à jour
${FirstName_Attendu}  George                                  # Nouveau prénom attendu
${LastName_Attendu}   Zion-Weaver                            # Nouveau nom attendu
${Email_Attendu}      janet.zion@api.testacademy.fr          # Nouvel email attendu

*** Test Cases ***
Test Requete PUT
    # Création des en-têtes avec le jeton d'authentification
    &{headers}=        Create Dictionary    Authorization=Bearer ${API_KEY}    # Prépare l'authentification Bearer

    # Création du corps de la requête avec les nouvelles informations
    &{Corps_Requete}=  Create Dictionary    first_name=${FirstName_Attendu}    last_name=${LastName_Attendu}    email=${Email_Attendu}    # Prépare les données à mettre à jour

    # Envoi de la requête PUT pour mettre à jour l'utilisateur
    ${Reponse}=        PUT    ${Base_URL}api/users/${Id_Utilisateur}    json=${Corps_Requete}    headers=${headers}    expected_status=200    # Envoie la requête PUT et attend un statut 200 OK

    # Log de la réponse pour vérification
    Log                ${Reponse.json()}    # Affiche la réponse JSON

    # Vérification que la réponse contient la clé 'updatedAt'
    Dictionary Should Contain Key    ${Reponse.json()}    updatedAt    # Vérifie que la mise à jour a généré un timestamp updatedAt

    # Vérification que les données ont bien été mises à jour
    ${first_name}=     Get From Dictionary    ${Reponse.json()}    first_name    # Extrait le prénom de la réponse
    Should Be Equal As Strings    ${FirstName_Attendu}    ${first_name}          # Vérifie que le prénom correspond à celui envoyé

    ${last_name}=      Get From Dictionary    ${Reponse.json()}    last_name     # Extrait le nom de la réponse
    Should Be Equal As Strings    ${LastName_Attendu}    ${last_name}            # Vérifie que le nom correspond à celui envoyé

    ${email}=          Get From Dictionary    ${Reponse.json()}    email         # Extrait l'email de la réponse
    Should Be Equal As Strings    ${Email_Attendu}    ${email}                   # Vérifie que l'email correspond à celui envoyé