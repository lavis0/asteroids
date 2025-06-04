import pygame
from circleshape import CircleShape
from constants import *
from random import uniform

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, 'white', self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            angle = uniform(20,50)
            split1 = Asteroid(self.position[0], self.position[1], self.radius - ASTEROID_MIN_RADIUS)
            split2 = Asteroid(self.position[0], self.position[1], self.radius - ASTEROID_MIN_RADIUS)
            split1.velocity = self.velocity.rotate(angle) * 1.2
            split2.velocity = self.velocity.rotate(-angle) * 1.2