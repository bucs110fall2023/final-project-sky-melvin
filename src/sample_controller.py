import check
import pygame

class Controller:
  
  def __init__(self):
    screen = pygame.display.set_mode((720, 720))
    font = pygame.font.Font(None, 35)
    #setup pygame data
    
  def mainloop(self):
    pygame.quit()
    
    wordle = check.Check.wordle()
    print(wordle)
    
    trial = check.Guess.guesses()
    print(trial)
    #select state loop
    
  
  ### below are some sample loop states ###

  def menuloop(self):
    pass
      #event loop

      #update data

      #redraw
      
  def gameloop(self):
    pass
      #event loop

      #update data

      #redraw
    
  def gameoverloop(self):
    pass
      #event loop

      #update data

      #redraw
