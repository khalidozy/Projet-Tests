*** Settings ***
Library    RequestsLibrary    # Import de la bibliothèque pour les requêtes HTTP
Library    JSONLibrary        # Import de la bibliothèque pour la manipulation JSON
Library    Collections        # Import de la bibliothèque pour la manipulation de collections

*** Variables ***
${Base_URL}    https://mock-api-h0g7.onrender.com/    # URL de base de l'API TestAcademy
${API_KEY}     Cle-API-ReqRes-test-academy            # Clé API pour l'authentification

*** Test Cases ***
Test Requete GET Users
    # Création du dictionnaire de paramètres pour la requête GET
    &{Params}=    Create Dictionary    page=1    per_page=6    # Définit les paramètres de pagination (page 1, 6 par page)

    # Création du dictionnaire des en-têtes avec l'authentification
    &{headers}=    Create Dictionary    Authorization=Bearer ${API_KEY}    # Ajoute le token Bearer dans les headers

    # Envoi de la requête GET et récupération de la réponse
    ${Reponse}=    GET    ${Base_URL}api/users    params=${Params}    headers=${headers}    expected_status=200    # Exécute la requête GET vers /api/users avec params et headers, attend un statut 200

    # Transformation de la réponse en format JSON
    ${ReponseJson}=    Set Variable    ${Reponse.json()}    # Convertir la réponse HTTP brute en objet JSON pour manipulation

    # Affichage du contenu JSON dans les logs
    Log    ${ReponseJson}    # Logue le contenu de la réponse JSON pour débogage

    # Extraction de la liste des utilisateurs depuis la clé 'data'
    ${ListeUtilisateurs}=    Get Value From Json    ${ReponseJson}    data[:]    # Récupère tous les éléments de la liste 'data' du JSON

    # Récupération du premier utilisateur de la liste
    ${PremiereUtilisateur}=    Get From List    ${ListeUtilisateurs}    0    # Extrait le premier élément (index 0) de la liste des utilisateurs

    # Vérification que le prénom du premier utilisateur est 'George'
    Should Be Equal    ${PremiereUtilisateur['first_name']}    George    # Valide que le champ 'first_name' du premier utilisateur est égal à 'George'