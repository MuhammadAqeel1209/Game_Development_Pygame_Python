import pygame
pygame.init()
gameWindow = pygame.display.set_mode((1200, 500)) # --> (width,height)
pygame.display.set_caption("My First Game")

# --> Varaible in PyGame
exit_game = False
game_over = False

# --> Creating A Game Loop

while not exit_game:
    # --> Event Handling In Pygame
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # --> For quit the game
            exit_game = True
        if event.type == pygame.KEYDOWN: # --> For detect the key arrow button in keyboard
            if event.key == pygame.K_RIGHT:
                print("Press Right arrow Key")
            if event.key == pygame.K_LEFT:
                print("Press Left arrow Key")
            if event.key == pygame.K_UP:
                print("Press Up arrow Key")
            if event.key == pygame.K_DOWN:
                print("Press Down arrow Key")

pygame.quit()
quit()

# --> https://www.pygame.org/docs/ --> Documentation of pygame