# Snake Game Development with Pygame

This README file provides instructions and details about the Python-based Snake game developed using the Pygame module. The game features a background image, sound effects, and a high-score saving mechanism.

---

## Features

1. **Background Image**: The background image (`bg.jpg`) is displayed during gameplay.
2. **Sound Effects**:
   - `gameover.mp3`: Plays when the player loses the game.
   - `back.mp3`: Plays as background music during gameplay.
3. **High Score Saving**:
   - `hiscore.txt`: Stores the highest score achieved by the player.
4. **Game File**:
   - The main game script is named `Snake_Game.py`.

---

## Prerequisites

To run the game, ensure you have the following installed on your system:

1. **Python** (version 3.6 or higher)
2. **Pygame module**
   - Install it using the command:
     ```bash
     pip install pygame
     ```

---

## Files and Resources

- `Snake_Game.py`: Main game script.
- `bg.jpg`: Background image used during the game.
- `gameover.mp3`: Sound effect for game over.
- `back.mp3`: Background music during gameplay.
- `hiscore.txt`: Text file to save the highest score.

---

## How to Run the Game

1. Clone or download the repository.
2. Ensure all the required files (`bg.jpg`, `gameover.mp3`, `back.mp3`, `hiscore.txt`) are in the same directory as `Snake_Game.py`.
3. Open a terminal or command prompt and navigate to the game directory.
4. Run the game using the command:
   ```bash
   python Snake_Game.py
   ```

---

## Gameplay Instructions

1. Use the arrow keys to move the snake.
2. Collect food to grow the snake and increase the score.
3. Avoid colliding with the walls or the snake’s own body.
4. When the game ends, the highest score is saved in `hiscore.txt`.

---

## Customization

### Changing the Background Image

Replace `bg.jpg` with your desired background image. Ensure the file name and extension remain the same.

### Updating Sounds

- Replace `gameover.mp3` and `back.mp3` with your preferred audio files.
- Ensure the file names and extensions remain unchanged.

### Resetting High Score

To reset the high score, open `hiscore.txt` and replace its content with `0`.

---

## Dependencies

- **Pygame**: Used for rendering graphics, handling events, and managing the game loop.

Install it using:

```bash
pip install pygame
```

---

## License

This project is open-source and can be used or modified for educational and personal purposes.

---

## Author

**Muhammad Aqeel**

- [GitHub](https://github.com/MuhammadAqeel1209)
- [LinkedIn](https://www.linkedin.com/in/muhammad-aqeel-a04716279/)
