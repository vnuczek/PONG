# Description for the Pong Game Project

This project is a classic implementation of the Pong game using Python and the Pygame library. The game features a simple start menu, two-player controls, and a scoring system. Players can control the paddles using the keyboard, and the game includes basic collision detection and ball movement mechanics.

## Features:

- **Two-player Gameplay:** Control the left paddle using the `w` and `s` keys, and the right paddle using the `UP` and `DOWN` arrow keys.
- **Simple Start Menu:** The game includes a start menu with instructions on how to play. Press `ENTER` to start the game.
- **Scoring System:** The game keeps track of the score for both players.
- **Collision Detection:** The ball bounces off the paddles and the top and bottom edges of the screen.
- **Reset Mechanism:** The ball resets to the center of the screen after a point is scored.

## File Structure:

- `main.py`: Entry point of the game that initializes and runs the game loop.
- `Scripts/paddle.py`: Contains the `Paddle` class, which represents the paddles in the game.
- `Scripts/ball.py`: Contains the `Ball` class, which represents the ball in the game.
- `Scripts/game.py`: Contains the `Game` class, which manages the overall game logic.
