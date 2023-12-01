import check
import pygame

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
    
    
    while running:
      print(pointer)
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          running = False
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_BACKSPACE:
              if pointer>0:
                pointer-=1
              if pointer==36:
                pointer-=2
                pygame.draw.rect(screen, "black", [coord[pointer][0],coord[pointer][1], 45, 45])
              pygame.draw.rect(screen, "black", [coord[pointer][0],coord[pointer][1], 45, 45])
              print('BACK')
          if pointer<36:
            if event.key == pygame.K_a:
              if pointer==36:
                pass
              else:
                text_surface = font.render('A', False, 'white')
                screen.blit(text_surface, coord[pointer])
                pointer+=1
            if event.key == pygame.K_b:
              if pointer==36:
                pass
              else:
                text_surface = font.render('B', False, 'white')
                screen.blit(text_surface, coord[pointer])
                pointer+=1
            if event.key == pygame.K_c:
              if pointer==36:
                pass
              else:
                text_surface = font.render('C', False, 'white')
                screen.blit(text_surface, coord[pointer])
                pointer+=1
            if event.key == pygame.K_d:
              if pointer==36:
                pass
              else:
                text_surface = font.render('D', False, 'white')
                screen.blit(text_surface, coord[pointer])
                pointer+=1
            if event.key == pygame.K_e:
              if pointer==36:
                pass
              else:
                text_surface = font.render('E', False, 'white')
                screen.blit(text_surface, coord[pointer])
                pointer+=1
            if event.key == pygame.K_f:
              if pointer==36:
                pass
              else:
                text_surface = font.render('F', False, 'white')
                screen.blit(text_surface, coord[pointer])
                pointer+=1
            if event.key == pygame.K_g:
              if pointer==36:
                pass
              else:
                text_surface = font.render('G', False, 'white')
                screen.blit(text_surface, coord[pointer])
                pointer+=1
            if event.key == pygame.K_h:
              if pointer==36:
                pass
              else:
                text_surface = font.render('H', False, 'white')
                screen.blit(text_surface, coord[pointer])
                pointer+=1
            if event.key == pygame.K_i:
              if pointer==36:
                pass
              else:
                text_surface = font.render('I', False, 'white')
                screen.blit(text_surface, coord[pointer])
                pointer+=1
            if event.key == pygame.K_j:
              if pointer==36:
                pass
              else:
                text_surface = font.render('J', False, 'white')
                screen.blit(text_surface, coord[pointer])
                pointer+=1
            if event.key == pygame.K_k:
              if pointer==36:
                pass
              else:
                text_surface = font.render('K', False, 'white')
                screen.blit(text_surface, coord[pointer])
                pointer+=1
            if event.key == pygame.K_l:
              if pointer==36:
                pass
              else:
                text_surface = font.render('L', False, 'white')
                screen.blit(text_surface, coord[pointer])
                pointer+=1
            if event.key == pygame.K_m:
              if pointer==36:
                pass
              else:
                text_surface = font.render('M', False, 'white')
                screen.blit(text_surface, coord[pointer])
                pointer+=1
            if event.key == pygame.K_n:
              if pointer==36:
                pass
              else:
                text_surface = font.render('N', False, 'white')
                screen.blit(text_surface, coord[pointer])
                pointer+=1
            if event.key == pygame.K_o:
              if pointer==36:
                pass
              else:
                text_surface = font.render('O', False, 'white')
                screen.blit(text_surface, coord[pointer])
                pointer+=1
            if event.key == pygame.K_p:
              if pointer==36:
                pass
              else:
                text_surface = font.render('P', False, 'white')
                screen.blit(text_surface, coord[pointer])
                pointer+=1
            if event.key == pygame.K_q:
              if pointer==36:
                pass
              else:
                text_surface = font.render('Q', False, 'white')
                screen.blit(text_surface, coord[pointer])
                pointer+=1
            if event.key == pygame.K_r:
              if pointer==36:
                pass
              else:
                text_surface = font.render('R', False, 'white')
                screen.blit(text_surface, coord[pointer])
                pointer+=1
            if event.key == pygame.K_s:
              if pointer==36:
                pass
              else:
                text_surface = font.render('S', False, 'white')
                screen.blit(text_surface, coord[pointer])
                pointer+=1
            if event.key == pygame.K_t:
              if pointer==36:
                pass
              else:
                text_surface = font.render('T', False, 'white')
                screen.blit(text_surface, coord[pointer])
                pointer+=1
            if event.key == pygame.K_u:
              if pointer==36:
                pass
              else:
                text_surface = font.render('U', False, 'white')
                screen.blit(text_surface, coord[pointer])
                pointer+=1
            if event.key == pygame.K_v:
              if pointer==36:
                pass
              else:
                text_surface = font.render('V', False, 'white')
                screen.blit(text_surface, coord[pointer])
                pointer+=1
            if event.key == pygame.K_w:
              if pointer==36:
                pass
              else:
                text_surface = font.render('W', False, 'white')
                screen.blit(text_surface, coord[pointer])
                pointer+=1
            if event.key == pygame.K_x:
              if pointer==36:
                pass
              else:
                text_surface = font.render('X', False, 'white')
                screen.blit(text_surface, coord[pointer])
                pointer+=1
            if event.key == pygame.K_y:
              if pointer==36:
                pass
              else:
                text_surface = font.render('Y', False, 'white')
                screen.blit(text_surface, coord[pointer])
                pointer+=1 
            if event.key == pygame.K_z:
              if pointer==36:
                pass
              else:
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
