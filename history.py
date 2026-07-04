# ==========================================
# Game History
# ==========================================

import os

APP_FOLDER = os.path.join(os.getenv("LOCALAPPDATA"), "GuessTheNumber")
os.makedirs(APP_FOLDER, exist_ok=True)

HISTORY_FILE = os.path.join(APP_FOLDER, "game_history.txt")


def save_history(player, difficulty, score, result):

    with open(HISTORY_FILE, "a") as file:

        file.write("=" * 40 + "\n")
        file.write(f"Player      : {player}\n")
        file.write(f"Difficulty  : {difficulty}\n")
        file.write(f"Score       : {score}\n")
        file.write(f"Result      : {result}\n")
        file.write("=" * 40 + "\n\n")
       