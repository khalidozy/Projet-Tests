@echo off
rem Script pour executer tous les tests en une seule fois !

echo Lancement de tous les tests...
rem Affiche un message d'introduction

call lancer_tests_unitaires.bat
rem Appelle le script des tests unitaires
if errorlevel 1 exit /b 1
rem Si un erreur est detecter (code retour > 0), on arrete tout 

call lancer_tests_api.bat
rem Appelle le script des tests api
if errorlevel 1 exit /b 1

call lancer_tests_ihm.bat
rem Appelle le script des tests UI
if errorlevel 1 exit /b 1

echo Tous les tests se sont exécutés correctement.
rem Message final si tout s'est bien passé 