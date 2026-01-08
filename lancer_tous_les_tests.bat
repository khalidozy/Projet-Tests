@echo off
rem script pour exécuter tous les tests en une seule fois

echo Lancement de tous les tests...
rem affiche un message d'introduction

call lancer_tests_unitaires.bat
rem appelle le script des tests unitaires 
if errorlevel 1 exit /b 1
rem si une erreur est détecté (code retour > 0), on aréte tout

call lancer_tests_api.bat
rem appelle le script des tests API
if errorlevel 1 exit /b 1

call lancer_tests_ihm.bat
rem appelle le script des tests UI
if errorlevel 1 exit /b 1

echo Tous les tests se sont exécutés correctement.
rem Message final si tout s'est bien passé
