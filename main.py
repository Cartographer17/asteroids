import pygame
from constants  import *

class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass


def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode ((SCREEN_WIDTH, SCREEN_HEIGHT))
    try:
        while True:
            for event in pygame.event.get():  
                if event.type == pygame.QUIT: 
                    return
                elif event.type == pygame.KEYDOWN:  
                    if event.key == pygame.K_ESCAPE:  
                        return 
            screen.fill((0,0,0))
            pygame.display.flip()
            dt = clock.tick(60)/1000
            
    except: 
        raise KeyboardInterrupt()
        

if __name__ == "__main__":
    main()
