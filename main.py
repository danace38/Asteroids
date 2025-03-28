# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    background = pygame.image.load("background.jpg").convert()
    clock = pygame.time.Clock()
    dt = 0

    # Variable counters for score tracking
    asteroids_destroyed = 0
    big_asteroid = 0
    medium_asteroid = 0
    small_asteroid = 0

    font = pygame.font.SysFont(None, 25)

    # pygame groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # Set containers ofr the Player and Asteroid classes 
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()

    # Instantiate the player at the center of the screen
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

 
    #Infinite loop for the game main loop. This will display GUI filled with black color background.
    while True:
        updatable.update(dt)
        total_score = (big_asteroid * 5) + (medium_asteroid * 3) + (small_asteroid * 1)
        
        destoyed_text = font.render(f"Total Destroyed Asteroids: {asteroids_destroyed} ", True, (255, 255, 255))
        big_text = font.render(f"Big Asteroid Points: {big_asteroid * 5} ", True, (255, 255, 255))
        medium_text = font.render(f"Medium Asteroid Points: {medium_asteroid * 3} ", True, (255, 255, 255))
        small_text = font.render(f"Small Asteroid Points: {small_asteroid * 1} ", True, (255, 255, 255))
        total_text = font.render(f"Total Points: {total_score}", True, (255, 255, 255))


        for asteroid in asteroids:
            if asteroid.check_collisions(player):
                print("Game over!")
                sys.exit()
            
            for shot in shots:
                if asteroid.check_collisions(shot):
                    shot.kill()
                    asteroid.split()
                    asteroids_destroyed += 1
                    
                    if asteroid.radius >= 60:
                        big_asteroid += 1
                    elif asteroid.radius >= 40:
                        medium_asteroid += 1
                    else:
                        small_asteroid += 1
     
                 
        screen.blit(background, (0,0))
        screen.blit(big_text, (20, 20))
        screen.blit(medium_text, (300, 20))
        screen.blit(small_text, (600, 20))  
        screen.blit(total_text, (20, 50))
        screen.blit(destoyed_text, (20, 76))

        for obj in drawable:
            obj.draw(screen)
        
        pygame.display.flip()
        pygame.display.set_caption("Asteroids Game")
        
        # This limits the framerate to 60 FPS
        dt = clock.tick(60) / 1000

        #This will check if the user has closed the window and exit the game loop if they do.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
    

if __name__ == "__main__":
    main()

