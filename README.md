# Number Guessing Game — CLI

A simple terminal-based number guessing game. The computer picks a number, you guess it — with difficulty settings, a hint system, live timer, and high score tracking.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)

---

## 📋 Project

Part of the [Number Guessing Game](https://roadmap.sh/projects/number-guessing-game) challenge on **roadmap.sh**.

---

## 🎮 Features

| Feature | Status |
|---|---|
| Welcome screen + rules | ✅ |
| Random number 1–100 | ✅ |
| Difficulty: Easy / Medium / Hard | ✅ |
| Higher / Lower feedback | ✅ |
| Invalid-input protection | ✅ |
| Hint system (fires every 2 wrong guesses) | ✅ |
| Live elapsed timer | ✅ |
| Per-difficulty high scores | ✅ |
| Play multiple rounds | ✅ |
| Zero dependencies (stdlib only) | ✅ |

---

## 🚀 Installation

Python 3.8+ — no `pip install` needed.

```bash
git clone https://github.com/trippusultan/number-guessing-game.git
cd number-guessing-game
```

---

## 🛠 Usage

```bash
python3 guess.py
```

That's it. The game runs interactively in your terminal.

---

## 📖 How to Play

```
==============================================
  NUMBER GUESSING GAME
==============================================
  Rules:
  • Computer picks a number between 1 and 100.
  • Choose a difficulty to set your chances.
  • After each wrong guess you'll be told
    whether the number is HIGHER or LOWER.
  • Hints appear every 2 wrong guesses.
  • Beat the high score to claim the crown.
==============================================

==============================================
  Welcome to the Number Guessing Game!
  I'm thinking of a number between 1 and 100.

  Select difficulty:
    1. Easy (10 chances)
    2. Medium (5 chances)
    3. Hard (3 chances)
==============================================

Enter your choice (1-3):
```

---

## 🏆 High Scores

High scores are saved locally to `high_scores.json` in the same directory as the script. Tracked per difficulty:

- **Fewest attempts** to win
- **Fastest time**

After each round:

```
🏆  High Scores:
------------------------------------
  Easy     3 attempt(s)  in 2.1s  on 2025-05-15 13:30
  Medium   4 attempt(s)  in 3.8s  on 2025-05-15 13:31
  Hard     2 attempt(s)  in 1.2s  on 2025-05-15 13:32
------------------------------------
```

---

## 💡 Hint System

Every 2 wrong guesses you get an extra clue without losing a chance:

| Hint | Meaning |
|---|---|
| 🔥 So close! | Within 2 numbers |
| 🌡️ Warm! | Within 5 numbers |
| 🌤️ Mildly warm | Within 15 numbers |
| ❄️ Cold | More than 15 away |
| 🥶 Ice cold | Way off |

---

## 📁 Data Storage

| File | Purpose |
|---|---|
| `guess.py` | Game script |
| `high_scores.json` | Saved high scores (created automatically) |

---

## 🔗 Links

- [roadmap.sh Project](https://roadmap.sh/projects/number-guessing-game)
- [GitHub Repo](https://github.com/trippusultan/number-guessing-game)

---

## 📄 License

MIT
