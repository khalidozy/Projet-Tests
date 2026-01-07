*** Settings ***
Library    RequestsLibrary    # Import de la bibliothèque pour les requêtes HTTP

*** Variables ***
${Base_URL}         https://mock-api-h0g7.onrender.com/    # Définition de l'URL de base de l'API
${API_KEY}          Cle-API-ReqRes-test-academy            # Clé API pour l'authentification
${Id_Utilisateur}   3                                      # ID de l'utilisateur à supprimer

*** Test Cases ***
Test Requete DELETE
    # Création des en-têtes avec l'authentification
    &{headers}=    Create Dictionary    Authorization=Bearer ${API_KEY}    # Prépare l'authentification Bearer

    # Envoi de la requête DELETE pour supprimer l'utilisateur spécifié
    ${Reponse}=    DELETE    ${Base_URL}api/users/${Id_Utilisateur}    headers=${headers}    expected_status=204    # Envoie la requête DELETE et attend un statut 204 No Content