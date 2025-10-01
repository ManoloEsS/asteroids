import pygame

from game_assets.circleshape import CircleShape
from constants.constants import SHOT_RADIUS


class Shot(CircleShape):
    """Represents a projectile shot by the player."""
    
    def __init__(self, x: float, y: float) -> None:
        """Initialize a Shot object.
        
        Args:
            x: The x-coordinate of the shot's starting position.
            y: The y-coordinate of the shot's starting position.
        """
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen: pygame.Surface) -> None:
        """Draw the shot on the screen.
        
        Args:
            screen: The pygame Surface to draw on.
        """
        pygame.draw.circle(screen, "red", self.position, self.radius, 2)

    def update(self, dt: float) -> None:
        """Update the shot's position.
        
        Args:
            dt: Delta time in seconds since the last update.
        """
        self.position += self.velocity * dt
