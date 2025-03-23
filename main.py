# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
 
    #Infinite loop for the game loop. This will display GUI filled with black color background.
    while True:
        screen.fill("black")
        pygame.display.flip()
        
        #This will check if the user has closed the window and exit the game loop if they do.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return



    
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()

