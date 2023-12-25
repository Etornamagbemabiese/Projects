"""Dictionary Functions Exercise."""
__author__ = "730645861"


def invert(input: dict[str, str]) -> dict[str, str]:
    """This function inverts a dictionary."""
    output: dict[str, str] = {}
    for key in input:  # This for loop iterates through a dictionary and adds it to a dictionary
        inverted_value = input[key]
        if inverted_value in output:
            raise KeyError
        output[input[key]] = key
    return output


def favorite_color(input: dict[str, str]) -> str:
    """This function returns the most inputted color."""
    favorite: dict[str, int] = {}  # dictionary that keeps track of the most favorite colors
    counter = 0
    output = ""
    for name, color in input.items():  # This for loop iterates through the inputted dictionary and adds value to a counter which is assigned to a users favorite color
        if color in favorite: 
            favorite[color] += 5
        else:
            favorite[color] = 0

        if favorite[color] > counter:
            counter = favorite[color]
            output = color
    
    if output == "":
        none: str = "None"
        return none
    return output


def count(input: list[str]) -> dict[str, int]: 
    """This function returns a dictionary that organizes a list into a dictionary."""
    if len(input) == 0:  # checks if array has numbers in it
        raise KeyError("Len of input cannot be equal 0")  

    output: dict[str, int] = {}
    for x in input:  # This for loop iterates through a list and edits the previously intiialized output dictionary variable
        if x in output:
            output[x] += 1
        else:
            output[x] = 1
    
    return output


def alphabetizer(input: list[str]) -> dict[str, list[str]]:
    """This function alphabetizies a list."""
    output: dict[str, list[str]] = {}
    if len(input) == 0:
        return None
    for x in input:  # This for loop iterates through a list and assigns variables to a dictionary
        letter = x[0].lower()
        
        if letter in output:
            output[letter] += [x]
        else:
            output[letter] = [x]
    return output


def update_attendance(input: dict[str, list[str]], day: str, attendance: str) -> dict[str, list[str]]:
    """This function updates a dictionary with 2 strings and a dictionary."""
    if day in input:  # This for loop iterates through a list (input) and edits it based on the other inputs (day) and (attendance)
        if attendance not in input[day]:  
            input[day].append(attendance)
    else:
        input[day] = [attendance]
    return input