import random

class Question:
    def __init__(self, texte, choix, choix_correct):
        self.texte = texte
        self.choix = choix
        self.choix_correct = choix_correct.lower()

    def est_correct(self, reponse):
        return reponse.lower() == self.choix_correct
