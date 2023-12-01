import check
import pygame
pygame.init()
class Controller:
  
  def __init__(self):
    screen = pygame.display.set_mode((520, 520))
    font = pygame.font.Font(None, 80)
    clock = pygame.time.Clock()
    running = True

    screen.fill("grey")
    x = 50
    y = 50
    coord=[]
    for h in range(6):
      y = y + 50
      for w in range(6):
        coord.append([x,y])
        pygame.draw.rect(screen, "black", [x, y, 45, 45])
        x = x + 50
      x = 50
    print(coord)
    pointer=0
    front_limit=6
    end_limit=0
    count=0 # amount of tires
    
    
    while running:
      print(pointer)
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          running = False
        if count==6:
          pygame.quit()
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_RETURN:
            if pointer%6==0 and pointer>=front_limit: #Only press enter with 6 letter word and can't immediatley press enter to skip to other lines
              end_limit=front_limit #store previous end limit as front limit before increasing it
              front_limit+=6 
              count+=1
                
          if event.key == pygame.K_BACKSPACE:
              if pointer>end_limit:
                pointer-=1
              if pointer==front_limit:
                pointer-=2
                pygame.draw.rect(screen, "black", [coord[pointer][0],coord[pointer][1], 45, 45])
              pygame.draw.rect(screen, "black", [coord[pointer][0],coord[pointer][1], 45, 45])
          if pointer==front_limit:
            pass
          else:
            if event.key == pygame.K_a:
              text_surface = font.render('A', False, 'white')
              screen.blit(text_surface, coord[pointer])
              pointer+=1
            if event.key == pygame.K_b:
              text_surface = font.render('B', False, 'white')
              screen.blit(text_surface, coord[pointer])
              pointer+=1
            if event.key == pygame.K_c:
              text_surface = font.render('C', False, 'white')
              screen.blit(text_surface, coord[pointer])
              pointer+=1
            if event.key == pygame.K_d:
              text_surface = font.render('D', False, 'white')
              screen.blit(text_surface, coord[pointer])
              pointer+=1
            if event.key == pygame.K_e:
              text_surface = font.render('E', False, 'white')
              screen.blit(text_surface, coord[pointer])
              pointer+=1
            if event.key == pygame.K_f:
              text_surface = font.render('F', False, 'white')
              screen.blit(text_surface, coord[pointer])
              pointer+=1
            if event.key == pygame.K_g:
              text_surface = font.render('G', False, 'white')
              screen.blit(text_surface, coord[pointer])
              pointer+=1
            if event.key == pygame.K_h:
              text_surface = font.render('H', False, 'white')
              screen.blit(text_surface, coord[pointer])
              pointer+=1
            if event.key == pygame.K_i:
              text_surface = font.render('I', False, 'white')
              screen.blit(text_surface, coord[pointer])
              pointer+=1
            if event.key == pygame.K_j:
              text_surface = font.render('J', False, 'white')
              screen.blit(text_surface, coord[pointer])
              pointer+=1
            if event.key == pygame.K_k:
              text_surface = font.render('K', False, 'white')
              screen.blit(text_surface, coord[pointer])
              pointer+=1
            if event.key == pygame.K_l:
              text_surface = font.render('L', False, 'white')
              screen.blit(text_surface, coord[pointer])
              pointer+=1
            if event.key == pygame.K_m:
              text_surface = font.render('M', False, 'white')
              screen.blit(text_surface, coord[pointer])
              pointer+=1
            if event.key == pygame.K_n:
              text_surface = font.render('N', False, 'white')
              screen.blit(text_surface, coord[pointer])
              pointer+=1
            if event.key == pygame.K_o:
              text_surface = font.render('O', False, 'white')
              screen.blit(text_surface, coord[pointer])
              pointer+=1
            if event.key == pygame.K_p:
              text_surface = font.render('P', False, 'white')
              screen.blit(text_surface, coord[pointer])
              pointer+=1
            if event.key == pygame.K_q:
              text_surface = font.render('Q', False, 'white')
              screen.blit(text_surface, coord[pointer])
              pointer+=1
            if event.key == pygame.K_r:
              text_surface = font.render('R', False, 'white')
              screen.blit(text_surface, coord[pointer])
              pointer+=1
            if event.key == pygame.K_s:
              text_surface = font.render('S', False, 'white')
              screen.blit(text_surface, coord[pointer])
              pointer+=1
            if event.key == pygame.K_t:
              text_surface = font.render('T', False, 'white')
              screen.blit(text_surface, coord[pointer])
              pointer+=1
            if event.key == pygame.K_u:
              text_surface = font.render('U', False, 'white')
              screen.blit(text_surface, coord[pointer])
              pointer+=1
            if event.key == pygame.K_v:
              text_surface = font.render('V', False, 'white')
              screen.blit(text_surface, coord[pointer])
              pointer+=1
            if event.key == pygame.K_w:
              text_surface = font.render('W', False, 'white')
              screen.blit(text_surface, coord[pointer])
              pointer+=1
            if event.key == pygame.K_x:
              text_surface = font.render('X', False, 'white')
              screen.blit(text_surface, coord[pointer])
              pointer+=1
            if event.key == pygame.K_y:
              text_surface = font.render('Y', False, 'white')
              screen.blit(text_surface, coord[pointer])
              pointer+=1 
            if event.key == pygame.K_z:
              text_surface = font.render('Z', False, 'white')
              screen.blit(text_surface, coord[pointer])
              pointer+=1
            
      

      pygame.display.update()
     
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
