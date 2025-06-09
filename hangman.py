import random
import json
import os
from typing import List, Dict


def main() -> None:
    """
    Main loop for running the hangman game. Prompts user to play again after each round.
    """
    while True:
        play_game()
        play_again = input("Do you want to play again? (y/n): ")
        if play_again != "y":
            print("Thanks for playing!")
            break


def play_game() -> None:
    """
    Executes one full game of Hangman including word selection, user input, and win/loss logic.
    """
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

        if guess in word:
            update_word_status(word, guess, word_status)
        else:
            hangman_status += 1

        if "_" not in word_status:
            clear_screen()
            display_gamestate(hangman_status, word_status, used_guesses, hangman_art)
            print(f"Congratulations! You've uncovered the hidden word: {word}.")
            break

        if hangman_status == 6:
            clear_screen()
            display_gamestate(hangman_status, word_status, used_guesses, hangman_art)
            print(f"Oh no! You've run out of guesses. The word was {word}. Better luck next time!")
            break


def select_word() -> str:
    """
    Randomly selects a word from a chosen category.
    Returns:
        A formatted word (uppercase, no spaces or dashes).
    """
    with open("categories.json", "r") as file:
        categories = json.load(file)
        category = choose_category(categories)
        return (
            random.choice(categories[category])
            .upper()
            .replace(" ", "")
            .replace("-", "")
        )


def choose_category(categories: Dict[str, List[str]]) -> str:
    """
    Prompts the user to select a valid category.
    Args:
        categories: A dictionary of categories to word lists.
    Returns:
        A valid category selected by the user.
    """
    while True:
        category = (
            input(f"Choose category: {", ".join(categories.keys())}\n").strip().lower()
        )
        if category in categories:
            return category
        print("Invalid category, try again.")


def display_gamestate(hangman_status: int, word_status: List[str], used_guesses: List[str], hangman_art: List[str]) -> None:
    """
    Displays the current state of the game.
    Args:
        hangman_status: Number of incorrect guesses.
        word_status: Current guessed status of the word.
        used_guesses: List of guessed letters.
        hangman_art: List of hangman ASCII art strings.
    """
    print(hangman_art[hangman_status])
    print(" ".join(word_status))
    print(f"Used guesses: {', '.join(used_guesses)}")


def get_guess(used_guesses: List[str]) -> str:
    """
    Prompts the user for a single, valid, unused alphabetical guess.
    Args:
        used_guesses: List of guessed letters.
    Returns:
        A validated and capitalized guess.
    """
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
    """
    Updates the word status to reveal correctly guessed letters.
    Args:
        word: The target word.
        guess: The current guess.
        word_status: The current display of the word.
    """
    for i in range(len(word)):
        if word[i] == guess:
            word_status[i] = guess


def clear_screen() -> None:
    """
    Clears the console screen based on OS.
    """
    os.system('cls' if os.name == 'nt' else 'clear')


if __name__ == "__main__":
    main()
