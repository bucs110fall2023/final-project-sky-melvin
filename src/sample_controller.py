import pygame
import random
import dictionary

pygame.init()
class Controller:
  
  def __init__(self):
    screen = pygame.display.set_mode((520, 520))
    font = pygame.font.Font(None, 80)
    clock = pygame.time.Clock()
    running = True

    screen.fill("grey")
    x = 100
    y = 50
    coord=[]
    for h in range(6):
      y = y + 50
      for w in range(6):
        coord.append([x,y])
        pygame.draw.rect(screen, "black", [x, y, 45, 45])
        x = x + 50
      x = 100
    print(coord)
    pointer=0
    end_limit=6
    front_limit=0
    count=0 # amount of tries
    wordle=Controller.wordle()
    guess=[]
    self.info = []
    x = 100
    y = 50
    
    while running:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          running = False
        if count==6:
          pygame.quit()
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_RETURN:
            if pointer%6==0 and pointer>=end_limit: #Only press enter with 6 letter word and can't immediatley press enter to skip to other lines
              Controller.check_pos(self ,wordle, guess)
              print(wordle)
              print(guess)
              print(self.info)
              guess = [item.upper() for item in guess]
              for w in range(front_limit,end_limit):
                pygame.draw.rect(screen, self.info[w-front_limit], [coord[w][0], coord[w][1], 45, 45])
                text_surface = font.render(guess[w-front_limit], False, 'white')
                screen.blit(text_surface, coord[w])
                
              for j in range(5):
                equal=True
                if self.info[j]=='green':
                  continue
                else:
                  equal=False
                  break
                
              guess.clear()
              self.info.clear()

              front_limit=end_limit #store previous end limit as front limit before increasing end_limit
              end_limit+=6
              count+=1
                
              if equal==True:
                pygame.quit()
              
          if event.key == pygame.K_BACKSPACE:
              if pointer>front_limit:
                guess.pop()
                pointer-=1
              if pointer==end_limit:
                pointer-=2
                pygame.draw.rect(screen, "black", [coord[pointer][0],coord[pointer][1], 45, 45])
              pygame.draw.rect(screen, "black", [coord[pointer][0],coord[pointer][1], 45, 45])
          if pointer==end_limit:
            pass
          else:
            if event.key == pygame.K_a:
              text_surface = font.render('A', False, 'white')
              screen.blit(text_surface, coord[pointer])
              pointer+=1
              guess.append('a')
            if event.key == pygame.K_b:
              text_surface = font.render('B', False, 'white')
              screen.blit(text_surface, coord[pointer])
              pointer+=1
              guess.append('b')
            if event.key == pygame.K_c:
              text_surface = font.render('C', False, 'white')
              screen.blit(text_surface, coord[pointer])
              pointer+=1
              guess.append('c')
            if event.key == pygame.K_d:
              text_surface = font.render('D', False, 'white')
              screen.blit(text_surface, coord[pointer])
              pointer+=1
              guess.append('d')
            if event.key == pygame.K_e:
              text_surface = font.render('E', False, 'white')
              screen.blit(text_surface, coord[pointer])
              pointer+=1
              guess.append('e')
            if event.key == pygame.K_f:
              text_surface = font.render('F', False, 'white')
              screen.blit(text_surface, coord[pointer])
              pointer+=1
              guess.append('f')
            if event.key == pygame.K_g:
              text_surface = font.render('G', False, 'white')
              screen.blit(text_surface, coord[pointer])
              pointer+=1
              guess.append('g')
            if event.key == pygame.K_h:
              text_surface = font.render('H', False, 'white')
              screen.blit(text_surface, coord[pointer])
              pointer+=1
              guess.append('h')
            if event.key == pygame.K_i:
              text_surface = font.render('I', False, 'white')
              screen.blit(text_surface, coord[pointer])
              pointer+=1
              guess.append('i')
            if event.key == pygame.K_j:
              text_surface = font.render('J', False, 'white')
              screen.blit(text_surface, coord[pointer])
              pointer+=1
              guess.append('j')
            if event.key == pygame.K_k:
              text_surface = font.render('K', False, 'white')
              screen.blit(text_surface, coord[pointer])
              pointer+=1
              guess.append('k')
            if event.key == pygame.K_l:
              text_surface = font.render('L', False, 'white')
              screen.blit(text_surface, coord[pointer])
              pointer+=1
              guess.append('l')
            if event.key == pygame.K_m:
              text_surface = font.render('M', False, 'white')
              screen.blit(text_surface, coord[pointer])
              pointer+=1
              guess.append('m')
            if event.key == pygame.K_n:
              text_surface = font.render('N', False, 'white')
              screen.blit(text_surface, coord[pointer])
              pointer+=1
              guess.append('n')
            if event.key == pygame.K_o:
              text_surface = font.render('O', False, 'white')
              screen.blit(text_surface, coord[pointer])
              pointer+=1
              guess.append('o')
            if event.key == pygame.K_p:
              text_surface = font.render('P', False, 'white')
              screen.blit(text_surface, coord[pointer])
              pointer+=1
              guess.append('p')
            if event.key == pygame.K_q:
              text_surface = font.render('Q', False, 'white')
              screen.blit(text_surface, coord[pointer])
              pointer+=1
              guess.append('q')
            if event.key == pygame.K_r:
              text_surface = font.render('R', False, 'white')
              screen.blit(text_surface, coord[pointer])
              pointer+=1
              guess.append('r')
            if event.key == pygame.K_s:
              text_surface = font.render('S', False, 'white')
              screen.blit(text_surface, coord[pointer])
              pointer+=1
              guess.append('s')
            if event.key == pygame.K_t:
              text_surface = font.render('T', False, 'white')
              screen.blit(text_surface, coord[pointer])
              pointer+=1
              guess.append('t')
            if event.key == pygame.K_u:
              text_surface = font.render('U', False, 'white')
              screen.blit(text_surface, coord[pointer])
              pointer+=1
              guess.append('u')
            if event.key == pygame.K_v:
              text_surface = font.render('V', False, 'white')
              screen.blit(text_surface, coord[pointer])
              pointer+=1
              guess.append('v')
            if event.key == pygame.K_w:
              text_surface = font.render('W', False, 'white')
              screen.blit(text_surface, coord[pointer])
              pointer+=1
              guess.append('w')
            if event.key == pygame.K_x:
              text_surface = font.render('X', False, 'white')
              screen.blit(text_surface, coord[pointer])
              pointer+=1
              guess.append('x')
            if event.key == pygame.K_y:
              text_surface = font.render('Y', False, 'white')
              screen.blit(text_surface, coord[pointer])
              pointer+=1 
              guess.append('y')
            if event.key == pygame.K_z:
              text_surface = font.render('Z', False, 'white')
              screen.blit(text_surface, coord[pointer])
              pointer+=1
              guess.append('z')

      pygame.display.update()
     
      clock.tick(60)  

    pygame.quit()
    
  def wordle():
    return list(random.choice(dictionary.words))
  
  def check_pos(self, wordle, trial):
    for x, y in zip(wordle, trial):
      if x == y:
        self.info.append("green")     #This is when the letter is in the correct position 
      elif y in wordle:
        self.info.append("yellow")      #This is when the letter is in the wrong position but is still in the word to guess
      else:
        self.info.append("black")    #This is when the letter is incorrect/not in the word that you are trying to guess
    
  
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
