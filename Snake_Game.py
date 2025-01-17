# -> Importing The Libiraries
import pygame
import random
import os

pygame.init() # --> Calling Constructor
pygame.mixer.init() # --> Calling Music and image constructor


screen_width = 900 # --> Set Width
screen_height = 600 # --> Set Height

# -->set Colors  👇👇👇
white =(255,255,255) # -->rgb values of colors
red = (255,0,0) # -->rgb values of colors
black = (0,0,0) # -->rgb values of colors

game_Window = pygame.display.set_mode((screen_width,screen_height)) # --> Set The Screen Window of pygame
pygame.display.set_caption("Snake Game") # --> Set Title of game Window
pygame.display.update() # --> Update The Window
bgimg = pygame.image.load("bg.jpg") # --> Load the Images
bgimg = pygame.transform.scale(bgimg,(screen_width,screen_height)).convert_alpha() # --> convert alpha --> when continusoly image work in game loop due to aplha --> speed of processing does not affect

clock = pygame.time.Clock() # --> Calling Clock function to handle the time
font = pygame.font.SysFont(None,35) # --> Set the font and style

# --> Making Function to Set the text on the Screen 👇👇👇
def ScreenData(text,color,x,y):
    screen_text = font.render(text,True,color)
    game_Window.blit(screen_text,[x,y])


# --> Making Function to plot the snake on the Screen 👇👇👇
def plot_snake(gameWindow, color, snk_list, snake_size):
    for x,y in snk_list:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])


# --> Making Function to Make the home screen of game👇👇👇
def Welcome():
    exit_game = False
    while not exit_game:
        game_Window.fill((233,220,229))
        ScreenData("Welcome to Snake Game",black,260,250)
        ScreenData("Press Space Bar to Play",black,263,290) 
        # --> Create the event of button 
        for event in  pygame.event.get():
            if event.type == pygame.QUIT: # --> For quit
                exit_game = True
            elif event.type == pygame.KEYDOWN : # --> For press key in the keyboard
                if event.key == pygame.K_SPACE:  # --> Space bar button
                    pygame.mixer.music.load('back.mp3') # --> load the music
                    pygame.mixer.music.play()      # --> play the music
                    GameLoop()      # --> Calling game loop function
        pygame.display.update() # --> update function of pygame
        clock.tick(60)    # --> clock update after 60 second         


# -->Making function to set the game loop 
def GameLoop():
    # --> Varaible in PyGame
    exit_game = False
    game_over = False
    score = 0
    # --> Snake axis X and Y
    snake_X = 45
    snake_Y = 55
    snake_Size = 17 # --> Size Of Snake Head and Food
    # --> Velocity of x and y equal then snake moves to diagonal position 
    velocity_x = 0
    velocity_y = 0
    init_velocity = 5 # --> Set the speed of Snake at the initial
    food_x = random.randint(20, int(screen_width/2))
    food_y = random.randint(20, int(screen_height/2))
    fps = 30 # --> Frame Per Seconds # --> Set the Speed --> fps Increase Speed Increase 

    snk_list = []  # --> Making list that store all axis of snake
    snk_length = 1

    if not os.path.exists("hiscore.txt"): # --> Check the file exit or not
        with open("hiscore.txt", "w") as f:
            f.write("0")
    with open("hiscore.txt", "r") as f:
        hiscore = f.read()

    # --> Creating A Game Loop
    while not exit_game:
        if game_over:
            with open("hiscore.txt", "w") as f:
                f.write(str(hiscore))
            game_Window.fill(white)
            # --> Show Message on the Screen
            ScreenData("Game Over !!Press Enter to continue", red, 200, 200)
            ScreenData("Score: " + str(score), red, 230, 230)
            for event in pygame.event.get():
                if event.type == pygame.QUIT: # --> For quit the game 
                    exit_game = True

                if event.type == pygame.KEYDOWN: # --> For press key in the keyboard
                    if event.key == pygame.K_RETURN: # --> This is enter key of keyboard
                        Welcome()
                        exit_game = True    
        else:    
            # --> Event Handling In Pygame 
            for event in pygame.event.get():
                if event.type == pygame.QUIT: # --> For quit the game 
                    exit_game = True
                if event.type == pygame.KEYDOWN: # --> For detect the key arrow button in keyboard
                    if event.key == pygame.K_RIGHT: # --> Right Arrow key
                        velocity_x = init_velocity
                        velocity_y = 0  
                    if event.key == pygame.K_LEFT: # --> Left Arrow key
                        velocity_x = - init_velocity
                        velocity_y = 0  
                    if event.key == pygame.K_UP: # --> Up Arrow key
                        velocity_y = - init_velocity 
                        velocity_x = 0 
                    if event.key == pygame.K_DOWN: # --> Down Arrow key
                        velocity_y =  init_velocity
                        velocity_x = 0
                    if event.key == pygame.K_q: # --> Cheat Button
                        score += 10
                        if score > int(hiscore):
                            hiscore = score   
            snake_X = snake_X + velocity_x # --> Change the axis of Snake --> means --> move to next position
            snake_Y = snake_Y + velocity_y # --> Change the axis of Snake --> means --> move to next position


            if abs(snake_X - food_x) < 6 and (snake_Y - food_y) < 6: # --> Condition for eating food
                score += 10   
                snk_length += 4  
            
                food_x = random.randint(20, int(screen_width/2))
                food_y = random.randint(20, int(screen_height/2)) 
                if score > int(hiscore):
                    hiscore = score     

            game_Window.fill(white)
            game_Window.blit(bgimg, (0, 0)) # --> Set the photo on the background

            border_thickness = 5 # --> Border thickness
            # --> Making Border of game loop
            border_rect = pygame.Rect(border_thickness, border_thickness, screen_width - 2 * border_thickness,
                                      screen_height - 2 * border_thickness)
            # --> draw border on page
            pygame.draw.rect(game_Window, white, border_rect, border_thickness)

            # --> Show the score on the screen
            ScreenData("Score: " + str(score) + "  Hiscore: " + str(hiscore), red, 5, 5)
            pygame.draw.rect(game_Window, red, [food_x, food_y, snake_Size, snake_Size]) # --> Creating the Food of Snake
            
            # --> Size of snake increase
            head = []
            head.append(snake_X)
            head.append(snake_Y)
            snk_list.append(head)

            if len(snk_list) > snk_length:
                del snk_list[0]

            # --> Check the condition for game over
            if head in snk_list[:-1]:
                game_over = True 
                # --> Game Over Music
                pygame.mixer.music.load('gameover.mp3') # --> Music load
                pygame.mixer.music.play()   # --> music play

            # --> Check the condition for game over
            if snake_X < 0 or snake_X > screen_width or snake_Y < 0 or snake_Y > screen_height:
                game_over = True  
                pygame.mixer.music.load('gameover.mp3') # --> Music load
                pygame.mixer.music.play() # --> music play
            
            plot_snake(game_Window, black, snk_list, snake_Size) # --> Make the screen on the screen
        pygame.display.update()
        clock.tick(fps) # --> clock update after fps second  

    pygame.quit()
    quit()


# --> Main Function Start
Welcome()