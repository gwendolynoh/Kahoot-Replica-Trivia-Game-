
# Final Project Milestone II

*Place this document in your final project repo folder `/etc`. *

***

Come up with interfaces for 3 possible classes you think you may need for your project. Again, brainstorm a little. Nothing is *wrong*.

## Class Interface 1
class Character:
'''
Creates the player in our maze game and sets it to the rest position (0,0) on screen. It will allow players to move on screen using the arrow keys. 
'''
  def __init__(self,x,y):
    self.position = (x,y)
    self.image = (str)
    self.character.shirt_color("")
    self.character.right()
    self.character.left()
    self.character.forward()
    self.character.backward()
  
## Class Interface 2
class Riddle:
'''
The Riddle is placed at the end of each level to move on to more challanging levels in the game. It will uses text that displays the riddle using a random generator from a dictionary.
'''
  def __init__(self,x,y):
    self.x = x
    self.y = y 
    self.positon = (self.x,self.y)
  
  def dictionary():
    riddle = ([r1..., r2..., r3..."dictionary"])
    select = random(riddle)
    text = print(select)
    answer = int(input("What is your answer?"))

  def result():
    key = ([k1...,k2...,k3...])
    if answer is key:
      print("your right")
    else:
      print("your wrong")
    
    
    
## Class Interface 3
pen = turtle.Turtle()

class Maze_lines:
'''
The Maze line creates the boarders in the game and is used as the "wall" on the surface so that creates the puzzle the players will have to solve. It uses Turtle to draw the lines on the game using position and the turtle interface. 
'''
  def __init__(self,x,y):
    self.up()
    self.pen_goto = (x,y)
    self.forward()
    self.backward()
    self.pen_down()

======================================================================
