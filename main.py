# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    # pygame groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    # Set containers ofr the Player and Asteroid classes 
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()

    # Instantiate the player at the center of the screen
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

 
    #Infinite loop for the game loop. This will display GUI filled with black color background.
    while True:
        updatable.update(dt)

        for asteroid in asteroids:
            if asteroid.check_collisions(player):
                print("Game over!")
                sys.exit()

        screen.fill("black")

        for obj in drawable:
            obj.draw(screen)
        
        pygame.display.flip()
        
        #This will check if the user has closed the window and exit the game loop if they do.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # This limits the framerate to 60 FPS
        dt = clock.tick(60) / 1000

        
    
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()

