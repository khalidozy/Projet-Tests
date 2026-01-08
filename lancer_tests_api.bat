@echo off
rem cache l'affichage des commandes dans le terminal

echo Lancement des tests d'API Robot framework...
rem affiche ce message avant d'excuter les tests API

cd tests_api
robot *.robot
rem lancer tous les tests robot framework dans le dossier tests_api



