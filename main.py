import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player

def main():
    pygame.init()
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    player = Player(x,y)
    clock = pygame.time.Clock()
    dt = 0
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode ((SCREEN_WIDTH, SCREEN_HEIGHT))
    try:
    # Your game loop and other code
        while True:
            for event in pygame.event.get():  
                if event.type == pygame.QUIT: 
                    return
                elif event.type == pygame.KEYDOWN:  
                    if event.key == pygame.K_ESCAPE:  
                        return 
            screen.fill((0,0,0))
            for sprite in updatable:
                sprite.update(dt)
            for sprite in drawable:
                sprite.draw(screen)
            pygame.display.flip()
            dt = clock.tick(60) / 1000
    except KeyboardInterrupt: 
        print("Game interrupted by keyboard.")
    finally:
        pygame.quit()

if __name__ == "__main__":
    main()
