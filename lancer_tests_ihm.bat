@echo off
rem cache l'affichage des commandes dans le terminal

echo Lancement des tests IHM...
rem affiche ce message avant de lancer les tests UI

robot tests_ihm
rem Exécute les tests présents dans le dossier ui_tests
