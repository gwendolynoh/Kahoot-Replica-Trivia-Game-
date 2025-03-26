## Project Description
The project is a quiz game that askes questions related to python terms. The idea is that the more questions you get correct you plant x amount of mushrooms which you are trying to beat the computer in how many mushrooms you can plant. The goal of this game is to help you memorize common python terms while competing against the computer. 

If pygame not installed enter "pip3 install pygame" in terminal

***    

## User Interface Design

- **Initial Concept**
  -[initial game screen] (assets/initialgamestart.jpg)
  '''
  The initial game screen was based off of random celebrities in which the player has to guess the right one to move onto the next quyestion.
  '''
  -[initial game end screen] (etc/initialgamestart.jpg)
  '''
  The initial game end screen did not change it is just game over put onto the screen
  '''
  -[initial design] (etc/initial.jpg)
  '''
  The initial design was to guess the celebrity but then that idea changed to a quiz game that is more useful
  '''
    
- **Final GUI**
  - [Game Screen] (etc/gamescreen.png)
  - [Game Over Screen] (etc/gameoverscreen.png)

***        

## Program Design

* Non-Standard libraries
    
* Class Interface Design
  [class diagram](src/85708.jpg) 

* Classes
- class Controller
  - '''
The controller is what keeps all functions. It sets up the screen in the game as well as the background and buttons. It also is where all the other functions are displayed and called. There are 3 different functions in the controller quiz_test() which is used to make the buttons on the screen work and connects the dictionary to the the the buttons. Next, we have the cpu_pos() which is the function that creates a random about of mushrooms that the player is trying to beat. Finally, gameendloop() function is what ends the game once the quiz is complete. 
'''
-class Question
'''
The Question class is used for the dictionary to connect the questions, answers, and picture files that are connected to each question. 
'''


## Project Structure and File List

The Project is broken down into the following file structure:

* main.py
* src
    * constants.py
    * controller.py
    * questions.py
    * 
* assets
    * background.png
    * cpu.png
    * mushroom.png
    * Q1.png
    * Q2.png
    * Q3.png
    * Q4.png
    * Q5.png
    * Q6.png
    * Q7.png
    * Q8.png
    * Q9.png
    * Q10.png
    * quiz-121408.mp3
    * Urban-Tribe.ttf
* etc
    * gameoverscreen.png
    * gamescreen.png
    * initial.jpg
    * initialgameover.jpg
    * initialgamestart.jpg 
***

## ATP

| Step                 |Procedure             |Expected Results                   |
|----------------------|:--------------------:|----------------------------------:|
|  1                   | Open terminal and enter: python3 main.py| GUI creen will appear with 4 different color boxes which are the buttons.  | 
|  2                   | Click on the color you believe is the correct answer   | -If correct the shell will print "You are correct!!" and a mushroom will appear on the screen -If incorrect "Sorry try again :(" will be displayed in the console and move to the next question   |
|3                     | Continue to click the color for your answer | -When quiz is over you score will print in the console and the number of mushrooms displayed is how many answers you got correct. -If the amount of mushrooms you planeted is greater than the blue mushroom (CPU) then you win. 
    