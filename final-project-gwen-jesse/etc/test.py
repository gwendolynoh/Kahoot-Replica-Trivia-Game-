import pygame


pygame.init()
pygame.display.init()
pygame.mixer.init()
x , y = 600 , 400
window = pygame.display.set_mode((x,y))
background = "white"
window.fill(background)
pygame.display.flip()


#Buttons 
window.fill("black")
red_rect = pygame.Rect(0, 200, 100, 100)
blue_rect = pygame.Rect(100, 200, 100, 100)
green_rect = pygame.Rect(0, 300, 100, 100)
yellow_rect = pygame.Rect(100, 300, 100, 100)
red_guess = pygame.draw.rect(window, "red", red_rect)
blue_guess = pygame.draw.rect(window, "blue", blue_rect)
green_guess = pygame.draw.rect(window, "green", green_rect)
yellow_guess = pygame.draw.rect(window, "yellow", yellow_rect)
pygame.display.flip()

#Baord Game display 
boards = pygame.transform.scale(pygame.image.load('assets/background.png'),(400,400))
window.blit(boards,(200,0))
pygame.display.update()
pygame.display.flip()
def position():
      x = 0
      y = 0
      while True:
        for event in pygame.event.get():
          if event.type == pygame.MOUSEBUTTONDOWN:
            coords = pygame.mouse.get_pos(x,y)
            print(coords)
position()