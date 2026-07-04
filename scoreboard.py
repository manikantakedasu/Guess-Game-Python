# ==========================================
# Scoreboard Module
# ==========================================

HIGH_SCORE_FILE = "highscore.txt"


def get_high_score():

    try:
        with open(HIGH_SCORE_FILE, "r") as file:
            return int(file.read())

    except:
        return 0


def save_high_score(score):

    high_score = get_high_score()

    if score > high_score:

        with open(HIGH_SCORE_FILE, "w") as file:
            file.write(str(score))

        return True

    return False