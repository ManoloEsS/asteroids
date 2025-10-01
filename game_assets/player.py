import pygame

from game_assets import circleshape
from constants import constants
from game_assets.shot import Shot


class Player(circleshape.CircleShape):
    """Represents the player's spaceship."""

    def __init__(self, x: float, y: float) -> None:
        """Initialize a Player object.
        
        Args:
            x: The x-coordinate of the player's starting position.
            y: The y-coordinate of the player's starting position.
        """
        super().__init__(x, y, constants.PLAYER_RADIUS)
        self.rotation = 0
        self.player_timer = 0

    def triangle(self) -> list[pygame.Vector2]:
        """Calculate the vertices of the player's triangle shape.
        
        Returns:
            A list of three Vector2 objects representing the triangle vertices.
        """
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen: pygame.Surface) -> None:
        """Draw the player's spaceship on the screen.
        
        Args:
            screen: The pygame Surface to draw on.
        """
        pygame.draw.polygon(screen, (255, 255, 255), self.triangle(), 2)

    def rotate(self, dt: float) -> None:
        """Rotate the player's spaceship.
        
        Args:
            dt: Delta time in seconds since the last update (can be negative for counter-clockwise rotation).
        """
        self.rotation += constants.PLAYER_TURN_SPEED * dt

    def update(self, dt: float) -> None:
        """Update the player's state based on keyboard input.
        
        Args:
            dt: Delta time in seconds since the last update.
        """
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()

        self.player_timer -= dt
        self.player_timer = max(self.player_timer, 0)

    def move(self, dt: float) -> None:
        """Move the player forward or backward.
        
        Args:
            dt: Delta time in seconds since the last update (can be negative for backward movement).
        """
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * constants.PLAYER_SPEED * dt

    def shoot(self) -> None:
        """Fire a shot if the cooldown has expired.
        
        Creates a new Shot object in the direction the player is facing
        and starts the cooldown timer.
        """
        if not self.player_timer > 0:
            shot = Shot(self.position.x, self.position.y)
            shot.velocity = (
                pygame.Vector2(0, 1).rotate(self.rotation) * constants.PLAYER_SHOT_SPEED
            )
            self.player_timer = constants.PLAYER_SHOOT_COOLDOWN
