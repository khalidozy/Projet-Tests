@echo off
rem Empeche d'afficher chaque commande executee dans le terminal

echo Lancement des tests unitaires...
rem Affiche ce message a l'ecran pour indiquer ce qu'on va faire

python -m unittest discover -v tests_unitaires
rem lance tous les tests dans le dossier tests unitaires avec details (-v = verbose)
