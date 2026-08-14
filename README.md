# Rock-Paper-Scissors Bot ✂️🪨📄

A CLI Python application that plays Rock-Paper-Scissors using adaptive strategies instead of simple random generation

---

## Algorithm Overview

The program allows players to select between two strategies before playing:

1. **Behavioral Strategy:** Analyzes human behavior patterns (e.g., win/loss responses, repetition switching, and opening round bias towards paper)
2. **Statistical Strategy:** Tracks move history and selects the counter-move against the player's most used symbol

---

## Navigation & Commands
* `start game` — Begins a game session and strategy selection
* `score` — Shows current match score during a game, or overall game history in the main menu
* `end game` — Ends the current game session, saves the history, and returns to the menu
* `exit` — Exits the application

---

## How to Run

### Prerequisites
* Python 3.x installed

### To Run
1. Clone or download this repository
2. Run the script

## Repository Structure
* **`main.py`**: Complete CLI game loop and AI strategy algorithms
* **`examples.txt`**: Detailed input/output execution walkthroughs
* **`README.md`**: Project documentation and overview
