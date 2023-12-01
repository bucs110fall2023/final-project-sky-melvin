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
    
    def check_pos(wordle, trial):
        for x, y in zip(wordle, trial):
            if x == y:
                Check.color("correct", x)      #This is when the letter is in the correct position 
            elif y in wordle:
                Check.color("kinda", y)      #This is when the letter is in the wrong position but is still in the word to guess
            else:
                Check.color("wrong", y)    #This is when the letter is incorrect/not in the word that you are trying to guess
    
    def color(self, letter):
        if self == "correct":
            return letter, "green"           #This part may be wrong, we'll have to test it but the functions should each return the letter and the box color
        elif self == "kinda":
            return letter, "yellow"
        elif self == "wrong":
            return letter, "black"
            
    
class Guess:
    def guesses():
        guess = input("Please enter what you think the word is:")
        while len(guess) != 6:
            guess = input("Invalid input, please enter what you think the word is:")
        else:
            return list(guess)
        
    