# Import "pygame", "time" and "random" modules 
import pygame
import time
import random

# Initialize "pygame"
pygame.init() 

# Create a game screen and set its title 
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption("Car Racing Game")

# Create a "carx", "cary" and "bgy" variables to track car and background positions
carx = 140
cary = 450
bgy = 0
# Create a variable "threshold" and set its value to zero
threshold = 0

# TA1a-Step 1: Create a counter variable to keep track of gameloop iterations


# TA1c-Step 1: Choose random x and y locations for stone placement



# Game loop
carryOn = True
# Create first time point "t1" 
t1 = time.time()
while carryOn:
    # NOTE: The images file and .py file in which image is being used must be in same folder
    
    # Display the background image
    bgImg_name = "road.png"
    bgImg = pygame.image.load(bgImg_name).convert_alpha()
    bgImg_scaled = pygame.transform.smoothscale(bgImg,(650,600))
    screen.blit(bgImg_scaled,(0,0))
    
    # Display the yellow car image
    yellow_car_name = "yellow_car.png"
    yellow_car = pygame.image.load(yellow_car_name).convert_alpha()
    yellow_car_scaled = pygame.transform.smoothscale(yellow_car,(230,150))
    
    # TA1c-Step 2: Display the stone image



    
    # Check for up, down, left, right, spacebar and enter key events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            carryOn = False              
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                cary -= 10
                bgy -= 10
            if event.key == pygame.K_DOWN:
                cary += 10
                bgy += 10
            if event.key==pygame.K_RIGHT:
                if carx <= 320:
                    carx += 10
            if event.key==pygame.K_LEFT:
                if carx >= 50:                          
                    carx -= 10 
            if event.key == pygame.K_SPACE:
                if carx < 260: 
                    carx += 90
            if event.key == pygame.K_RETURN:
                if game_time >= threshold and game_time <= (threshold+10):
                    cary -= 50 
                    threshold += 10
                
    # Reset car and backgroun positions
    if cary <= 30:
        bgy = 0
        cary = 450
        # TA1a-Step 2: Increment counter and print the "counter" variable value 
        # Everytime car position is reset increment counter by 1

        # Print the number of gameloop iterations completed.

        # TA1c-Step 3: Update the stone's x and y locations after incrementing the counter 


        
    # TA1d_Step 1: Create rectangle for car and stone




    # TA1d_Step 2: Draw rectangles for car ic color (100,0,100) and stone in color (0,0,100)


    # TA1d-Step 3: If car and stone rectangles collide

        # Set car position to its initial position 

        # Change the position of stone


        
    # Display yellow car image upon updating "carx" and "cary" variable values
    screen.blit(yellow_car_scaled,(carx, cary))
    
    # TA1c-Step 4: Display the stone upon updating "stone_x" and "stone_y" variable values  

    
    # Create second time point "t2" 
    t2 = time.time()
    game_time = t2-t1
    game_time = round(game_time, 2)
    
    # Display game time elapsed
    font = pygame.font.Font(None, 35)
    text = font.render("TIME ELAPSED: " + str(game_time)+ "seconds", 1, (0, 255,255))
    screen.blit(text, (130,15))
    
    # TA1a-Step 3: Display finish line after 5 iterations of game loop
    # Check if "counter" is equal to 5

        # Create and draw the finish line white-colored rectangle at (x,y)=(95, 40) with width=400 and height=30



        # Display "----------FINISH----------" text in a color with rgb combination as (255,0,0)




        
        # TA1b-Step 1: End the game loop after displaying finish line



        # Display finish time in seconds text


        # Display "Game Over, Good Luck Next Time!" text





        # Break out of 'while' game loop
        
    
    # Update the contents of the display
    pygame.display.flip()
    
# On the occurence of "pygame.QUIT" event close the game screen.
pygame.quit()