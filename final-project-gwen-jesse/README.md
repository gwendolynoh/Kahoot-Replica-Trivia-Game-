:warning: Everything between << >> needs to be replaced (remove << >> after replacing)
# CS110 Project Proposal
# << Project Title >>
## CS 110 Final Project
###   Fall, 2022
### [Assignment Description](https://docs.google.com/document/d/1H4R6yLL7som1lglyXWZ04RvTp_RvRFCCBn6sqv-82ps/edit?usp=sharing)


**https://replit.com/join/vmrlclcdfa-gwendolynoh**

Google Slides; 
**https://docs.google.com/presentation/d/1ClMwH9cy6r-x1ARuYlC4f-4gXD1kbJxvnAANKwSpp0Q/edit?usp=sharing)**

####  Gwendolyn Oh

***

## Project Description
Our project is a quiz game that askes questions related to python terms. The idea is that the more questions you get correct you plant x amount of mushrooms which you are trying to beat the computer in how many mushrooms you can plant. The goal of this game is to help you memorize common python terms while competing against the computer. 

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

## Tasks and Responsibilities 
We worked as a team bouncing ideas off one another. Although, Jesse was responsible for getting the pictures and the music. Gwen was responsible for making the dictionaries and the colored buttons. Other than that, we both worked together to figure it out. 
## Testing
We did not hesistate to test. Right after we would make a loop we would test it. We also tested each step individually just to make sure that it was working, for example: making the picture appear, next we tested to make sure the picture and the boxes appeared, then we tested to make sure the boxes worked, then we kept testing to see if the quiz would work with the boxes, and so on. 

## ATP

| Step                 |Procedure             |Expected Results                   |
|----------------------|:--------------------:|----------------------------------:|
|  1                   | Open terminal and enter: python3 main.py| GUI creen will appear with 4 different color boxes which are the buttons.  | 
|  2                   | Click on the color you believe is the correct answer   | -If correct the shell will print "You are correct!!" and a mushroom will appear on the screen -If incorrect "Sorry try again :(" will be displayed in the console and move to the next question   |
|3                     | Continue to click the color for your answer | -When quiz is over you score will print in the console and the number of mushrooms displayed is how many answers you got correct. -If the amount of mushrooms you planeted is greater than the blue mushroom (CPU) then you win. 
    