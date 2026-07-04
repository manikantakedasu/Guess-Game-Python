# ==========================================
# Guess The Number Game
# Main File
# Developed by: Manikanta
# Version 3.0
# ==========================================

from game import start_game
from scoreboard import get_high_score
from statistics import display_statistics
from history import HISTORY_FILE
import os


def show_title():
    print("=" * 60)
    print("🎮        GUESS THE NUMBER GAME        🎮")
    print("=" * 60)
    print("Welcome to the Professional Guess Game!")
    print("=" * 60)


def show_welcome_board(player_name):

    print("\n" + "=" * 60)
    print(f"        👋 WELCOME {player_name.upper()}!")
    print("=" * 60)

    print(f"\n🎯 Hello {player_name.title()}, are you ready?\n")

    print("🔢 Guess the hidden number.")
    print("🏆 Beat your highest score.")
    print("📊 Improve your win rate.")
    print("🎮 Have Fun & Good Luck!")

    print("\n" + "=" * 60)

    input("Press ENTER to continue...")


def get_player_name():

    while True:

        name = input("\n👤 Enter Your Name: ").strip()

        if name == "":
            print("❌ Name cannot be empty.")
        else:
            return name
        
     


def show_history():

    print("\n" + "=" * 60)
    print("📜 GAME HISTORY")
    print("=" * 60)

    if not os.path.exists(HISTORY_FILE):
       print("No history found.")
       return

    with open(HISTORY_FILE, "r") as file:

        data = file.read()

        if data.strip() == "":
            print("No history available.")
        else:
            print(data)

    print("=" * 60)

    input("\nPress ENTER to return to Main Menu...")


def show_high_score():

    print("\n" + "=" * 60)
    print("🏆 HIGH SCORE")
    print("=" * 60)
    print(f"🥇 Highest Score : {get_high_score()}")
    print("=" * 60)

    input("\nPress ENTER to return to Main Menu...")


def main_menu():

    print("\n" + "=" * 60)
    print("📋 MAIN MENU")
    print("=" * 60)
    print("1️⃣  Play Game")
    print("2️⃣  View Statistics")
    print("3️⃣  View High Score")
    print("4️⃣  View Game History")
    print("5️⃣  Exit")
    print("=" * 60)

    return input("Enter your choice : ").strip()


def main():

    show_title()

    player_name = get_player_name()

    show_welcome_board(player_name)

    while True:

        choice = main_menu()

        if choice == "1":

            start_game(player_name)

        elif choice == "2":

            display_statistics(get_high_score())

        elif choice == "3":

            show_high_score()

        elif choice == "4":

            show_history()

        elif choice == "5":

            print("\n" + "=" * 60)
            print(f"👋 Thank You For Playing, {player_name}!")
            print("❤️ Have a Great Day!")
            print("=" * 60)
            break

        else:

            print("\n❌ Invalid Choice! Please enter 1 to 5.")


if __name__ == "__main__":
    main()

  