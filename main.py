import random

print("Hello! I am a Rock-Paper-Scissors bot. Here are a few rules:")
print("1. We have three choices: rock, paper, or scissors.")
print("2. You make your move, then I make mine and display the result (fair play guaranteed!).")
print('To view your current score during a match, type: "score".')
print('To start a game, type "start game". To return to the main menu, type "end game". To exit the application, type "exit".')
print("Ready to play?\n")

# History & Session Tracking
player_move_archive = []  # History of player moves across rounds
last_result = None        # Outcome of previous round relative to the bot ('win', 'lose', 'draw')
round_num = 1             # Counter for rounds in the current session
all_games = []            # Archive of completed game sessions


def get_losing_move(move):
    """Returns the move that loses to the player's last move."""
    if move == "rock":
        return "scissors"
    elif move == "scissors":
        return "paper"
    elif move == "paper":
        return "rock"


def get_winning_move(move):
    """Returns the move that beats the player's last move."""
    if move == "rock":
        return "paper"
    elif move == "scissors":
        return "rock"
    elif move == "paper":
        return "scissors"


def behavioral_strategy(player_move_archive, last_result, round_num):
    """Predicts next move using human psychological tendencies."""
    if round_num == 1:
        return "paper"  # First round default analyzer move

    # If the player repeats a move twice, they often switch to a counter move
    if len(player_move_archive) >= 2:
        if player_move_archive[-1] == player_move_archive[-2]:
            return get_losing_move(player_move_archive[-1])

    last_player_move = player_move_archive[-1]
    
    # After a loss, mirror the player's previous move. After a win, counter it.
    if last_result == "lose":
        return last_player_move
    elif last_result == "win":
        return get_winning_move(last_player_move)
    else:
        return random.choice(["rock", "paper", "scissors"])


def statistical_strategy(player_move_archive, round_num):
    """Calculates the most frequent player move and plays its counter."""
    if round_num == 1:
        return "paper"

    rock_count = player_move_archive.count("rock")
    scissors_count = player_move_archive.count("scissors")
    paper_count = player_move_archive.count("paper")

    # Determine most frequent selection
    if rock_count >= scissors_count and rock_count >= paper_count:
        most_common = "rock"
    elif scissors_count >= paper_count:
        most_common = "scissors"
    else:
        most_common = "paper"

    return get_winning_move(most_common)


# Main Application Loop
while True:
    user_input = input("> ").strip().lower()

    if user_input == "exit":
        print("Goodbye!")
        exit()

    elif user_input == "score":
        if not all_games:
            print("No saved game history yet. Play a match first!")
        else:
            print("\n--- Game History ---")
            for i, game in enumerate(all_games, 1):
                strategy_name = "Behavioral" if game["strategy"] == "behavioral" else "Statistical"
                
                if game["player_score"] > game["bot_score"]:
                    winner = "Player"
                elif game["bot_score"] > game["player_score"]:
                    winner = "Bot"
                else:
                    winner = "Tie"

                print(f"Game {i}")
                print(f"Strategy: {strategy_name}")
                print(f"Score: You {game['player_score']} : {game['bot_score']} Bot")
                print(f"Winner: {winner}\n")

    elif user_input == "start game":
        print("Select bot strategy:")
        print("1 — Behavioral (Psychological Win/Loss Analysis)")
        print("2 — Statistical (Frequency Analysis)")
        strategy_choice = input("Your choice (1 or 2): ").strip()

        loc_player_score = 0
        loc_bot_score = 0

        current_strategy = "behavioral" if strategy_choice == "1" else "statistical"

        print("Make your move: rock, paper, or scissors")

        # Game Session Loop
        while True:
            move = input("Your move: ").strip().lower()

            if move == "end game":
                print(f"Game Over! Final Score: You — {loc_player_score}, Bot — {loc_bot_score}")
                print("Returning to main menu...")

                if loc_player_score > loc_bot_score:
                    winner = "player"
                elif loc_bot_score > loc_player_score:
                    winner = "bot"
                else:
                    winner = "draw"

                all_games.append({
                    "strategy": current_strategy,
                    "player_score": loc_player_score,
                    "bot_score": loc_bot_score,
                    "winner": winner
                })
                break

            elif move == "score":
                print(f"Current Score: You — {loc_player_score}, Bot — {loc_bot_score}")
                continue

            elif move not in ["rock", "paper", "scissors"]:
                print("Invalid input! Please choose: rock, paper, or scissors. Or enter commands: score, end game")
                continue

            # Bot Move Selection
            if current_strategy == "statistical":
                bot_move = statistical_strategy(player_move_archive, round_num)
            else:
                bot_move = behavioral_strategy(player_move_archive, last_result, round_num)

            print(f"My move: {bot_move}")

            # Evaluate Winner
            if move == bot_move:
                print("It's a tie!")
                last_result = "draw"
            elif (move == "rock" and bot_move == "scissors") or \
                 (move == "scissors" and bot_move == "paper") or \
                 (move == "paper" and bot_move == "rock"):
                print("You won this round!")
                loc_player_score += 1
                last_result = "lose"  # Bot perspective: bot lost
            else:
                print("Bot won this round!")
                loc_bot_score += 1
                last_result = "win"   # Bot perspective: bot won

            player_move_archive.append(move)
            round_num += 1
