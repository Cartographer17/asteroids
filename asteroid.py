import pygame
from circleshape import CircleShape

class Asteroid(CircleShape):
    containers = None

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)  # Ensures base class attributes are set
        self.width = 2

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), (int(self.position.x), int(self.position.y)), self.radius, self.width)

    def update(self, dt):
        self.position += self.velocity * dt