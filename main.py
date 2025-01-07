import random

# Classe Question
class Question:
    def __init__(self, text, choices, correct_choice):
        self.text = text
        self.choices = choices
        self.correct_choice = correct_choice

# Liste des questions
questions_data = [
    ("Qui est le prénom de notre prof de python ?", ["Thomas", "Ronel", "Wilfried"], "Wilfried"),
    ("Dans quelle école sommes nous ?", ["HEC", "ESIEE-PARIS", "ESIEE-IT"], "ESIEE-IT"),
    ("Quel âge j'ai ?", ["21", "23", "25"], "23"),
    ("Quelle est ma couleur préférée ?", ["rouge", "bleu", "jaune"], "bleu"),
    ("Quelle est la capitale de l'Espagne ?", ["Madrid", "Barcelone", "Tapas"], "Madrid"),
    ("Quel est le plus grand océan ?", ["Atlantique", "Pacifique", "Indien"], "Pacifique"),
    ("Je mesure combien ?", ["160", "157", "158"], "158"),
    ("Quel est le symbole chimique de l'eau ?", ["O2", "H2O", "CO2"], "H2O"),
    ("Combien de joueurs dans une équipe de basket ?", ["9", "10", "5"], "5"),
    ("Combien y a-t-il de délégué dans la classe ?", ["0", "2", "1"], "0")
]

# Création des objets Question
questions = [Question(text, choices, correct) for text, choices, correct in questions_data]
random.shuffle(questions)

# Déroulement du quiz
score = 0

print("Bienvenue au QCM ! Répondez avec a, b ou c.\n")

for i, question in enumerate(questions, 1):
    # Mélanger les choix tout en conservant la correspondance avec la réponse correcte
    shuffled_choices = question.choices[:]
    random.shuffle(shuffled_choices)
    
    # Identifier la bonne réponse dans la liste mélangée
    try:
        correct_index = shuffled_choices.index(question.correct_choice)
    except ValueError:
        print(f"Erreur : '{question.correct_choice}' n'est pas dans les choix pour la question : {question.text}")
        continue
    
    correct_letter = chr(97 + correct_index)  # Convertir l'indice en lettre (a, b, c)

    # Afficher la question et les choix mélangés
    print(f"Question {i}: {question.text}")
    for index, choice in enumerate(shuffled_choices):
        print(f"{chr(97 + index)}. {choice}")
    
    # Obtenir la réponse utilisateur
    answer = input("Votre réponse : ").strip().lower()
    
    # Vérifier la réponse
    if answer == correct_letter:
        print("Correct !\n")
        score += 1
    else:
        print(f"Faux. La bonne réponse était : {correct_letter}. {question.correct_choice}\n")

print(f"Votre score final est de {score}/{len(questions)}.")
