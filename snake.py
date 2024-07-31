def setup():
    global x
    global y
    global window
    global dotX
    global dotY
    global score
    global img, img2, img3, img4, img5, img6, img7, img8, img9, img10
    global question_answered, user_answered, correct_answer
    import random
    import math
    global apple_counter

    #apple counter
    apple_counter = 0

    #Position of snake
    score = 0   
    x = 100
    y = 100

    # Position of the red dot
    dotX = random.randint(0,5)*100
    dotY = random.randint(0,3)*100

    if dotX > 500 - 50 or dotY > 400 - 50:
        dotX = random.randint(0,5)*100
        dotY = random.randint(0,3)*100

    #for the math question
    question_answered = False
    user_answered = False
    user_answer = None

    #all the images that are used in the code
    img = loadImage("snake-removebg-preview.png")
    img2 = loadImage ("images__1_-removebg-preview.png")
    img3 = loadImage ("snake-removebg-preview (1).png")
    img4 = loadImage ("instruction.png")
    img5 = loadImage ("546502-middle-removebg-preview.png")
    img6 = loadImage ("snakes_and-removebg-preview.png")
    img7 = loadImage ("download-removebg-preview.png")
    img8 = loadImage ("pples-removebg-preview.png")
    img9 = loadImage ("images__1_-removebg-preview.png")
    img10 = loadImage ("download__1_-removebg-preview.png")
    
    #main setup part for the background; includes size of window, background and more variables
    background (60, 179, 113)
    size (500, 400)    
    window = 1

    score = 0
    #Position of snake
    x = 100
    y = 100

    # Position of the red dot
    dotX = random.randint(0,5)*100
    dotY = random.randint(0,3)*100

    if dotX > 500 - 50 or dotY > 400 - 50:
        dotX = random.randint(0,5)*100
        dotY = random.randint(0,3)*100

def menu():
    #menu/homepage for my game 
   
    global window
    global img, img2, img3, img4, img5, img6, img7, img8, img9, img10
    global question_answered, user_answered
    
    #tracks my mouse movement and tells me the x and y coordinates. the framerate is to update the coordinates of the mouse as fast as possible
    frameRate(40)
    println(str(mouseX) + " : " + str(mouseY))

    #this is for the main rectangle (the large one thats in the middle of the screen that contains the title) and     makes the rectangular box around it
    fill (173, 216, 230)
    rect(110, 20, 280, 280, 28)

    #this is for the main rectangle but this part of the code is to write the title and make the snake image
    image (img6, 95, 25, width/2, height/8) 
    image (img7, 125, 72, width/12, height/8) 
    image (img8, 155, 80, width/4.5, height/7) 
    image (img, 173, 12) #snake image
    image (img9, 93, 100, width/3, height/2) 
    image (img10, 280, 190, width/5, height/4)

    #this is for the left button on the bottom of the homepage; it's for the play button and icon beside it
    fill (3, 36, 127)
    rect (110, 310, 190, 80, 28)
    fill (255)
    triangle (152, 332, 152, 357, 175, 343) #play icon 
    fill (255)
    textSize(30)
    text("Play", 190, 357)

    #this is for the right button on the bottom of the homepage; its for the instructions button and icon
    fill (3, 36, 127)
    rect (310, 310, 80, 80, 28) #right button on how to play
    image (img4, 325, 322, img4.width/10, img4.height/10)#instruction icon


def draw():
    global question_answered, user_answered
    #this is to set up the different windows I will be having (such as the play window, instructions window, etc)
    global window

    #for the homepage window
    if window == 1:
        menu()

    #for the instructions window which will explain on how to play
    elif window == 2:
        instructions()

    #for the question window which will prompt the user math question and then let them answer it
    elif window == 3:
        question()

    #for the actual game window
    elif window == 4:
        askNum()    
    
    elif window == 5:
        snake_game()
        
    elif window == 6:
        game_over()

    
def game_over():
    #for the game over screen
    frameRate(40)
    println(str(mouseX) + " : " + str(mouseY))
    background (0)
    fill(255,0,0) # red color
    text("Incorrect.", 155, 180)
    text ("Game over.", 155, 220)    
    fill (255, 0, 0)
    rect (110, 260, 280, 50, 28)
    fill (255)
    text ("Return to home.", 130, 295)

def instructions():
    global question_answered, user_answered
    #for window when u press on instructions. the instructions tab describes on how to play the game and gives a detailed explanation on how to play

    #this is required or nothing would be able to be clicked on meaning the buttons would not take you anywhere if clicked
    frameRate(40)
    println(str(mouseX) + " : " + str(mouseY))

    global img, img2, img3
    #this is for the background of that page
    background(144, 238, 144)

    #this is for the title of the page which is How to Play
    fill (0, 0, 128)
    rect (143, 20, 200, 70, 28) 
    image (img2, 0, -20)
    image (img3, 350, 10)
    fill (255)
    text ("How to play", 182, 62)

    #this is to make the square in the middle of the page which will contain the body text
    rect (20, 110, 340, 260, 28) 
    fill (0)

    #this is to make the text that explains on how to play the game. 
    textSize (20)
    text ("It's simple really! The objective ", 30, 140)
    text ("of the game is to eat as many", 30, 160)
    text ("apples possible; boosting your", 30, 180)
    text ("score. You control a snake which", 30, 200)
    text ("roams around a certain plane", 30, 220)
    text ("eating apples and avoiding the ", 30, 240)
    text ("outer edges of the playing area.", 30, 260)
    text ("The catch? Well, you need to be", 30, 280)
    text ("able to answer mathematical", 30, 300)
    text ("questions in order to continue", 30, 320)
    text ("on. Go on and test your skills in ", 30, 340)
    text ("Snakes and Apples!", 30, 360)

    #back button on top left of the page that takes you to the homepage
    fill (21,71,52) 
    rect (0, 0, 90, 25)
    fill (255)
    text ("Back", 18, 20)


def question():
    global question_answered, user_answered
    #have to add this on every page to allow the user to be able to press the buttons
    frameRate(40)
    println(str(mouseX) + " : " + str(mouseY))

    global img, img2, img3, img4, img5
    #images
    background (144, 238, 144)
    image (img, -20, -20)
    image (img5, 310, 200, height/1, width/2)   

    #for the are u ready text box and text
    fill (173, 216, 230)
    rect (22.5, 90, 450, 100, 28) 
    fill (0)
    text ("Are you ready to be tested?", 40.5, 150) 
    
    #yes text box and text
    fill (173, 216, 230)
    rect (130, 230, 100, 50, 28) #yes box
    fill (0)
    text ("Yes", 154, 263.5)
    
    #no text box and text
    fill (173, 216, 230)
    rect (270, 230, 100, 50, 28) #no box
    fill (0)
    text ("No", 300.5, 263.5)

    #back button
    fill (21,71,52) #back button
    rect (0, 0, 120, 27)
    fill (255)
    text ("Back", 18, 24)
