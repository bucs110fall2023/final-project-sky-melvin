import dictonary
import random

class Check:
    def __init__(self, l, p):
        self.letter = l
        self.position = p
    
    def wordle():
        return list(random.choice(dictonary.words))
        
    def game():
        attempts = 0
        max_attempts = 6
        guessed_letters = []
    
    def color(self):
        pass
    
class Guess:
    def guesses():
        guess = input("Please enter what you think the word is:")
        while len(guess) != 6:
            guess = input("Invalid input, please enter what you think the word is:")
        else:
            return list(guess)
        
    