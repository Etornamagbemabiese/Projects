def reverse_multiply(input: list[int]) -> list[int]:
    rv: list[int] = []

    counter: int = len(input) - 1
    while counter >= 0:
        rv.append(input[counter] * 2)
        counter -= 1

    return rv 

print(reverse_multiply([1, 2, 3]))