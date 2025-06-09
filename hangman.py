import random
import json
import os
from typing import List, Dict


def main() -> None:
    while True:
        play_game()
        play_again = input("Do you want to play again? (y/n): ")
        if play_again != "y":
            print("Thanks for playing!")
            break


def play_game() -> None:
    word = select_word()
    word_status = ["_"] * len(word)
    used_guesses = []
    hangman_status = 0
    with open("hangman_art.json", "r") as file:
        hangman_art = json.load(file)

    while True:
        clear_screen()
        display_gamestate(hangman_status, word_status, used_guesses, hangman_art)
        guess = get_guess(used_guesses)
        used_guesses.append(guess)

        if guess in word:  # A correct guess
            update_word_status(word, guess, word_status)
        else:  # An incorrect guess
            hangman_status += 1

        if "_" not in word_status:  # Win conditions
            clear_screen()
            display_gamestate(hangman_status, word_status, used_guesses, hangman_art)
            print(f"Congratulations! You've uncovered the hidden word: {word}.")
            break

        if hangman_status == 6:  # Lose conditions
            clear_screen()
            display_gamestate(hangman_status, word_status, used_guesses, hangman_art)
            print(
                f"Oh no! You've run out of guesses. The word was {word}. Better luck next time!"
            )
            break


def select_word() -> str:
    with open("categories.json", "r") as file:
        categories = json.load(file)
        category = choose_category(categories)
        return (
            random.choice(categories[category])
            .upper()
            .replace(" ", "")
            .replace("-", "")
        )  # ensure chosen word is formatted correctly


def choose_category(categories: Dict[str, List[str]]) -> str:
    while True:
        category = (
            input(f"Choose category: {", ".join(categories.keys())}\n").strip().lower()
        )
        if category in categories:
            return category
        print("Invalid category, try again.")


def display_gamestate(hangman_status: int, word_status: List[str], used_guesses: List[str], hangman_art: List[str]) -> None:
    print(hangman_art[hangman_status])
    print(" ".join(word_status))
    print(f"Used guesses: {', '.join(used_guesses)}")


def get_guess(used_guesses: List[str]) -> str:
    while True:
        guess = input("Guess: ").upper()
        if not guess.isalpha():
            print("\nPlease enter only alphabetic characters.")
        elif len(guess) != 1:
            print("\nPlease enter only one letter at a time.")
        elif guess in used_guesses:
            print("\nLetter already guessed, try again.")
        else:
            return guess


def update_word_status(word: str, guess: str, word_status: List[str]) -> None:
    for i in range(len(word)):
        if word[i] == guess:
            word_status[i] = guess


def clear_screen() -> None:
    os.system('cls' if os.name == 'nt' else 'clear') # If on Windows, uses cls command to clear terminal. Otherwise, uses clear (Mac/Linux/Unix)


if __name__ == "__main__":
    main()
