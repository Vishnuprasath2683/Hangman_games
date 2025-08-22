# Hangman Game (Python)

## 🎮 Introduction

This is a simple **Hangman game** implemented in Python. The player guesses letters to uncover a hidden word. Each incorrect guess reduces the number of lives and progressively draws the hangman. The game ends when the player either guesses the full word or runs out of lives.

---

## 📑 Table of Contents

1. [Installation](#installation)
2. [Usage](#usage)
3. [Features](#features)
4. [Project Structure](#project-structure)
5. [Dependencies](#dependencies)
6. [Configuration](#configuration)
7. [Examples](#examples)
8. [Troubleshooting](#troubleshooting)
9. [Contributors](#contributors)
10. [License](#license)

---

## ⚙️ Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/your-username/hangman-game.git
   cd hangman-game
   ```
2. Ensure you have **Python 3.6+** installed.
3. No external libraries are required.

---

## 🚀 Usage

Run the game from the terminal:

```bash
python main.py
```

* You will be prompted to guess letters.
* Correct guesses will reveal letters in the hidden word.
* Wrong guesses reduce your **lives** and update the hangman drawing.
* Win by guessing all letters, or lose when lives reach zero.

---

## 🌟 Features

* Classic **Hangman gameplay**.
* Randomly chosen words from a word list.
* ASCII art hangman that updates as you lose lives.
* Case-insensitive letter input.
* Simple, beginner-friendly code.

---

## 📂 Project Structure

```
.
├── main.py          # Main game logic
├── words_files.py   # List of possible words
├── stages_files.py  # ASCII art stages for the hangman
```

---

## 📦 Dependencies

* Python standard library (`random`).
* No third-party packages required.

---

## 🔧 Configuration

You can customize:

* **Word list** in `words_files.py`:

  ```python
  words = ["apple", "butterfly", "pineapple", "horse", "monkey", "aeroplane", "hello"]
  ```
* **Hangman drawings** in `stages_files.py`.

---

## 🖥️ Examples

Example gameplay:

```
Guess a letter: a
['_', 'a', '_', '_', 'a', '_']
Lives left: 5
 +---+
 |   |
 O   |
/|\  |
/    |
=========
```

---

## 🛠️ Troubleshooting

* **Game exits immediately**: Make sure you are running with Python 3, not Python 2.
* **No output after guess**: Ensure inputs are lowercase (the code forces `.lower()`).
* **Words too simple?** Add more entries to `words_files.py`.

---

## 👨‍💻 Contributors

* Vishnuprasath SK (@Vishnuprasath2683)

---

## 📜 License

This project is licensed under the **MIT License**.
Feel free to use, modify, and distribute it as you like.

---

