# Tic Tac Toe AI (Python)

This project is a Tic Tac Toe game with an AI opponent implemented using the Minimax algorithm. The game allows a human player to compete against a computer AI, which always makes the optimal move i.e.  AI plays optimally, meaning it never loses — it will always win or draw against the human player.
##### Note:  The graphical interface and game framework were provided by CS50 staff. I implemented only the core game logic in tictactoe.py, including the AI decision-making and game rules.

## What I Implemented

In the provided CS50 framework, I implemented the core game logic inside tictactoe.py:

* player: Determines whose turn it is.

* actions: Returns all valid moves for the current state.

* result: Returns the new board state after a move.

* winner: Checks if a player has won.

* terminal: Determines if the game is over.

* utility: Assigns a numerical value to terminal states.

* minimax: Computes the optimal move for the current player using the Minimax algorithm.

These functions form the decision-making core of the AI, allowing it to play optimally.

## What Was Provided

The following parts were given by the CS50 staff:

* runner.py: Handles the graphical interface, user input, and game loop using Pygame.

* OpenSans-Regular.ttf: Font file for rendering text in the GUI.

* requirements.txt: Dependencies for running the project.

#### This framework allowed me to focus solely on implementing the AI logic.

## Features

* Human vs AI gameplay

* AI plays optimally using Minimax

* Pygame GUI with clickable interface

* Game reset and replay functionality

## How to Run

* Install dependencies from requirements.txt:

  * pip install -r requirements.txt


* Run the game:

  * python runner.py


Choose your player (X or O) and start playing.
