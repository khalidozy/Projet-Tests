@echo off
rem Empéche d'afficher chaque commande exécutée dans le terminal

echo Lancement des tests unitaires...
rem affiche ce message à l'écran pour indiquer ce qu'on va faire

"C:\Users\Unicornis\AppData\Local\Programs\Python\Python314\python.exe" -m unittest discover -v tests_unitaires

echo Tests unitaires terminés.
exit /b 0
