*** Settings ***
Library    Selenium2Library
Resource    commun.resource

*** Test Cases *** 
Le Tableau De Bord Doit Etre Visible Apres Une Connexion Réussie
    [Setup]    Effectuer Une Connexion Réusie
    Vérifiez Que Le Tableau De Bord Est Visible
    [Teardown]    Effectuer Une Déconnexion Réussie   
Le Lien De Deconnexion Devrait Etre Visible Après Une Déconnexion Réussie
     [Setup]    Effectuer Une Connexion Réusie
    Vérifiez Que Le Tableau De Bord Est Visible
    Effectuer Une Déconnexion Réussie 
    Vérifier Que Le Lien De Connexion Est Visible

*** Keywords ***

Effectuer Une Connexion Réusie
    Ouvrir Le Navigateur Et Accéder A L'Application
    Accéder A La Page De Connexion
    Entrer Le Nom Utilisateur    ${UTILISATEUR VALIDE}    
    Entrer Le Mot De Passe    ${MOT DE PASSE VALIDE}
    Soumettre Le Formulaire De Connexion
    Wait Until Element Is Not Visible    ${CHAMP NOM UTILISATEUR}

Vérifiez Que Le Tableau De Bord Est Visible
    Title Should Be    ${TITRE PAGE TABLEAU DE BORD}

Effectuer Une Déconnexion Réussie
    Click Element    xpath=//section[@id='body-area']/div[2]/div/ul/li[8]/a

Vérifier Que Le Lien De Connexion Est Visible
    Wait Until Element Is Visible    ${LIEN SE CONNECTER}