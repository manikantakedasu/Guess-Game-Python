# ==========================================
# Guess The Number Game
# Statistics Module
# ==========================================

import os

APP_FOLDER = os.path.join(os.getenv("LOCALAPPDATA"), "GuessTheNumber")
os.makedirs(APP_FOLDER, exist_ok=True)

STATISTICS_FILE = os.path.join(APP_FOLDER, "statistics.txt")



def get_statistics():

    try:
        with open(STATISTICS_FILE, "r") as file:

            data = file.readlines()

            games = int(data[0].strip())
            wins = int(data[1].strip())
            losses = int(data[2].strip())

            return games, wins, losses

    except:

        with open(STATISTICS_FILE, "w") as file:
            file.write("0\n")
            file.write("0\n")
            file.write("0\n")

        return 0, 0, 0


def update_statistics(result):

    games, wins, losses = get_statistics()

    games += 1

    if result == "WIN":
        wins += 1
    else:
        losses += 1

    with open(STATISTICS_FILE, "w") as file:
        file.write(f"{games}\n")
        file.write(f"{wins}\n")
        file.write(f"{losses}\n")


def display_statistics(high_score):

    games, wins, losses = get_statistics()

    if games == 0:
        win_rate = 0
    else:
        win_rate = round((wins / games) * 100, 2)

    print("\n" + "=" * 42)
    print("📊 PLAYER STATISTICS")
    print("=" * 42)
    print(f"🎮 Games Played : {games}")
    print(f"🏆 Wins         : {wins}")
    print(f"❌ Losses       : {losses}")
    print(f"📈 Win Rate     : {win_rate}%")
    print(f"🥇 High Score   : {high_score}")
    print("=" * 42)
    input("\nPress ENTER to return to Main Menu...")