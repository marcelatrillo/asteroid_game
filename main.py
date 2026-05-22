import pygame
import sys
from constants import SCREEN_HEIGHT,SCREEN_WIDTH
from logger import log_state, log_event
from player import Player
from asteroids import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0.0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Shot.containers = (shots, drawable, updatable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    asteroidfield = AsteroidField()

    Player.containers = (updatable, drawable)
    player = Player(x = SCREEN_WIDTH / 2,y = SCREEN_HEIGHT / 2)

    while True: 
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)
        for asteroid in asteroids:
            if asteroid.collides_with(player)== True:
                log_event("player_hit")
                print( "Game Over!")
                sys.exit()

        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collides_with(shot)== True:
                    log_event("asteroid_shot")
                    shot.kill()
                    asteroid.split() 

                

        screen.fill("black")

        for thing in drawable:
            thing.draw(screen)

        pygame.display.flip()

        dt = clock.tick(60)/1000
        
        
        

if __name__ == "__main__":
    main()
