# Tic Tac Toe Game

## Introduction
This is a simple implementation of the classic Tic Tac Toe game in Python using the Pygame library for the graphical interface and Tkinter for displaying end-of-game messages. The game allows you to play against an AI opponent.

## Prerequisites
Make sure you have Python installed on your system. You can download Python from [python.org](https://www.python.org/downloads/).

Additionally, you need to have the Pygame library installed. You can install it using the following command:

```bash
pip install pygame
```

## How to Run the Game

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/your-username/tic-tac-toe.git
   ```

   Alternatively, you can download the ZIP file and extract it.

2. **Navigate to the Project Directory:**

   ```bash
   cd tic-tac-toe
   ```

3. **Run the Game:**

   Execute the following command to run the game:

   ```bash
   python tic_tac_toe.py
   ```

   The game window will appear, and you can start playing Tic Tac Toe.

## How to Play

1. When you run the game, you will be prompted to choose whether you want to play as 'X' or 'O'.
2. Click on the corresponding button to make your choice.
3. The game board will be displayed, and you can make your moves by clicking on an empty cell, because the first player is the user by default.
4. The AI opponent will automatically make its moves.
5. The game will continue until there is a winner, a draw, or you choose to quit.

## End-of-Game Messages

- If you win: "Tu as gagné ! Veux-tu rejouer ?"
- If you lose: "Tu as perdu ! Veux-tu rejouer ?"
- If it's a draw: "Nul ! Veux-tu rejouer ?"

## Restarting or Quitting the Game

- After the game is over, a pop-up window will appear asking if you want to play again.
- Click "oui" to restart the game with the same symbol.
- Click "non" to quit the game.

## Scores

- The scores are displayed in the end-of-game message in the format "Score: Player - Computer."
- The scores are reset when you choose to quit the game
