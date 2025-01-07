# Projet QCM

Ce projet est un quiz à choix multiples (QCM) contenant 10 questions. Il utilise des classes et des modules pour organiser le code et proposer une expérience interactive à l'utilisateur.


## Instructions pour exécuter le programme

1. Assurez-vous que Python est installé sur votre machine.
2. Placez tous les fichiers du projet dans un même répertoire.
3. Lancez le programme avec la commande suivante :
   python3 main.py
  

## Fonctionnalités principales

1. Quiz interactif :
   - Le programme pose 10 questions aléatoires à l'utilisateur.
   - Chaque question propose 3 réponses possibles (a, b, c).
   - L'utilisateur répond en entrant a, b ou c (insensible à la casse).
   - À la fin, le score total et les réponses correctes sont affichés.

2. Organisation modulaire :
   - Le projet utilise des classes pour structurer les questions et leurs réponses.
   - Les questions et les choix sont mélangées à chaque exécution pour varier les sessions.


## Tests unitaires

Des tests unitaires sont inclus pour vérifier le bon fonctionnement des classes principales, notamment la méthode de validation des réponses (is_correct).

Pour exécuter les tests, utilisez la commande suivante :
python3 -m unittest test_qcm.py



## Organisation des fichiers

- main.py : Point d'entrée du programme, gère l'interaction avec l'utilisateur.
- question.py : Classe Question pour structurer les questions et leurs réponses.
- test_qcm.py : Tests unitaires pour valider les fonctionnalités de la classe Question.


