"""
Module for Ball class in the Pong game.
"""

import pygame

class Ball:
    """
    Represents the ball in the Pong game.
    """

    def __init__(self, x: int, y: int, size: int, speed_x: int, speed_y: int) -> None:
        """
        Initializes a Ball instance.

        :param x: The x-coordinate of the ball.
        :param y: The y-coordinate of the ball.
        :param size: The size (diameter) of the ball.
        :param speed_x: The speed of the ball in the x-direction.
        :param speed_y: The speed of the ball in the y-direction.
        """
        self.rect: pygame.Rect = pygame.Rect(x, y, size, size)
        self.speed_x: int = speed_x
        self.speed_y: int = speed_y

    def move(self) -> None:
        """
        Moves the ball according to its speed.
        """
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

    def bounce(self, screen_height: int) -> None:
        """
        Bounces the ball off the top and bottom of the screen.

        :param screen_height: The height of the game screen.
        """
        if self.rect.top <= 0 or self.rect.bottom >= screen_height:
            self.speed_y *= -1

    def reset_position(self, screen_width: int, screen_height: int) -> None:
        """
        Resets the ball to the center of the screen and reverses its x-direction.

        :param screen_width: The width of the game screen.
        :param screen_height: The height of the game screen.
        """
        self.rect.center = (screen_width // 2, screen_height // 2)
        self.speed_x *= -1

    def draw(self, screen: pygame.Surface) -> None:
        """
        Draws the ball on the screen.

        :param screen: The Pygame screen surface.
        """
        pygame.draw.ellipse(screen, (255, 255, 255), self.rect)
