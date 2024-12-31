import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS

class Shot(CircleShape):
    def __init__(self, position_x, position_y):
        super().__init__(position_x, position_y, SHOT_RADIUS)

    def update(self, dt):
        # Update position based on velocity
        self.position += self.velocity * dt

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius)