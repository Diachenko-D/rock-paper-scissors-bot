import random

print("Hello! I am a Rock-Paper-Scissors bot! I have a few rules:")
print("1. We have three objects: Rock, Scissors, Paper")
print("2. You make your move, and I make mine and display the result (fair play guaranteed!)")
print('To display the score write to me - "score"')
print('To start a game write to me - "start game", to go back to the menu - "end game", and to end the whole program - "exit"')
print("Shall we start?")

# Score tracking
player_move_archive = []  # Player move history
last_result = None        # Result of previous round (relative to the bot)
round_num = 1             # Round number
all_games = []


def get_losing_move(move):  # Function returns the move that loses to player's last move
    if move == "rock":
        return "scissors"
    elif move == "scissors":
        return "paper"
    elif move == "paper":
        return "rock"


def get_winning_move(move):  # Function returns the move that beats player's last move
    if move == "rock":
        return "paper"
    elif move == "scissors":
        return "rock"
    elif move == "paper":
        return "scissors"


def strategy(player_move_archive, last_result, round_num):
    if round_num == 1:
        return "paper"
    # If the same move is repeated twice, the player will likely pick a move losing to the previous one
    if len(player_move_archive) >= 2:
        if player_move_archive[-1] == player_move_archive[-2]:
            return get_losing_move(player_move_archive[-1])

    last_player_move = player_move_archive[-1]
    # After a win repeat the player move, after a loss beat the player move
    if last_result == "lose":
        return last_player_move
    elif last_result == "win":
        return get_winning_move(last_player_move)
    else:  # On a draw output a random move
        return random.choice(["rock", "scissors", "paper"])


def stats(player_move_archive):  # Function determines the most used move and beats it
    if round_num == 1:
        return "paper"

    # Count how many times the player chose each symbol
    rock = player_move_archive.count("rock")
    scissors = player_move_archive.count("scissors")
    paper = player_move_archive.count("paper")

    # Find the most frequent move
    if rock >= scissors and rock >= paper:
        most_common = "rock"
    elif scissors >= paper:
        most_common = "scissors"
    else:
        most_common = "paper"
    # Return the move that beats the most frequent move
    return get_winning_move(most_common)


# Main program
while True:  # handle menu level inputs

    user_input = input("> ").strip().lower()

    if user_input == "exit":
        print(f"Bye!")
        exit()

    elif user_input == "score":
        if not all_games:
            print("No score yet, we haven't played together yet")
        else:
            print("\n Game history \n")
            for i, game in enumerate(all_games, 1):
                if game["strategy"] == "strategy":
                    strategy_name = "Behavioral"
                else:
                    strategy_name = "Statistical"
                if game["player_score"] > game["bot_score"]:
                    winner = "You"
                elif game["bot_score"] > game["player_score"]:
                    winner = "Bot"
                else:
                    winner = "Friendship won"
                print(f"Game {i}")
                print(f"Strategy - {strategy_name}")
                print(f"Score: {game['player_score']} : {game['bot_score']}")
                print(f"Winner: {winner}")
                print()

    elif user_input == "start game":

        # Let the player choose a strategy
        print("Select bot strategy:")
        print("1 — Behavioral (win/loss analysis)")
        print("2 — Statistical (move statistics)")
        strategy_choice = input("Your choice (1 or 2): ").strip()

        loc_player_score = 0  # Player score in this game
        loc_bot_score = 0     # Bot score in this game

        if strategy_choice == "1":
            current_strategy = "strategy"
        else:
            current_strategy = "stats"

        print("Make your move: rock, paper or scissors")

        # Create another loop for multi-round game
        while True:
            # Read player move
            move = input("Your move: ").strip().lower()

            if move == "end game":  # Output score of current game and exit to menu
                print(f"Game over! Final score for this game: You — {loc_player_score}, Bot — {loc_bot_score}")
                print("Exit to menu")
                # Determine winner of this game
                if loc_player_score > loc_bot_score:
                    winner = "player"
                elif loc_bot_score > loc_player_score:
                    winner = "bot"
                else:
                    winner = "draw"
                # Save this game
                all_games.append({
                    "strategy": current_strategy,
                    "player_score": loc_player_score,
                    "bot_score": loc_bot_score,
                    "winner": winner
                })
                break

            elif move == "score":  # If player enters score in move field, print score and return to input
                print(f"Current score: You — {loc_player_score}, Bot — {loc_bot_score}")
                continue

            elif move not in ["rock", "scissors", "paper"]:
                print("Invalid move! Try: rock, paper, scissors. Or try one of the commands: score, end game")
                continue

            # Bot makes a move
            if current_strategy == "stats":
                bot_move = stats(player_move_archive)
            else:
                bot_move = strategy(player_move_archive, last_result, round_num)
            print(f"My move: {bot_move}")

            # Determine winner and save round result
            if move == bot_move:
                print("Draw!")
                last_result = "draw"
            elif (move == "rock" and bot_move == "scissors") or \
                 (move == "scissors" and bot_move == "paper") or \
                 (move == "paper" and bot_move == "rock"):
                print("You won!")
                loc_player_score += 1
                last_result = "lose"
            else:
                print("Bot won!")
                loc_bot_score += 1
                last_result = "win"

            # Save player move and increase round counter
            player_move_archive.append(move)
            round_num += 1
