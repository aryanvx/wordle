# Wordle (weird version written solely in Python)

This is my take on Wordle, but stripped down to basics — just a Python script you run in your terminal. Guess a five-letter word in six tries, get feedback on each letter, and see if you can crack the code before you run out of attempts.

## How to Play

1. Run the script
2. Enter the password to get started (anything alphanumeric because again, it was for my Python class, and this was one of the requirements)
3. Tell me your name
4. I’ll explain the rules — with some built-in pauses to build suspense
5. Start guessing five-letter words
6. After each guess, you’ll get feedback:
   - ✔ means the letter is correct and in the right spot
   - ➕ means the letter is in the word but in a different spot
   - ❌ means the letter isn’t in the word at all
7. You have six attempts, so use them wisely

## Features

- Random word chosen from a built-in list
- Input validation for word length and character type
- Clear feedback after every guess
- Password protection (because why not?)
- Basic error handling so the program doesn’t just crash on you

## How to Run

Just run the Python file in your terminal:

```
python wordle.py
```
