# Wordle in Python

This project is a Python-based implementation of the popular word-guessing game **Wordle**.
Players attempt to guess a secret five-letter word within a limited number of attempts.
After each guess, feedback is provided to indicate correct letters, misplaced letters, and incorrect letters.

I used the pandas library in this one so that I could learn data manipulation in python.

## Features

- **Customizable Word List**: Easily configure the list of words to use for the game.
- **Accurate Feedback**: 
	Feedback highlights 
	correct letters will be seen as the letter,
	misplaced letters will the show the symbol "+" plus,
	 and incorrect letters are show as the "x" symbol.
- **Command-Line Interface**: Play directly in the terminal.
- **Configurable Attempts**: Customize the number of allowed attempts.

### Example Gameplay

![image](https://github.com/user-attachments/assets/2b811c5a-c61b-4d94-b17c-103153646c0e)

## How to Play

1. Start the game by running the `wordle.py` script.
2. Guess the secret word by typing a five-letter word. Any non five letter word will just use a chance
 ![image](https://github.com/user-attachments/assets/5b458edd-96d5-4716-b1b5-70775f885ac0)

3. After each guess, you will recieve feedback:
	correct letters will be seen as the letter,
	misplaced letters will the show the symbol "+" plus,
	and incorrect letters are show as the "x" symbol.
4. You have a limited number of attempts (default is 6) to guess the correct word.

## Configuration

You can modify the following settings in the script:

- **Word List**: Add or update words in the `Word.xlsx` file.
- **Attempts**: Change the number of allowed attempts by editing the `atm` variable in `Wordle.py`.

## Contact

For questions or feedback, please reach out in my linkedin linkedin.com/in/velezjc
or visit vlzjc.github.io
