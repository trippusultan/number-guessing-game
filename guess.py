#!/usr/bin/env python3
"""
Number Guessing Game — CLI
The computer picks a number between 1 and 100. You guess it.
"""

import sys
import json
import random
import time
import os
from datetime import datetime

HIGH_SCORES_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "high_scores.json")

DIFFICULTY = {
    "1": ("Easy", 10),
    "2": ("Medium", 5),
    "3": ("Hard", 3),
}

RANGE_MIN = 1
RANGE_MAX = 100


# ── high scores ───────────────────────────────────────────────────────────────

def load_scores() -> dict:
    if not os.path.exists(HIGH_SCORES_FILE):
        return {}
    with open(HIGH_SCORES_FILE, "r") as f:
        return json.load(f)


def save_scores(scores: dict) -> None:
    with open(HIGH_SCORES_FILE, "w") as f:
        json.dump(scores, f, indent=2)


def record_score(difficulty_key: str, attempts: int, elapsed: float) -> bool:
    scores = load_scores()
    key = difficulty_key
    if key not in scores or attempts < scores[key]["attempts"]:
        scores[key] = {
            "attempts": attempts,
            "elapsed": round(elapsed, 1),
            "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
        }
        save_scores(scores)
        return True
    return False


# ── hint system ───────────────────────────────────────────────────────────────

def give_hint(secret: int, guess: int) -> str:
    """Return a hint based on how far off the guess is."""
    diff = abs(secret - guess)
    if diff <= 2:
        return "🔥 So close! You're within 2."
    if diff <= 5:
        return "🌡️  Warm! Within 5."
    if diff <= 15:
        return "🌤️  Mildly warm. Within 15."
    if diff <= 30:
        return "❄️  Cold. More than 15 away."
    return "🥶 Ice cold. Way off."


# ── game loop ─────────────────────────────────────────────────────────────────

def play_round() -> None:
    secret = random.randint(RANGE_MIN, RANGE_MAX)
    attempts = 0
    start_time = time.time()

    # Difficulty
    print("=" * 46)
    print("  Welcome to the Number Guessing Game!")
    print(f"  I'm thinking of a number between {RANGE_MIN} and {RANGE_MAX}.")
    print("\n  Select difficulty:")
    for key, (name, chances) in DIFFICULTY.items():
        print(f"    {key}. {name} ({chances} chances)")
    print("=" * 46)

    while True:
        choice = input("\nEnter your choice (1-3): ").strip()
        if choice in DIFFICULTY:
            break
        print("Invalid choice. Enter 1, 2, or 3.")

    diff_name, max_chances = DIFFICULTY[choice]
    print(f"\nGreat! {diff_name} — {max_chances} chances.")
    print("Let's start the game!\n")

    remaining = max_chances
    while remaining > 0:
        try:
            raw = input(f"Enter your guess ({RANGE_MIN}-{RANGE_MAX}) [{remaining} left]: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\n\nGoodbye!")
            sys.exit(0)
        attempts += 1
        remaining -= 1

        # Validate input
        if not raw.isdigit():
            print("Please enter a valid number.")
            attempts -= 1
            remaining += 1
            continue

        guess = int(raw)
        if guess < RANGE_MIN or guess > RANGE_MAX:
            print(f"Number must be between {RANGE_MIN} and {RANGE_MAX}.")
            attempts -= 1
            remaining += 1
            continue

        if guess == secret:
            elapsed = time.time() - start_time
            new_record = record_score(choice, attempts, elapsed)
            print(f"\n🎉  Congratulations! You guessed it in {attempts} attempt{'s' if attempts != 1 else ''}.")
            print(f"⏱  Time: {elapsed:.1f}s")
            if new_record:
                print(f"🏆  New high score for {diff_name}!")
            elif load_scores().get(choice, {}).get("attempts"):
                prev = load_scores()[choice]["attempts"]
                print(f"   Best: {prev} attempt{'s' if prev != 1 else ''} on {diff_name}.")
            return

        direction = "less" if guess > secret else "greater"
        print(f"Incorrect! The number is {direction} than {guess}.")
        # Hint every 2 wrong guesses
        if attempts % 2 == 0 and remaining > 0:
            print(give_hint(secret, guess))

    # Ran out of chances
    elapsed = time.time() - start_time
    print(f"\n💀  Game over! You ran out of chances.")
    print(f"   The number was {secret}.")
    print(f"   ⏱  Time: {elapsed:.1f}s")


def show_high_scores() -> None:
    scores = load_scores()
    if not scores:
        print("\nNo scores yet. Play first!")
        return
    print("\n🏆  High Scores:")
    print("-" * 36)
    for key in sorted(scores, key=lambda k: int(k)):
        diff_name, _ = DIFFICULTY[key]
        s = scores[key]
        print(f"  {diff_name:<8} {s['attempts']} attempt(s)  in {s['elapsed']}s  on {s['date']}")
    print("-" * 36)


def main() -> None:
    print("\n" + "=" * 46)
    print("  NUMBER GUESSING GAME")
    print("=" * 46)
    print("  Rules:")
    print("  • Computer picks a number between 1 and 100.")
    print("  • Choose a difficulty to set your chances.")
    print("  • After each wrong guess you'll be told")
    print("    whether the number is HIGHER or LOWER.")
    print("  • Hints appear every 2 wrong guesses.")
    print("  • Beat the high score to claim the crown.")
    print("=" * 46)

    while True:
        play_round()
        show_high_scores()
        again = input("\nPlay again? (y/n): ").strip().lower()
        if again not in ("y", "yes"):
            print("\nThanks for playing!\n")
            break


if __name__ == "__main__":
    main()
