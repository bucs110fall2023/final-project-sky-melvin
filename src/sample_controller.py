import pygame
import random
import dictionary

pygame.init()
class Controller:
  
  def __init__(self):
    self.screen = pygame.display.set_mode((500, 520))
    self.font = pygame.font.Font(None, 80)
    self.font2 = pygame.font.Font(None, 20)
    self.clock = pygame.time.Clock()
    self.running = True
    self.menu = True
    self.restart = False
    self.num_letters=6

    
    self.attempts=0
    self.pointer=0
    self.end_limit=6
    self.front_limit=0
    self.count=0 # amount of tries
    self.wordle=Controller.wordle()
    self.wordle2=list(self.wordle)
    self.guess=[]
    self.info = []
    

      
     
      
    
  def wordle():
    return random.choice(dictionary.words)
  
  def check_pos(self, wordle, trial):
    for x, y in zip(wordle, trial):
      if x == y:
        self.info.append("green")     #This is when the letter is in the correct position 
      elif y in wordle:
        self.info.append("yellow")      #This is when the letter is in the wrong position but is still in the word to guess
      else:
        self.info.append("black")    #This is when the letter is incorrect/not in the word that you are trying to guess
    
  
  def mainloop(self):
    Controller.menuloop(self)
    if not self.menu:
      Controller.gameloop(self)
    
    
  
  ### below are some sample loop states ###

  def menuloop(self):
    while self.menu:
      self.screen.fill("grey")
      text_surface = self.font.render("Hexa-Wordle", False, 'black')
      self.screen.blit(text_surface, (75, 25))
      pygame.draw.polygon(self.screen, "green", [(100,200), (400,200), (400,300), (100,300)])
      startbox = pygame.Rect(100,200,300,100)
      text_surface = self.font.render("START", False, 'black')
      self.screen.blit(text_surface, (160, 225))
      pygame.display.flip()
      for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
          raise SystemExit 
        elif event.type == pygame.MOUSEBUTTONDOWN: 
          if event.button == 1: 
            pos = pygame.mouse.get_pos()
            start = startbox.collidepoint(pos)
            if start:
              self.menu = False
            else:
              self.menu = True
      
      #event loop

      #update data

      #redraw
      
  def gameloop(self):
    while self.running:
      if not self.restart:
        self.screen.fill("grey")
        text_surface = self.font.render("Hexa-Wordle", False, 'black')
        self.screen.blit(text_surface, (75, 25))
        self.x_coord = 100
        self.y_coord = 50
        self.coord=[]
        for h in range(self.num_letters):
          self.y_coord = self.y_coord + 50
          for w in range(self.num_letters):
            self.coord.append([self.x_coord,self.y_coord])
            pygame.draw.rect(self.screen, "black", [self.x_coord, self.y_coord, 45, 45])
            self.x_coord = self.x_coord + 50
          self.x_coord = 100
          self.restart = True
      else:
        pass
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          self.running = False
        if self.count==6:
          pygame.quit()
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_RETURN:
            if self.pointer%6==0 and self.pointer>=self.end_limit: #Only press enter with 6 letter word and can't immediatley press enter to skip to other lines
              Controller.check_pos(self ,self.wordle2, self.guess)
              print(self.wordle2)
              print(self.guess)
              print(self.info)
              self.guess = [item.upper() for item in self.guess]
              for w in range(self.front_limit,self.end_limit):
                pygame.draw.rect(self.screen, self.info[w-self.front_limit], [self.coord[w][0], self.coord[w][1], 45, 45])
                text_surface = self.font.render(self.guess[w-self.front_limit], False, 'white')
                self.screen.blit(text_surface, self.coord[w])
              self.attempts = self.attempts + 1
              
              for j in range(self.num_letters): #Checking if player guessed word correctly 
                equal=True
                if self.info[j]=='green':
                  continue
                else:
                  equal=False
                  break
                  
                
              self.guess.clear()
              self.info.clear()

              self.front_limit=self.end_limit #store previous end limit as front limit before increasing end_limit
              self.end_limit+=6
              self.count+=1
                
              if equal==True: #What to do when player guess word correctly
                self.restart = True
                Controller.gameoverloop(self)
              
              if equal==False and self.attempts==6:
                self.restart = True
                Controller.gameoverloop(self)
                
              
                
             
              
          if event.key == pygame.K_BACKSPACE:
              if self.pointer>self.front_limit:
                self.guess.pop()
                self.pointer-=1
              if self.pointer==self.end_limit:
                self.pointer-=2
                pygame.draw.rect(self.screen, "black", [self.coord[self.pointer][0],self.coord[self.pointer][1], 45, 45])
              pygame.draw.rect(self.screen, "black", [self.coord[self.pointer][0],self.coord[self.pointer][1], 45, 45])
          if self.pointer==self.end_limit:
            pass
          else:
            if event.key == pygame.K_a:
              text_surface = self.font.render('A', False, 'white')
              self.screen.blit(text_surface, self.coord[self.pointer])
              self.pointer+=1
              self.guess.append('a')
            if event.key == pygame.K_b:
              text_surface = self.font.render('B', False, 'white')
              self.screen.blit(text_surface, self.coord[self.pointer])
              self.pointer+=1
              self.guess.append('b')
            if event.key == pygame.K_c:
              text_surface = self.font.render('C', False, 'white')
              self.screen.blit(text_surface, self.coord[self.pointer])
              self.pointer+=1
              self.guess.append('c')
            if event.key == pygame.K_d:
              text_surface = self.font.render('D', False, 'white')
              self.screen.blit(text_surface, self.coord[self.pointer])
              self.pointer+=1
              self.guess.append('d')
            if event.key == pygame.K_e:
              text_surface = self.font.render('E', False, 'white')
              self.screen.blit(text_surface, self.coord[self.pointer])
              self.pointer+=1
              self.guess.append('e')
            if event.key == pygame.K_f:
              text_surface = self.font.render('F', False, 'white')
              self.screen.blit(text_surface, self.coord[self.pointer])
              self.pointer+=1
              self.guess.append('f')
            if event.key == pygame.K_g:
              text_surface = self.font.render('G', False, 'white')
              self.screen.blit(text_surface, self.coord[self.pointer])
              self.pointer+=1
              self.guess.append('g')
            if event.key == pygame.K_h:
              text_surface = self.font.render('H', False, 'white')
              self.screen.blit(text_surface, self.coord[self.pointer])
              self.pointer+=1
              self.guess.append('h')
            if event.key == pygame.K_i:
              text_surface = self.font.render('I', False, 'white')
              self.screen.blit(text_surface, self.coord[self.pointer])
              self.pointer+=1
              self.guess.append('i')
            if event.key == pygame.K_j:
              text_surface = self.font.render('J', False, 'white')
              self.screen.blit(text_surface, self.coord[self.pointer])
              self.pointer+=1
              self.guess.append('j')
            if event.key == pygame.K_k:
              text_surface = self.font.render('K', False, 'white')
              self.screen.blit(text_surface, self.coord[self.pointer])
              self.pointer+=1
              self.guess.append('k')
            if event.key == pygame.K_l:
              text_surface = self.font.render('L', False, 'white')
              self.screen.blit(text_surface, self.coord[self.pointer])
              self.pointer+=1
              self.guess.append('l')
            if event.key == pygame.K_m:
              text_surface = self.font.render('M', False, 'white')
              self.screen.blit(text_surface, self.coord[self.pointer])
              self.pointer+=1
              self.guess.append('m')
            if event.key == pygame.K_n:
              text_surface = self.font.render('N', False, 'white')
              self.screen.blit(text_surface, self.coord[self.pointer])
              self.pointer+=1
              self.guess.append('n')
            if event.key == pygame.K_o:
              text_surface = self.font.render('O', False, 'white')
              self.screen.blit(text_surface, self.coord[self.pointer])
              self.pointer+=1
              self.guess.append('o')
            if event.key == pygame.K_p:
              text_surface = self.font.render('P', False, 'white')
              self.screen.blit(text_surface, self.coord[self.pointer])
              self.pointer+=1
              self.guess.append('p')
            if event.key == pygame.K_q:
              text_surface = self.font.render('Q', False, 'white')
              self.screen.blit(text_surface, self.coord[self.pointer])
              self.pointer+=1
              self.guess.append('q')
            if event.key == pygame.K_r:
              text_surface = self.font.render('R', False, 'white')
              self.screen.blit(text_surface, self.coord[self.pointer])
              self.pointer+=1
              self.guess.append('r')
            if event.key == pygame.K_s:
              text_surface = self.font.render('S', False, 'white')
              self.screen.blit(text_surface, self.coord[self.pointer])
              self.pointer+=1
              self.guess.append('s')
            if event.key == pygame.K_t:
              text_surface = self.font.render('T', False, 'white')
              self.screen.blit(text_surface, self.coord[self.pointer])
              self.pointer+=1
              self.guess.append('t')
            if event.key == pygame.K_u:
              text_surface = self.font.render('U', False, 'white')
              self.screen.blit(text_surface, self.coord[self.pointer])
              self.pointer+=1
              self.guess.append('u')
            if event.key == pygame.K_v:
              text_surface = self.font.render('V', False, 'white')
              self.screen.blit(text_surface, self.coord[self.pointer])
              self.pointer+=1
              self.guess.append('v')
            if event.key == pygame.K_w:
              text_surface = self.font.render('W', False, 'white')
              self.screen.blit(text_surface, self.coord[self.pointer])
              self.pointer+=1
              self.guess.append('w')
            if event.key == pygame.K_x:
              text_surface = self.font.render('X', False, 'white')
              self.screen.blit(text_surface, self.coord[self.pointer])
              self.pointer+=1
              self.guess.append('x')
            if event.key == pygame.K_y:
              text_surface = self.font.render('Y', False, 'white')
              self.screen.blit(text_surface, self.coord[self.pointer])
              self.pointer+=1 
              self.guess.append('y')
            if event.key == pygame.K_z:
              text_surface = self.font.render('Z', False, 'white')
              self.screen.blit(text_surface, self.coord[self.pointer])
              self.pointer+=1
              self.guess.append('z')
      
      pygame.display.update()
      
      self.clock.tick(60)  

    pygame.quit()
      #event loop

      #update data

      #redraw
    
  def gameoverloop(self):
    if self.attempts < 6:
      while self.restart:
        self.screen.fill("grey")
        text_surface = self.font.render("Hexa-Wordle", False, 'black')
        self.screen.blit(text_surface, (75, 25))
        text_surface_2 = self.font2.render("You got the correct word! It took you " + str(self.attempts) + " tries. If you want to restart, press the button. Otherwise close the screen.", False, "black")
        self.screen.blit(text_surface_2, (0, 30))
        pygame.draw.polygon(self.screen, "blue", [(100,200), (400,200), (400,300), (100,300)])
        restartbox = pygame.Rect(100,200,300,100)
        text_surface = self.font.render("RESTART", False, 'black')
        self.screen.blit(text_surface, (125, 225))
        pygame.display.flip()
        for event in pygame.event.get(): 
          if event.type == pygame.QUIT: 
            raise SystemExit 
          elif event.type == pygame.MOUSEBUTTONDOWN: 
            if event.button == 1: 
              pos = pygame.mouse.get_pos()
              restart = restartbox.collidepoint(pos)
              if restart:
                self.restart = False
                self.__init__()
                Controller.gameloop(self)
              else:
                self.restart = True
    else:
      while self.restart:
        self.screen.fill("grey")
        text_surface = self.font.render("Hexa-Wordle", False, 'black')
        self.screen.blit(text_surface, (75, 25))
        text_surface_2 = self.font2.render("Sorry. The word was " + self.wordle + ". If you want to restart, press the button. Otherwise close the screen.", False, "black")
        self.screen.blit(text_surface_2, (0, 30))
        pygame.draw.polygon(self.screen, "blue", [(100,200), (400,200), (400,300), (100,300)])
        restartbox = pygame.Rect(100,200,300,100)
        text_surface = self.font.render("RESTART", False, 'black')
        self.screen.blit(text_surface, (125, 225))
        pygame.display.flip()
        for event in pygame.event.get(): 
          if event.type == pygame.QUIT: 
            raise SystemExit 
          elif event.type == pygame.MOUSEBUTTONDOWN: 
            if event.button == 1: 
              pos = pygame.mouse.get_pos()
              restart = restartbox.collidepoint(pos)
              if restart:
                self.restart = False
                self.__init__()
                Controller.gameloop(self)
              else:
                self.restart = True
      #event loop

      #update data

      #redraw
