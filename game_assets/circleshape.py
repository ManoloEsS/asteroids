import pygame


class CircleShape(pygame.sprite.Sprite):
    """Base class for circular game objects.
    
    Inherits from pygame.sprite.Sprite and provides common functionality
    for objects with circular collision detection.
    """
    
    def __init__(self, x: float, y: float, radius: float) -> None:
        """Initialize a CircleShape object.
        
        Args:
            x: The x-coordinate of the object's position.
            y: The y-coordinate of the object's position.
            radius: The radius of the circular object.
        """
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen: pygame.Surface) -> None:
        """Draw the object on the screen.
        
        Args:
            screen: The pygame Surface to draw on.
        """
        pass

    def update(self, dt: float) -> None:
        """Update the object's state.
        
        Args:
            dt: Delta time in seconds since the last update.
        """
        pass

    def collision(self, other: "CircleShape") -> bool:
        """Check if this object collides with another CircleShape.
        
        Args:
            other: Another CircleShape object to check collision with.
            
        Returns:
            True if the objects are colliding, False otherwise.
        """
        distance = pygame.math.Vector2.distance_to(self.position, other.position)
        return distance <= self.radius + other.radius
