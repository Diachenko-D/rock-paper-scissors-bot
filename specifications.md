The terminal receives one of the following commands or moves as input:
Commands: start game, score, end game, exit
Moves: rock, paper, scissors

It is guaranteed that input is provided only in the terminal, as text, in English. Case and spaces are ignored for convenience ("Rock   " = "rock").
If the input content is not in the list of moves or commands, the program simply prompts for input again.

The game follows the basic rules of rock-paper-scissors and respects its opponent (moves are made using an algorithm, NOT by analyzing the player's current move!).

Ties are not counted in the score, only wins or losses. One win = one point to the score.

The bot allows the player to choose a strategy: behavioral or statistical. The behavioral strategy is based on general player analysis in advance; it is a predefined strategy described in the program. Below are its main key points:

To beat the opponent, use strategies:
After a win, play the same symbol the opponent used in the previous round; after a loss, play the symbol that beats the opponent's symbol in that round.
Also, if the opponent repeated the same gesture twice, they will likely change it on the third try, so it is better to pick the symbol that loses to the previous gesture.
Inexperienced players prefer rock. In the first round, we will try throwing paper, treating the first round as an analytical round.

The second strategy is statistical. The bot beats the figure most frequently chosen by the player (note: the first move, just like in the previous strategy, is always paper).

Features:
- Game sessions are saved only after the "end game" command.
- Move history accumulates across sessions; each game is numbered.
- The program does not terminate on input errors, but prompts to enter again.

The program works according to this algorithm:
Menu
Player input -> Start game
Enter game
Select strategy
Player move
Bot move and winner announcement
- when entering the "score" command, the current score is displayed
- when entering the "end game" command, return to the menu
Exit to menu
- when entering the "score" command, the game history and scores for all games are displayed
- when entering the "exit" command, code terminates
