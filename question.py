import random

class Question:
    def __init__(self, text, choices, correct_choice):
        self.text = text
        self.choices = choices
        self.correct_choice = correct_choice.lower()

    def is_correct(self, answer):
        return answer.lower() == self.correct_choice
