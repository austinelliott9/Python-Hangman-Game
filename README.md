# 🎮 Python Hangman Game

A clean, terminal-based implementation of the classic Hangman game written in Python.  
Choose categories, guess letters, and avoid the noose—all while enjoying retro ASCII visuals!

---

## ✨ Features

- 🗂️ Multiple word categories via JSON configuration
- 🎨 ASCII art visuals for each incorrect guess
- ✅ Real-time input validation with user-friendly feedback
- 🔁 Play-again loop without restarting the script
- 🧪 Unit tested with `pytest`
- 🧱 Modular, readable codebase with docstrings and type hints
- 📦 Easily extensible with new categories or visuals

---

## 📂 Project Structure

```
Python Hangman Game/
│
├── hangman.py            # Main game logic
├── test_hangman.py       # Unit tests using pytest
├── categories.json       # Word categories grouped by theme
├── hangman_art.json      # ASCII art for visualizing the hangman
├── .gitignore            # Files excluded from Git tracking
├── .gitattributes        # Git configuration
└── README.md             # Project documentation
```

---

## 🚀 How to Run the Game

1. **Clone the repository**:
```bash
git clone https://github.com/austinelliott9/Python-Hangman-Game.git
cd Python-Hangman-Game
```

2. **Run the game**:
```bash
python hangman.py
```

---

## 🧪 Run the Tests

Make sure `pytest` is installed:
```bash
pip install pytest
```

Then run the tests:
```bash
pytest test_hangman.py
```

---

## ➕ Add Your Own Categories

To add a new category:
1. Open `categories.json`
2. Add a new key and list of words:
```json
"vehicles": ["car", "truck", "bicycle"]
```
3. Save and relaunch the game—no code edits needed!

---

## 🙌 Acknowledgements

Originally developed as the final project for [CS50's Introduction to Programming with Python (CS50P)](https://cs50.harvard.edu/python). This version was enhanced for GitHub presentation with cleaner code, documentation, and testing. For a video demonstration created for the course, please click [here](https://www.youtube.com/watch?v=2ek9Izr-ovE).

---

## 🪪 License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
