*** Settings ***
Library    RequestsLibrary    # Import de la bibliothèque pour les requêtes HTTP
Library    Collections        # Import de la bibliothèque pour la manipulation de collections

*** Variables ***
${Base_URL}           https://mock-api-h0g7.onrender.com/    # URL de base de l'API
${API_KEY}            Cle-API-ReqRes-test-academy            # Clé API pour l'authentification
${FirstName_Attendu}  Anass                                  # Prénom attendu pour le test
${LastName_Attendu}   Rami                                   # Nom de famille attendu pour le test
${Email_Attendu}      anass.rami@api.testacademy.fr          # Email attendu pour le test

*** Test Cases ***
Test Requete POST
    # Création des en-têtes avec le jeton d'authentification
    &{headers}=        Create Dictionary    Authorization=Bearer ${API_KEY}    # Prépare l'authentification Bearer

    # Création du corps de la requête en JSON
    &{Corps_Requete}=  Create Dictionary    first_name=${FirstName_Attendu}    last_name=${LastName_Attendu}    email=${Email_Attendu}    # Construit le payload JSON avec prénom, nom et email

    # Envoi de la requête POST pour créer un utilisateur
    ${Reponse}=        POST    ${Base_URL}api/users    json=${Corps_Requete}    headers=${headers}    expected_status=201    # Envoie le POST et attend un statut 201 Created

    # Log de la réponse JSON pour vérification
    Log                ${Reponse.json()}    # Affiche le corps de la réponse

    # Vérification de la présence des clés 'id' et 'createdAt' dans la réponse
    Dictionary Should Contain Key    ${Reponse.json()}    id           # Valide que la réponse contient un ID généré
    Dictionary Should Contain Key    ${Reponse.json()}    createdAt    # Valide que la réponse contient la date de création

    # Vérification de la correspondance des données envoyées et reçues
    ${first_name}=     Get From Dictionary    ${Reponse.json()}    first_name    # Extrait le prénom de la réponse
    Should Be Equal As Strings    ${FirstName_Attendu}    ${first_name}          # Compare le prénom reçu avec celui envoyé

    ${last_name}=      Get From Dictionary    ${Reponse.json()}    last_name     # Extrait le nom de la réponse
    Should Be Equal As Strings    ${LastName_Attendu}    ${last_name}            # Compare le nom reçu avec celui envoyé

    ${email}=          Get From Dictionary    ${Reponse.json()}    email         # Extrait l'email de la réponse
    Should Be Equal As Strings    ${Email_Attendu}    ${email}                   # Compare l'email reçu avec celui envoyé