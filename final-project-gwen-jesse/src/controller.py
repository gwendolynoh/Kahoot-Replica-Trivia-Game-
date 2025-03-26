import pygame
import random 
import pygame.mixer
from .questions import Questions
from .constants import filename, prompt

class Controller:
  def __init__(self):
    '''
    This initializes the screen with the window display as well as the color buttons and background in the game. It also includes the imported quiz dictionary, that includes the prompt, answer, and picture file. 
    '''
    #Window display
    pygame.init()
    pygame.display.init()
    pygame.mixer.init()
    x , y = 600 , 400
    self.window = pygame.display.set_mode((x,y))
    background = "white"
    self.window.fill(background)
    pygame.display.flip()

    self.window.fill("black")
    red_rect = pygame.Rect(0, 200, 100, 100)
    blue_rect = pygame.Rect(100, 200, 100, 100)
    green_rect = pygame.Rect(0, 300, 100, 100)
    yellow_rect = pygame.Rect(100, 300, 100, 100)
    self.red_guess = pygame.draw.rect(self.window, "red", red_rect)
    self.blue_guess = pygame.draw.rect(self.window, "blue", blue_rect)
    self.green_guess = pygame.draw.rect(self.window, "green", green_rect)
    self.yellow_guess = pygame.draw.rect(self.window, "yellow", yellow_rect)
    pygame.display.flip()
    

    #Baord Game display 
    boards = pygame.transform.scale(pygame.image.load('assets/background.png'),(400,400))
    self.window.blit(boards,(200,0))
    pygame.display.update()
    pygame.display.flip()

    
    self.questions = [
      Questions(prompt[0], 'red',filename[0]),
      Questions(prompt[1], 'green',filename[1]),
      Questions(prompt[2], 'red',filename[2]),
      Questions(prompt[3], 'blue', filename[3]),
      Questions(prompt[4], 'yellow', filename[4]),
      Questions(prompt[5], 'yellow', filename[5]),
      Questions(prompt[6], 'red', filename[6]),
      Questions(prompt[7], 'green', filename[7]),
      Questions(prompt[8], 'yellow', filename[8]),
      Questions(prompt[9], 'red', filename[9])
    ]
  
  
  def quiz_test(self):
    '''
    The quiz_test() method uses a event loop to connect the color boxes on the screen to the possible answer choices from the dictionary. This function is the core of the game it checks the players answers to the correct answer from the dictionary. In the function it also blits the image of the mushroom to the screen based on the amount of correct answers the players gets in the quiz. 
    '''
    color = ['red','blue','green','yellow']
    score = 0
    q_num = 0 
    ply_xcoord = 160
    ply_ycoord = 185
    
    pygame.mixer.music.load("assets/quiz-121408.mp3")
    pygame.mixer.music.set_volume(4)
    pygame.mixer.music.play()
    
    for question in self.questions:
      print(question.prompt)
      answer = True
      while answer == True:  
        for event in pygame.event.get():
          if event.type == pygame.MOUSEBUTTONDOWN:
            if self.red_guess.collidepoint(pygame.mouse.get_pos()):
              answer = color[0]
              print("Your picked RED")
            elif self.blue_guess.collidepoint(pygame.mouse.get_pos()):
              answer = color[1]
              print("You picked BLUE")
            elif self.green_guess.collidepoint(pygame.mouse.get_pos()):
              answer = color[2]
              print("You picked GREEN")
            elif self.yellow_guess.collidepoint(pygame.mouse.get_pos()):
              answer = color[3]
              print("You picked YELLOW")
        picture = pygame.transform.scale(pygame.image.load(self.questions[q_num].filename),(200,200))
        self.window.blit(picture,(0,0))
        pygame.display.update()
        pygame.display.flip()
        pygame.time.wait(2000)
      if answer == question.answer:
        print("You are correct!!")
        score += 1
        q_num += 1
        if score == score:
          new_pos = ply_xcoord + 35 * score
          player_position = pygame.transform.scale(pygame.image.load('assets/mushroom.png'),(50,50))
          self.window.blit(player_position,(new_pos,ply_ycoord))
          pygame.display.update()
          print("Congrats you planted" + str(score) + "mushrooms")
      else: 
        print("Sorry try again :(")
        q_num += 1
    print("You got:" + str(score) + "/" + str(len(self.questions)))

  def cpu_pos(self):
    '''
    The cup_pos method is what acts as the "compter" that the player is compeating against. It generates a random number that acts as "the amount of mushrooms" the computer planted. 
    '''
    comp_xpos = 200
    comp_ypos = 293
    a , b = 0 , 11
    turns = random.randrange(a,b)
    for i in range(turns):
      coord = comp_xpos + 35 * i
      cpu_pos = pygame.transform.scale(pygame.image.load('assets/cpu.png'),(50,50))
      self.window.blit(cpu_pos,(coord,comp_ypos))    
      pygame.display.update() 
    print("Can you plant more than" +  str(i+1)  + "mushrooms")

  
  def gameoverloop(self):
    '''
    This method is what ends the game after the quiz is complete and the mushrooms are drawn based oin correct answer 
    '''
    x = 600
    y = 400
    pygame.display.set_caption('Game Over')
    font = pygame.font.Font('assets/Urban-Tribe.ttf', 32)
    text = font.render('Game Over', True, "light green")
    textRect = text.get_rect()
    textRect.center = (x // 2, y // 2)
    over_screen = pygame.transform.scale(pygame.image.load('assets/background.png'),(600,400))
    self.window.blit(over_screen,(0,0))
    pygame.display.update()
    pygame.display.flip()
    while True:
      self.window.blit(text, textRect)
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
           pygame.quit()
           quit()
        pygame.display.update()