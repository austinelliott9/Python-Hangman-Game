# Hangman
### Video Demo: https://youtu.be/2ek9Izr-ovE
### Description:
I decided to go with a simple hangman game for my final project. As demonstrated in the video, the program starts by listing the available categories and asks the user to choose one. If the entered category does not match any of those available, it asks the user to try again. Once a valid category is chosen, ASCII art of the empty gallows is printed, along with the number of blanks ( _ ) that corresponds to the number of letters in the word to be guessed. Used guesses appear below that and the user is prompted to make a guess. Only a single, alphabetic character will be accepted as a valid guess – unique feedback will appear for invalid character types, invalid number of characters, and already-used guesses. Correct guesses result in all instances of that letter being revealed in place of the blanks. Incorrect guesses result in the next body part of the hangman to be printed (head -> body -> left arm -> right arm -> left leg -> right leg). The game ends when either all blank letters are guessed correctly or when the right leg gets drawn. The user is then asked if they want to play again (“y” repeats the program, “n” ends it).

I initially kept the ASCII art and the categories in the main project.py file but eventually decided to declutter and moved them to their own json files. This also made it a little easier to add new categories, as you just need to open the categories.json and structure one in the same way the others are written. I considered adding a feature to the main program in which “add category” is an option at launch and the user is prompted for a category name + words in the category. I did not get around to it, but it would theoretically be easy because of the json structure.

A few aspects of the program that I would like to highlight:

Lose condition: The integer hangman_status starts at 0 and increments every time an incorrect guess is made. This let me use it to select the correct ASCII art from an array of art for the current gamestate, as well as determine when the game has been lost (if it =6)

Win condition: Since winning the game means that all of the blanks have been filled, I simply decided to check whether “_” is in the word_status after every guess is made. If it isn’t, that means the winning text can be displayed.

Console clearing: While testing, I was getting annoyed with the clutter even while playing the game. One of the last things I added was the automatic clearing of the console after making every guess. Since the command for that differs by operating system, I first check if the program is being run on Windows and use the “cls” command if so. If not, it is likely Mac/Linux/Unix, which all use the “clear” command.
