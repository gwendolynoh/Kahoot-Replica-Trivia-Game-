from questions import Questions

class Dictionary: 
  def __init__(self):
    filename = [
      "assets/bradpitt.png", 
      "assets/dwayne.png", 
      "assets/ben.png",
      "assets/jenniferanderson.png", 
      "assets/tom.png",
      "assets/taylor.png", 
      "assets/johnnydepp.png", 
      "assets/leo.png",
      "assets/ladygaga.png", 
      "assets/willsmith.png"
    ]
    
    prompt = [
      "Who is this?\n(red) Brad Pitt\n(blue) Sean Penn\n(green) Simon Cowell\n(yellow) Cory Monteith\n\n",
      "Who is this?\n(red) Marisa Tomei\n(blue) Jennifer Garner\n(green) Dwayne Johnson\n(yellow) Eminem\n\n",
      "Who is this?\n(red) Ben Affleck\n(blue) George Clooney\n(green) Johnny Depp\n(yellow) Dwayne Johnson\n\n",
      "Who is this?\n(red) Miley Cyrus\n(blue) Jennifer Anderson\n(green) Jennifer Lawrence\n(yellow) Ellen DeGeneres\n\n",
      "Who is this?\n(red) Ashton Kutcher\n(blue) Snoop Dogg\n(green) John Travolta\n(yellow) Tom Cruise\n\n",
      "Who is this?\n(red) Julia Roberts\n(blue) Taylor Swift\n(green) Britney Spears\n(yellow) Beyoncé\n\n",
      "Who is this?\n(red),Johnny Depp\n(blue) Arnold Schwarzenegger\n(green) Justin Timberlake\n(yellow) Mel Gibson\n\n",
      "Who is this?\n(red),Tom Hanks\n(blue) Jay Z\n(green) Leonardo DiCaprio\n(yellow) Ben Affleck\n\n",
      "Who is this?\n(red),Celine Dion\n(blue) Jennifer Lawrence\n(green) Natalie Portman\n(yellow) Lady Gaga\n\n",
      "Who is this?\n(red),Will Smith\n(blue) Dwayne Johnson\n(green) Justin Bieber\n(yellow) Mel Gibson\n\n",
    ]
    
    questions = [
      Questions(prompt[0], 'red',filename[0]),
      Questions(prompt[1], 'green',filename[1]),
      Questions(prompt[2], 'red',filename[2]),
      Questions(prompt[3], 'blue', filename[3]),
      Questions(prompt[4], 'yellow', filename[4]),
      Questions(prompt[5], 'blue', filename[5]),
      Questions(prompt[6], 'red', filename[6]),
      Questions(prompt[7], 'green', filename[7]),
      Questions(prompt[8], 'yellow', filename[8]),
      Questions(prompt[9], 'red', filename[9])
    ]
