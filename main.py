"""
Main module to run the Pong game.
"""

import pygame
from Scripts.game import Game

def main() -> None:
    """
    Main function to initialize and run the Pong game.
    """
    pygame.init()
    screen_width, screen_height = 800, 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('Pong')

    game = Game(screen_width, screen_height)

    running = True
    show_menu = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    show_menu = False

        if show_menu:
            screen.fill((0, 0, 0))
            font = pygame.font.Font(None, 74)
            text = font.render("PONG", True, (255, 255, 255))
            screen.blit(text, (screen_width // 2 - text.get_width() // 2, screen_height // 4))

            instructions = font.render("Press ENTER to Start", True, (255, 255, 255))
            screen.blit(instructions, (screen_width // 2 - instructions.get_width() // 2, screen_height // 2))

            how_to_play_font = pygame.font.Font(None, 36)
            how_to_play = how_to_play_font.render("W/S: Move Left Paddle", True, (255, 255, 255))
            screen.blit(how_to_play, (screen_width // 2 - how_to_play.get_width() // 2, screen_height // 2 + 50))
            how_to_play = how_to_play_font.render("UP/DOWN: Move Right Paddle", True, (255, 255, 255))
            screen.blit(how_to_play, (screen_width // 2 - how_to_play.get_width() // 2, screen_height // 2 + 90))

            pygame.display.flip()
        else:
            game.update()
            game.draw(screen)
            pygame.display.flip()
            pygame.time.Clock().tick(60)

    pygame.quit()

if __name__ == '__main__':
    main()
