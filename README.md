# Rock, Paper, Scissors Game

This is a simple command-line Rock, Paper, Scissors game where you can play against the computer. The game keeps track of the number of rounds played and maintains a leaderboard of the best players.

## Features

- Play Rock, Paper, Scissors against the computer.
- Track the number of rounds played.
- Maintain a leaderboard of the best players with the most wins.
- Save and load game statistics.

## Requirements

- Python 3.x

## How to Run

1. Clone the repository or download the `rock_paper_scissors.py` file.
2. Open a terminal and navigate to the directory containing the `rock_paper_scissors.py` file.
3. Run the script using the command:
   ```sh
   python rock_paper_scissors.py

## How to Play

Start the game by running the script.
You will be presented with a menu:

[N] Enter or change the player's name

[P] Play Rock, Paper, Scissors

[L] Print the list of best players

[Q] Quit the game

Follow the prompts to play the game and see the results.
The game will display the results of each round and update the leaderboard accordingly.

## Code Structure

- voittajanSelvitys(pelaajan_valinta, tietokoneen_valinta): Determines the winner between the player's and the computer's choices.
- pelaa(nimi, tilasto, laskuri): Manages the gameplay loop and updates the statistics.
- tietokoneenValinta(): Generates the computer's choice.
- tulostaParhaatPelaajatLista(tilasto): Prints the list of best players.
- lisaaVoitto(nimi, tilasto): Adds a win for the player.
- tallennaTilasto(tilasto): Saves the statistics to a file.
- lataaTilasto(): Loads the statistics from a file.
- annaNimi(): Prompts the player to enter a name.

## Saving and Loading Statistics

The game saves the statistics to a file named tilasto.txt.
If the file exists, the game loads the statistics when it starts.
The statistics include the number of rounds played and the number of wins for each player.

## Notes

The game interface and messages are in Finnish.
The game runs in a loop until you choose to quit by selecting [Q] from the menu.
