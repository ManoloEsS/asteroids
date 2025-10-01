import random

import pygame

from constants import constants
from game_assets.circleshape import CircleShape
from constants.constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    """Represents an asteroid in the game."""
    
    def __init__(self, x: float, y: float, radius: float) -> None:
        """Initialize an Asteroid object.
        
        Args:
            x: The x-coordinate of the asteroid's position.
            y: The y-coordinate of the asteroid's position.
            radius: The radius of the asteroid.
        """
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface) -> None:
        """Draw the asteroid on the screen.
        
        Args:
            screen: The pygame Surface to draw on.
        """
        pygame.draw.circle(screen, "green", self.position, self.radius, 2)

    def update(self, dt: float) -> None:
        """Update the asteroid's position.
        
        Args:
            dt: Delta time in seconds since the last update.
        """
        self.position += self.velocity * dt

    def split(self) -> None:
        """Split the asteroid into two smaller asteroids.
        
        Removes this asteroid and creates two new smaller asteroids
        moving in different directions. Does nothing if the asteroid
        is already at minimum size.
        """
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        angle = random.uniform(20, 50)

        vector1 = self.velocity.rotate(angle)
        vector2 = self.velocity.rotate(-angle)

        new_radius = self.radius - constants.ASTEROID_MIN_RADIUS

        new_asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid_1.velocity = vector1 * 1.2
        new_asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid_2.velocity = vector2 * 1.2

    def rotate(self, angle: float, dt: float) -> None:
        """Rotate the asteroid.
        
        Args:
            angle: The angle to rotate by (in degrees per second).
            dt: Delta time in seconds since the last update.
        """
        self.rotation += angle * dt
