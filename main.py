# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys
from player import *
from constants import *
from asteroidfield import *
from asteroid import *
from shot import *

def main():
    pygame.init()

    print("Starting asteroids!")
    print(f'Screen width: {SCREEN_WIDTH}')
    print(f'Screen height: {SCREEN_HEIGHT}')
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updateable, drawable)
    Asteroid.containers = (updateable, drawable, asteroids)
    Shot.containers = (updateable, drawable, shots)
    AsteroidField.containers = (updateable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT /2)
    asteroidField = AsteroidField()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        pygame.Surface.fill(screen, (0,0,0))
        for drawableObj in drawable:
            drawableObj.draw(screen)
        for updateableObj in updateable:
            updateableObj.update(dt)

        killShots = []
        killAsteroids = []
        for asteroid in asteroids:
            if asteroid.collision(player):
                print("Game over!")
                sys.exit()

            for shot in shots:
                if shot.collision(asteroid):
                    shot.kill()
                    asteroid.split()

        pygame.display.flip()
        dt = clock.tick(60) / 1000
        
if __name__ == "__main__":
    main()