@echo off
rem Empeche d'afficher chaque commande executee dans le terminal

echo Lancement des tests d'API Robot Framework
rem Affiche ce message avant d'executer les tests API 

cd tests_api
robot *.robot 

rem Lance tous les tests Robot Framework dans le dossier tests_api

