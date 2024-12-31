import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player

def main():
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x,y)
    pygame.init()
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
            player.update(dt)
            player.draw(screen)  # Ensure the player is drawn before flipping
            pygame.display.flip()
            dt = clock.tick(60) / 1000
    except KeyboardInterrupt: 
        print("Game interrupted by keyboard.")
    finally:
        pygame.quit()

if __name__ == "__main__":
    main()
