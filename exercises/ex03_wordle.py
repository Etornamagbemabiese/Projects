"""EX03 - Wordle!"""
__author__ = "730645861"


def contains_char(secretWord: str, userInput: str) -> bool:
    """This function takes a users guess and checks if it matches any of my secretword indexes."""
    assert len(userInput) == 1
    # makes sure that the length of guess is 1
    i: int = len(secretWord) - 1
    t: int = 0
    f: int = 1
    # variable intializers
    while i >= 0:
        # while loops that checks if the guess is equal to any part of the secret
        if secretWord[i] == userInput:
            t = t + 1
        else:
            f = f + 1
        i = i - 1
    if t > 0:
        return True
    else:
        return False
    

def emojified(guess: str, secret: str) -> str:
    """This function "EMOJIFIES' any given value to its respective color."""
    assert len(guess) == len(secret)
    # asserts that the lengths equal each other
    WHITE_BOX: str = "\U00002B1C"
    YELLOW_BOX: str = "\U0001F7E8"
    GREEN_BOX: str = "\U0001F7E9"
    # intializers for the emojis
    emoji = ""
    i: int = 0
    while i < len(guess):
        # while loops that assigns emojis to a users guesses
        if guess[i] == secret[i]:
            emoji += GREEN_BOX
        else:
            if contains_char(secret, guess[i]):
                emoji += YELLOW_BOX
            else:
                emoji += WHITE_BOX
        i = i + 1
    return emoji


def input_guess(guess: int) -> str:
    """This function takes uer input and checks if it has the correct amt of characters."""
    user_input: str = input(f"Enter a {guess} character word: ")
    # user input
    while len(user_input) != guess:
        # checks if amt of characters the user inputted is equal to the amt of characters "guess" is equal to
        user_input = input(f"That wasn't {guess} chars! Try again: ")
    return user_input


def main() -> None:
    """This is the main function that operates similarly to the game 'Wordle'."""
    N: int = 1
    # i ntializers for the loop
    secrets = "codes"
    while N <= 6:
        # while loops that runs as long as the integer N is less than 6(the amt of characters in wordle)
        print("=== Turn " + str(N) + "/6 ===")

        userInp = input_guess(5)

        if userInp == secrets:
            # checks to see if the user has won
            print(emojified(userInp, secrets))
            print("You won in " + str(N) + "/6 turns!")
            return None 
        print(emojified(userInp, secrets))
        # prints curent score
        N = N + 1
    print("X/6 - Sorry, try again tomorrow!")
    # losing statement


if __name__ == "__main__":
    main() 