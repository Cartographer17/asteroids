import pygame
from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED
from shot import Shot
from constants import PLAYER_SHOOT_SPEED


class Player(CircleShape, pygame.sprite.Sprite):
    containers = None
    def __init__(self, x, y):
        CircleShape.__init__(self, x, y, PLAYER_RADIUS)
        pygame.sprite.Sprite.__init__(self)
        self.rotation = 0
        self.time = 0
        self.shoot_allowed = True
        if self.containers:
            self.add(self.containers)

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def update(self, dt):
        if self.time > 0:
            self.time -= dt
            if self.time <= 0:
                self.shoot_allowed = True
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rotation += PLAYER_TURN_SPEED * dt
        if keys[pygame.K_d]:
            self.rotation -= PLAYER_TURN_SPEED * dt
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        if self.shoot_allowed:
            new_shot = Shot(self.position.x, self.position.y)
            shot_direction = pygame.Vector2(0, 1).rotate(self.rotation)
            new_shot.velocity = shot_direction * PLAYER_SHOOT_SPEED

            # Set the cooldown timer and disallow shooting
            self.time = 0.3  # Assuming 0.3 seconds is your cooldown time
            self.shoot_allowed = False

