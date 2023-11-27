import pygame
import check
#import your controller

def main():
    pygame.init()
    screen = pygame.display.set_mode((720, 720))
    font = pygame.font.Font(None, 35)
    pygame.quit()
    wordle = check.Check.wordle()
    print(wordle)
    
    trial = check.Guess.guesses()
    print(trial)
    #Create an instance on your controller object
    #Call your mainloop
    
    ###### NOTHING ELSE SHOULD GO IN main(), JUST THE ABOVE 3 LINES OF CODE ######

# https://codefather.tech/blog/if-name-main-python/
if __name__ == '__main__':
    main()
