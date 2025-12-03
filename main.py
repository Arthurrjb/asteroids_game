import sys
import pygame
import player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from logger import log_state, log_event
from constants import *
from shot import Shot

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}") 
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt=0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    player.Player.containers = (updatable, drawable)
    AsteroidField.containers = (updatable,)
    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    player1 = player.Player(SCREEN_WIDTH / 2,SCREEN_HEIGHT / 2,PLAYER_RADIUS)
    asteroid_field = AsteroidField()
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        updatable.update(dt)
        
        for asteroide in asteroids:
            if player1.collides_with(asteroide):
                log_event("player_hit")
                print("Game Over!")
                sys.exit()
        
        for asteroide in asteroids:
            for shote in shots:
                if shote.collides_with(asteroide):
                    log_event("asteroid_shot")
                    shote.kill()
                    asteroide.kill()


        for thing in drawable:
            thing.draw(screen)

        pygame.display.flip()
        dt=clock.tick(60)/1000

if __name__ == "__main__":
    main()
