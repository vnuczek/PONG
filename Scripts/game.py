"""
Module for the Game class which manages the Pong game.
"""

import pygame
from Scripts.paddle import Paddle
from Scripts.ball import Ball

class Game:
    """
    Manages the Pong game including the paddles, ball, and game logic.
    """

    def __init__(self, screen_width: int, screen_height: int) -> None:
        """
        Initializes a Game instance.

        :param screen_width: The width of the game screen.
        :param screen_height: The height of the game screen.
        """
        self.screen_width: int = screen_width
        self.screen_height: int = screen_height
        self.paddle_speed: int = 10
        self.ball_speed: int = 7

        self.left_paddle: Paddle = Paddle(50, screen_height // 2 - 50, 10, 100, self.paddle_speed)
        self.right_paddle: Paddle = Paddle(screen_width - 60, screen_height // 2 - 50, 10, 100, self.paddle_speed)
        self.ball: Ball = Ball(screen_width // 2 - 5, screen_height // 2 - 5, 10, self.ball_speed, self.ball_speed)

        self.left_score: int = 0
        self.right_score: int = 0
        self.font: pygame.font.Font = pygame.font.Font(None, 74)

    def update(self) -> None:
        """
        Updates the game state including paddle and ball positions.
        """
        keys = pygame.key.get_pressed()
        self.left_paddle.move(keys[pygame.K_w], keys[pygame.K_s], self.screen_height)
        self.right_paddle.move(keys[pygame.K_UP], keys[pygame.K_DOWN], self.screen_height)
        self.ball.move()
        self.ball.bounce(self.screen_height)

        # Ball collision with paddles
        if self.ball.rect.colliderect(self.left_paddle.rect) or self.ball.rect.colliderect(self.right_paddle.rect):
            self.ball.speed_x *= -1

        # Ball out of bounds
        if self.ball.rect.left <= 0:
            self.right_score += 1
            self.ball.reset_position(self.screen_width, self.screen_height)
        if self.ball.rect.right >= self.screen_width:
            self.left_score += 1
            self.ball.reset_position(self.screen_width, self.screen_height)

    def draw(self, screen: pygame.Surface) -> None:
        """
        Draws all game elements on the screen.

        :param screen: The Pygame screen surface.
        """
        screen.fill((0, 0, 0))
        self.left_paddle.draw(screen)
        self.right_paddle.draw(screen)
        self.ball.draw(screen)
        pygame.draw.aaline(screen, (255, 255, 255), (self.screen_width // 2, 0), (self.screen_width // 2, self.screen_height))

        left_text = self.font.render(str(self.left_score), True, (255, 255, 255))
        screen.blit(left_text, (self.screen_width // 4, 20))
        right_text = self.font.render(str(self.right_score), True, (255, 255, 255))
        screen.blit(right_text, (self.screen_width // 4 * 3, 20))
