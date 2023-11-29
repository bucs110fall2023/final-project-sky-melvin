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
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_a:
            print('a')
          if event.key == pygame.K_b:
            print('b') 
          if event.key == pygame.K_c:
            print('c') 
          if event.key == pygame.K_d:
            print('d') 
          if event.key == pygame.K_e:
            print('e') 
          if event.key == pygame.K_f:
            print('f')
          if event.key == pygame.K_g:
            print('g') 
          if event.key == pygame.K_h:
            print('h') 
          if event.key == pygame.K_i:
            print('i') 
          if event.key == pygame.K_j:
            print('j') 
          if event.key == pygame.K_k:
            print('k') 
          if event.key == pygame.K_l:
            print('l') 
          if event.key == pygame.K_m:
            print('m') 
          if event.key == pygame.K_n:
            print('n') 
          if event.key == pygame.K_o:
            print('o') 
          if event.key == pygame.K_p:
            print('p') 
          if event.key == pygame.K_q:
            print('q') 
          if event.key == pygame.K_r:
            print('r') 
          if event.key == pygame.K_s:
            print('s') 
          if event.key == pygame.K_t:
            print('t') 
          if event.key == pygame.K_u:
            print('u') 
          if event.key == pygame.K_v:
            print('v') 
          if event.key == pygame.K_w:
            print('w') 
          if event.key == pygame.K_x:
            print('x')
          if event.key == pygame.K_y:
            print('y') 
          if event.key == pygame.K_z:
            print('z')
             
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
