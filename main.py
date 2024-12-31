import pygame
import sys
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player
from asteroid import Asteroid
from asteroidfields import AsteroidField
from shot import Shot

def main():
    pygame.init()
    game_font = pygame.font.Font(None, 64)
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()
    shots_group = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots_group, updatable, drawable)
    player = Player(x,y)
    asteroidfield = AsteroidField()
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
            asteroidfield.update(dt)
            for sprite in updatable:
                sprite.update(dt)
            for sprite in drawable:
                sprite.draw(screen)
            for sprite in asteroids:
                if sprite.collisions(player):
                    game_over_text = game_font.render("Game Over!", True, (255, 0, 0))
                    text_rect = game_over_text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
                    screen.blit(game_over_text, text_rect)
                    pygame.display.flip()
                    pygame.time.wait(2000)  # 2000 milliseconds = 2 seconds
                    print("Game Over!")  
                    sys.exit()
            pygame.display.flip()
            dt = clock.tick(60) / 1000
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        pygame.quit()

if __name__ == "__main__":
    main()
