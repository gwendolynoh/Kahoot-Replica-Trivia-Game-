import pygame
from src.controller import Controller



def main():
  '''
  The main() function is what calls the Class Controller() that holds all the methods that creates this game.
  '''
  pygame.init()
  test = Controller()
  test.cpu_pos()
  test.quiz_test()
  test.gameoverloop()
  
if __name__ == '__main__':
  main() 
