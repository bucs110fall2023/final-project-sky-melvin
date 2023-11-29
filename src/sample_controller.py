import check
import pygame

class Controller:
  
  def __init__(self):
    screen = pygame.display.set_mode((520, 520))
    font = pygame.font.Font(None, 35)
    clock = pygame.time.Clock()
    running = True
    while running:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          running = False
          
      screen.fill("grey")
      
      x = 50
      y = 50

      for h in range(6):
        y = y + 50
        for w in range(6):
          pygame.draw.rect(screen, "black", [x, y, 45, 45])
          x = x + 50
        x = 50
          
         
      
      pygame.display.flip()

      clock.tick(60)  

    pygame.quit()
    
  def mainloop(self):
    #wordle = check.Check.wordle()
    #print(wordle)
    
    #trial = check.Guess.guesses()
    #print(trial)
    
    #check.Check.check_pos(wordle, trial)
    #select state loop
    pass
    
  
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
