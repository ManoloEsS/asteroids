from sys import exit

import pygame

from game_assets.asteroid import Asteroid
from game_assets.asteroidfield import AsteroidField
from constants import constants as c
from game_assets.player import Player
from game_assets.shot import Shot


def main():
    pygame.init()
    screen = pygame.display.set_mode((c.SCREEN_WIDTH, c.SCREEN_HEIGHT))
    fps = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    field = AsteroidField()
    Shot.containers = (shots, updatable, drawable)

    Player.containers = (updatable, drawable)
    x = c.SCREEN_WIDTH / 2
    y = c.SCREEN_HEIGHT / 2
    player1 = Player(x, y)

    dt = 0

    # starts in middle of screen
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)

        for asteroid in asteroids:
            if player1.collision(asteroid):
                print("Game Over!")
                exit()

            for shot in shots:
                if asteroid.collision(shot):
                    shot.kill()
                    asteroid.split()

        screen.fill((0, 0, 0))

        for items in drawable:
            items.draw(screen)

        pygame.display.flip()

        dt = fps.tick(60) / 1000


if __name__ == "__main__":
    main()
