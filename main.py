# importing the 3 modules: random, time, and sys.
import random, time, sys

# put all of the code into a try block.
try:
    
    # making a dictionary with all the words.
    words = {
    1: "black",
    2: "bread",
    3: "queen",
    4: "dairy",
    5: "creed",
    6: "panda",
    7: "horse",
    8: "break",
    9: "breed",
    10: "about",
    11: "alert",
    12: "chain",
    13: "chair",
    14: "bring",
    15: "brief",
    16: "chase",
    17: "chart",
    18: "curve",
    19: "cycle",
    20: "beach",
    21: "crowd",
    22: "final",
    23: "first",
    24: "eight",
    25: "elite",
    26: "floor",
    27: "flash",
    28: "drill",
    29: "earth",
    30: "dying",
    31: "globe",
    32: "glass",
    33: "issue",
    34: "grant",
    35: "index",
    36: "logic",
    37: "loose",
    38: "lower",
    39: "lucky",
    40: "lunch",
    41: "lying",
    43: "sheet",
    44: "pound",
    45: "spare",
    46: "there",
    47: "smart",
    48: "truth",
    49: "state",
    50: "worry",
    51: "worst",
    52: "visit",
    53: "vital",
    54: "youth",
    55: "yield",
    56: "urban",
    57: "throw",
    58: "mixed",
    59: "north",
    60: "river",
    61: "adopt",
    62: "ideal",
    63: "bosom",
    64: "waive",
    65: "choir",
    66: "pudgy",
    67: "stood",
    68: "spoke",
    69: "outgo",
    70: "delay",
    71: "bilge",
    72: "sieve",
    73: "noose",
    74: "grape",
    75: "shied",
    76: "drawl",
    77: "daisy",
    78: "strut",
    79: "clasp",
    80: "block",
    81: "laugh",
    82: "hardy",
    83: "burnt",
    84: "crick",
    85: "vixen",
    86: "furor",
    87: "geeky",
    88: "cough",
    89: "naive",
    90: "meant",
    91: "stork",
    92: "prime",
    93: "outer",
    94: "idyll",
    95: "elect",
    96: "razor",
    97: "swear",
    98: "crump",
    99: "dough",
    100: "kings",
    101: "abide",
    102: "acorn",
    103: "adore",
    104: "agile",
    105: "ample",
    106: "angel",
    107: "apple",
    108: "argue",
    109: "asset",
    110: "audio",
    111: "avoid",
    112: "awake",
    113: "bacon",
    114: "badge",
    115: "baker",
    116: "baldy",
    117: "balsa",
    118: "banjo",
    119: "barge",
    120: "basil",
    121: "bathe",
    122: "beard",
    123: "beast",
    124: "beefy",
    125: "began",
    126: "being",
    127: "belly",
    128: "berry",
    129: "bible",
    130: "biker",
    131: "bison",
    132: "blame",
    133: "blaze",
    134: "bleak",
    135: "blend",
    136: "bless",
    137: "blimp",
    138: "blink",
    139: "bliss",
    140: "block",
    141: "blond",
    142: "blood",
    143: "bloom",
    144: "blown",
    145: "blues",
    146: "blunt",
    147: "board",
    148: "boast",
    149: "bogus",
    150: "booth",
}

    # choosing a random word from the dictionary.
    answer = random.choice(words)

    # making the password.
    password = input("Enter the password: ")
    
    # if statement if password is correct.
    if password.isalnum():
        
        # asking user for name.
        playerName = input("To whom am I addressing? ")
        
        # making name look nice.
        playerName = playerName.title()
                
        def instructions(name):
            '''
            Summary:
                The instructions() function prints a series of messages with built-in delays to provide an introduction
                and guide for playing the game Wordle.

            Args:
                Name.

            Returns:
                Returns the function instructions (simply just print statements), formatted with name, and introduces
                the idea of a progress guide to help with the objective of the game.
            '''
            
            # time.sleep's are building suspense.
            print(f"Welcome to wordle {name}.\n")
            time.sleep(2.5)

            print("Wordle is a single player game.\n")
            time.sleep(2.5)

            print("You have to guess a five-letter word.\n")
            time.sleep(2.5)

            print("You have six attempts.\n")
            time.sleep(2.5)

            print("Your progress guide:\n")
            time.sleep(1)

            print("      ✔ indicates that the letter at that position was guessed correctly.")
            time.sleep(2.25)

            print("      ➕ indicates that the letter at that position is in the answer but in a different position.")
            time.sleep(2.25)

            print("      ❌ indicates that the letter at that position is wrong and isn't in the answer.\n")
            time.sleep(2.25)
            
        # calling the function.
        instructions(playerName)
        
        def checkWord():
            '''
            Summary:
                The checkWord() function is a Python function that allows a player to guess a word within a certain
                number of attempts, providing feedback on the correctness of the guess and ending the game when the
                player runs out of attempts or guesses the word correctly.

            Args:
                N/A

            Returns:
                Returns the word with the feedback (ex: if "horse" is guessed and the correct word is "house", the "h",
                "o", "s", and "e" will show up as correct and "u" will be marked incorrect).
            '''
            
            # using an attempt integer for the Wordle.
            attempt = 6

            # creating a while loop as long as the player has attempts remaining.
            while attempt > 0:
                
                # player's guess
                guess = str(input("Guess the word: "))

                # only run if guess is alphanumeric.
                if guess.isalpha():
                    
                    # what happens when guess is longer than 5 characters.
                    if len(guess) > 5:
                        print(f"""
                        Guess was too long, please remember the guess must be 5 characters long.
                        Your guess was {len(guess)} character(s) long.
                            """)

                    # what happens when guess is shorter than 5 characters.
                    elif len(guess) < 5:
                        print(f"""
                        Guess was too short, please remember the guess must be 5 characters long.
                        Your guess was {len(guess)} character(s) long.
                            """)

                    # will only run if guess is 5 characters long.
                    elif len(guess) == 5:
                        
                        # if guess is the same as the answer.
                        if guess == answer:
                            
                            # print statement for answer matching guess.
                            print(f"You guessed the word correctly! Congratulations {playerName}!")
                            
                            # breaks out of the loop when word is guessed correctly.
                            break

                        # else statement if user has not guessed the answer.
                        else:
                            
                            # attempt decreases by 1 every time the loop occurs.
                            attempt -= 1
                            
                            # prints how many attempts the player has left.
                            print(f"You have {attempt} attempt(s) left")

                            # for loop that takes the iterator of tuples with the zip method made by answer and guess.
                            # word will hold an element from answer sequence.
                            # letter will hold an element from the guess sequence.
                            for i in range(len(answer)):
                                
                                # sets the word to the iteration number of answer
                                word = answer[i]
                                
                                # sets the letter to the iteration number of guess
                                letter = guess[i]
                                
                                # if letters guess in answer are in answer AND if the letters guessed are in the word
                                # the letter and the "✔" will be printed.
                                if letter in answer and letter in word:
                                    print(f"{letter} ✔")

                                # if the letters are in the answer but aren't in the correct position, print the letter
                                # and "➕" next to it.
                                elif letter in answer:
                                    print(f"{letter} ➕")

                                # if both conditions above evaluate as false, just print an "❌".
                                else:
                                    print(f"{letter} ❌")
                                    
                            

                            # when the amount of attempts the player runs out, the game ends.
                            if attempt == False:
                                print(f"Better luck next time {playerName}! The word was", answer)
                                break
                            

                # else statement for when the guess is not alphabetical.
                else:
                    print("Guess must be alphabetical. Try again.")

        # calling the function where the word is checked for letters.
        checkWord()
    
    # else statement if password is incorrect.
    else:
        print("Please enter a correct password.")
        sys.exit()

# except block for NameErrors.
except NameError:
    print("Object has not been defined.")

# except block for TypeErrors.
except TypeError:
    print("Operation cannot be performed on data type.")
    
# except block for SyntaxErrors.
except SyntaxError:
    print("Please check over all syntax.")
    
# except block for all other general exceptions.
except:
    print("An error occured. Please try again.")
