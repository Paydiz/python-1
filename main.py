import random

# Classe Question
class Question:
    def __init__(self, texte, choix, choix_correct):
        self.texte = texte
        self.choix = choix
        self.choix_correct = choix_correct

# Liste des questions
questions_data = [
    ("Quel est le prénom de notre prof de Python ?", ["Thomas", "Ronel", "Wilfried"], "Wilfried"),
    ("Dans quelle école sommes-nous ?", ["HEC", "ESIEE-PARIS", "ESIEE-IT"], "ESIEE-IT"),
    ("Quel âge ai-je ?", ["21", "23", "25"], "23"),
    ("Quelle est ma couleur préférée ?", ["rouge", "bleu", "jaune"], "bleu"),
    ("Quelle est la capitale de l'Espagne ?", ["Madrid", "Barcelone", "Tapas"], "Madrid"),
    ("Quel est le plus grand océan ?", ["Atlantique", "Pacifique", "Indien"], "Pacifique"),
    ("Quelle est ma taille ?", ["160", "157", "158"], "158"),
    ("Quel est le symbole chimique de l'eau ?", ["O2", "H2O", "CO2"], "H2O"),
    ("Combien de joueurs dans une équipe de basket ?", ["9", "10", "5"], "5"),
    ("Combien y a-t-il de délégués dans la classe ?", ["0", "2", "1"], "0")
]

# Création des objets Question
questions = [Question(texte, choix, correct) for texte, choix, correct in questions_data]
random.shuffle(questions)

# Déroulement du quiz
score = 0

print("Bienvenue au QCM ! Répondez avec a, b ou c.\n")

for i, question in enumerate(questions, 1):
    # Mélanger les choix tout en conservant la correspondance avec la réponse correcte
    choix_melanges = question.choix[:]
    random.shuffle(choix_melanges)
    
    # Identifier la bonne réponse dans la liste mélangée
    try:
        index_correct = choix_melanges.index(question.choix_correct)
    except ValueError:
        print(f"Erreur : '{question.choix_correct}' n'est pas dans les choix pour la question : {question.texte}")
        continue
    
    lettre_correcte = chr(97 + index_correct)  # Convertir l'indice en lettre (a, b, c)

    # Afficher la question et les choix mélangés
    print(f"Question {i}: {question.texte}")
    for index, choix in enumerate(choix_melanges):
        print(f"{chr(97 + index)}. {choix}")
    
    # Obtenir la réponse utilisateur
    reponse = input("Votre réponse : ").strip().lower()
    
    # Vérifier la réponse
    if reponse == lettre_correcte:
        print("Correct !\n")
        score += 1
    else:
        print(f"Faux. La bonne réponse était : {lettre_correcte}. {question.choix_correct}\n")

print(f"Votre score final est de {score}/{len(questions)}.")
