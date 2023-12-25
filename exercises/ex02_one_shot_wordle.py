"""EX02 - Wordle!"""
__author__ = "730645861"
# emojis
WHITE_BOX: str = "\U00002B1C"
YELLOW_BOX: str = "\U0001F7E8"
GREEN_BOX: str = "\U0001F7E9"
# variables for my program
v: int = 0
emoji: str = ""
secret_word: str = "python"
# user input
six_word: str = input("What is your 6-letter guess? ") 
# loop that checks if the user inputted the correct amount of characters for wordle
while len(six_word) != len(secret_word):
    six_word = input("That was not 6 letters! Try again:") 
# checks if the user got it right on the first try
if six_word == secret_word:
    print(GREEN_BOX + GREEN_BOX + GREEN_BOX + GREEN_BOX + GREEN_BOX + GREEN_BOX)
    print("Woo! You got it!")
# else statement that runs through the variables and uses booleans to compare them. Also adds value to the emoji string
else:
    while v < len(secret_word):
        if secret_word[v] == six_word[v]:
            emoji += GREEN_BOX
        else:
            if six_word[v] == secret_word[0] or six_word[v] == secret_word[1] or six_word[v] == secret_word[2] or six_word[v] == secret_word[3] or six_word[v] == secret_word[4] or six_word[v] == secret_word[5]:
                emoji += YELLOW_BOX
            else:
                if six_word[v] != secret_word[0] or six_word[v] != secret_word[1] or six_word[v] != secret_word[2] or six_word[v] != secret_word[3] or six_word[v] != secret_word[4] or six_word[v] == secret_word[5]:
                    emoji += WHITE_BOX
        v = v + 1
    print("Not Quite, play again soon!")
    # prints emoji and "loser" statement
    print(emoji)
