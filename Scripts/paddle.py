"""
Module for Paddle class in the Pong game.
"""

import pygame

class Paddle:
    """
    Represents a paddle in the Pong game.
    """

    def __init__(self, x: int, y: int, width: int, height: int, speed: int) -> None:
        """
        Initializes a Paddle instance.

        :param x: The x-coordinate of the paddle.
        :param y: The y-coordinate of the paddle.
        :param width: The width of the paddle.
        :param height: The height of the paddle.
        :param speed: The speed of the paddle.
        """
        self.rect: pygame.Rect = pygame.Rect(x, y, width, height)
        self.speed: int = speed

    def move(self, up: bool, down: bool, screen_height: int) -> None:
        """
        Moves the paddle up or down.

        :param up: Boolean indicating if the paddle should move up.
        :param down: Boolean indicating if the paddle should move down.
        :param screen_height: The height of the game screen.
        """
        if up and self.rect.top > 0:
            self.rect.y -= self.speed
        if down and self.rect.bottom < screen_height:
            self.rect.y += self.speed

    def draw(self, screen: pygame.Surface) -> None:
        """
        Draws the paddle on the screen.

        :param screen: The Pygame screen surface.
        """
        pygame.draw.rect(screen, (255, 255, 255), self.rect)
