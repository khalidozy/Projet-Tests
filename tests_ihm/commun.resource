*** Settings ***
Library    Selenium2Library

*** Variables ***
${URL}    http://livraison3.testacademy.fr
${NAVIGATEUR}    chrome
${LIEN SE CONNECTER}     xpath=//a[contains(text(),'Se connecter')]
${LIEN SE DECONNECTER}    xpath=//section[@id='body-area']/div[2]/div/ul/li[8]/a
${CHAMP NOM UTILISATEUR}    xpath=//input[@name='username']
${CHAMP MOT DE PASSE}    xpath=//input[@name='password'] 
${UTILISATEUR VALIDE}    robot
${MOT DE PASSE VALIDE}    robot
${BOUTON SE CONNECTER}    xpath=(//button[@type='submit'])[5]
${ZONE ERREUR}    xpath=//div[@id='modal-login']/div/div[2]/div/div[2]/div/p
${TITRE PAGE TABLEAU DE BORD}    Tableau de bord - Livraison 3
*** Keywords ***
Ouvrir Le Navigateur Et Accéder A L'Application
    Open Browser    ${URL}    browser=${NAVIGATEUR}
    Maximize Browser Window
    
Accéder A La Page De Connexion
   Click Element    ${LIEN SE CONNECTER}

Entrer Le Nom Utilisateur
    [Arguments]    ${utilisateur Valide}
    Wait Until Element Is Visible    ${CHAMP NOM UTILISATEUR}  
    Click Element    ${CHAMP NOM UTILISATEUR}
    Input Text    ${CHAMP NOM UTILISATEUR}    ${utilisateur Valide}

Entrer Le Mot De Passe
    [Arguments]    ${mot de passe}
   Input Text    ${CHAMP MOT DE PASSE}    ${mot de passe}

Soumettre Le Formulaire De Connexion
   Click Element    ${BOUTON SE CONNECTER}