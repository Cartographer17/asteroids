import pygame
from constants  import *

def main():
    pygame.init()
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
    except: 
        raise KeyboardInterrupt()
        

if __name__ == "__main__":
    main()
