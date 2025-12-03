import constants
import circleshape
import pygame
from logger import log_event
import random

class Asteroid (circleshape.CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)
        self.rotation = 0

    def draw(self,screen):
        pygame.draw.circle(screen,'white',self.position,self.radius,width=constants.LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= constants.ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            ang = random.uniform(20,50)
            v1 = self.velocity.rotate(ang)
            v2 = self.velocity.rotate(-ang)
            self.radius -= constants.ASTEROID_MIN_RADIUS

            asteroid1 = Asteroid(self.position.x, self.position.y, self.radius)
            asteroid1.velocity = v1 * 1.2
            asteroid2 = Asteroid(self.position.x, self.position.y, self.radius)
            asteroid2.velocity = v2 * 1.2
