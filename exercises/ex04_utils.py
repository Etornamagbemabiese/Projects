"""EX03 UTILS."""
__author__ = "730645861"


def all(input: list[int], same: int) -> bool:
    """Function returns if all of the list indexes are the same as the given input."""
    if len(input) == 0:  # checks if array has numbers in it
        return False
    loop: int = len(input)  # intializes loop variable
    while loop > 0:  # checks if inputs are the same
        if same == input[loop - 1]:
            loop -= 1
        else:
            return False
    return True


def max(input: list[int]) -> int:
    """Function returns the max int in a list."""
    if len(input) == 0:  # checks if array has numbers in it
        raise ValueError("max() arg is an empty List")  
    loop: int = len(input)  # intializes loop variable
    max_ind: int = input[0]  # intializes max variable
    while loop > 0:  # loop that finds max int
        if input[loop - 1] > max_ind:
            max_ind = input[loop - 1]
        loop -= 1
    
    return max_ind


def is_equal(input_one: list[int], input_two: list[int]) -> bool:
    """Function returns if two lists are equal to each other."""
    if len(input_one) != len(input_two):  # checks if the array lengths are equal
        return False
    loop = len(input_one)  # intializes loop variable
    while loop > 0:  # checks if lists are the same at each index
        if input_one[loop - 1] != input_two[loop - 1]:
            return False
        loop -= 1
    return True
