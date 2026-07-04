# ==========================================
# Guess The Number Game
# Game Logic
# ==========================================

import random
import time
from scoreboard import get_high_score, save_high_score
from history import save_history
from colorama import Fore, Style, init
from statistics import update_statistics, display_statistics
def choose_difficulty():
    init(autoreset=True)

    while True:

        print("\n" + "=" * 50)
        print("        SELECT DIFFICULTY")
        print("=" * 50)
        print("1. Easy   (1 - 10)   ❤️❤️❤️❤️❤️")
        print("2. Medium (1 - 50)   ❤️❤️❤️❤️")
        print("3. Hard   (1 - 100)  ❤️❤️❤️")
        print("0. Back to Main Menu")
        print("=" * 50)

        choice = input("Enter your choice : ")
        if choice == "0":
         return None

        if choice == "1":
            return 1, 10, 5, "Easy"

        elif choice == "2":
            return 1, 50, 4, "Medium"

        elif choice == "3":
            return 1, 100, 3, "Hard"

        else:
            print("❌ Invalid Choice! Try Again.")


def show_lives(lives):
    print("\n❤️ Lives :", "❤️ " * lives)


def start_game(player_name):

    difficulty_data = choose_difficulty()

    if difficulty_data is None:
     return
    lower, upper, lives, difficulty = difficulty_data

    secret_number = random.randint(lower, upper)

    print(Fore.CYAN + "\n⏳ Get Ready...")

    for i in range(3, 0, -1):
        print(Fore.YELLOW + f"{i}...")
        time.sleep(1)

    print(Fore.GREEN + "🚀 GO!!!\n")
    time.sleep(0.5)

    attempts = 0

    start_time = time.time()

    print("\n" + "=" * 60)
    print("🎮 GAME STARTED")
    print("=" * 60)
    print(f"👤 Player      : {player_name}")
    print(f"🎯 Difficulty : {difficulty}")
    print(f"🔢 Guess a number between {lower} and {upper}")
    print("=" * 60)
    print(f"🏆 Current High Score : {get_high_score()}")

    while lives > 0:

        show_lives(lives)

        try:
            guess = int(input("\n👉 Enter your guess : "))

        except ValueError:
            print("❌ Please enter numbers only.")
            continue

        attempts += 1

        # -------------------------
        # WIN CONDITION
        # -------------------------

        if guess == secret_number:

            end_time = time.time()

            time_taken = round(end_time - start_time, 2)

            score = (lives * 20) - (attempts * 2)

            if score < 10:
                score = 10

            if score >= 50:
                rank = "🥇 Gold"

            elif score >= 30:
                rank = "🥈 Silver"

            else:
                rank = "🥉 Bronze"

            print(Fore.GREEN + "\n🎉 Congratulations!")
            print("✅ Correct Guess!")

            print("\n========== GAME SUMMARY ==========")
            print(f"👤 Player          : {player_name}")
            print(f"🎯 Difficulty      : {difficulty}")
            print(f"🔢 Correct Number  : {secret_number}")
            print(f"📊 Attempts Used   : {attempts}")
            print(f"❤️ Lives Left      : {lives}")
            print(f"⏱️ Time Taken      : {time_taken} seconds")
            print(f"🏆 Score           : {score}")
            print(f"🏅 Rank            : {rank}")
            print("🎊 Result          : WIN")
            print("==================================")
            if save_high_score(score):
                print(Fore.CYAN + "\n🎉 NEW HIGH SCORE!")
            save_history(
                player_name,
                difficulty,
                score,
                "WIN"
            )

            update_statistics("WIN")
            display_statistics(get_high_score())

            return score
        
        
        
         # -------------------------
        # TOO LOW
        # -------------------------
        elif guess < secret_number:

            print(Fore.YELLOW + "\n📉 Too Low!")

            difference = secret_number - guess

            if difference > 30:
                print("💡 Hint : Try a MUCH bigger number.")
            elif difference > 15:
                print("💡 Hint : Try a bigger number.")
            elif difference > 5:
                print("💡 Hint : You're getting close!")
            else:
                print("🔥 Hint : Very Close!")

        # -------------------------
        # TOO HIGH
        # -------------------------
        else:

            print(Fore.BLUE + "\n📈 Too High!")

            difference = guess - secret_number

            if difference > 30:
                print("💡 Hint : Try a MUCH smaller number.")
            elif difference > 15:
                print("💡 Hint : Try a smaller number.")
            elif difference > 5:
                print("💡 Hint : You're getting close!")
            else:
                print("🔥 Hint : Very Close!")

        lives -= 1

    # -------------------------
    # GAME OVER
    # -------------------------

    end_time = time.time()
    time_taken = round(end_time - start_time, 2)

    print(Fore.RED + "\n💀 GAME OVER!")
    print(f"😢 The correct number was : {secret_number}")

    rank = "🥉 Bronze"

    print("\n========== GAME SUMMARY ==========")
    print(f"👤 Player          : {player_name}")
    print(f"🎯 Difficulty      : {difficulty}")
    print(f"🔢 Correct Number  : {secret_number}")
    print(f"📊 Attempts Used   : {attempts}")
    print(f"❤️ Lives Left      : {lives}")
    print(f"⏱️ Time Taken      : {time_taken} seconds")
    print("🏆 Score           : 0")
    print(f"🏅 Rank            : {rank}")
    print("❌ Result          : LOSE")
    print("==================================")

    print("\n❤️ Better Luck Next Time!")
    save_history(
        player_name,
        difficulty,
        0,
        "LOSE"
    )

    update_statistics("LOSE")
    display_statistics(get_high_score())

    return 0
