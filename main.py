# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame

import constants
import player


def main():
    pygame.init()
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    print("Starting Asteroids!")
    print(f"Screen width: {constants.SCREEN_WIDTH}")
    print(f"Screen height: {constants.SCREEN_HEIGHT}")

    fps = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    player.Player.containers = (updatable, drawable)
    # starts in middle of screen
    x = constants.SCREEN_WIDTH / 2
    y = constants.SCREEN_HEIGHT / 2
    player1 = player.Player(x, y)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)

        screen.fill((0, 0, 0))
        for items in drawable:
            items.draw(screen)

        pygame.display.flip()
        fps.tick(60)
        dt = fps.tick(60) / 1000


if __name__ == "__main__":
    main()
