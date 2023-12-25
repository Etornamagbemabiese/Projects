"""EX01 - Chardle - A cute step toward Worldle."""
__author__ = "730645861"

five_Word: str = input("Enter a 5-character word:") 


if len(five_Word) != 5:
    print("Error:word must contain 5 characters")
    exit()
else:
    single_Character: str = input("Enter a single character:") 

    if len(single_Character) != 1:
        print("Error:Character must be a single character.")
        exit()
    else:
        print("Searching for " + single_Character + " in " + five_Word)
        instanceCounter = 0
        counter = 0

        if single_Character == five_Word[0]:
            print(single_Character + " found at index " + str(counter))
            instanceCounter = instanceCounter + 1

        counter = counter + 1
        if single_Character == five_Word[1]:
            print(single_Character + " found at index " + str(counter))
            instanceCounter = instanceCounter + 1

        counter = counter + 1
        if single_Character == five_Word[2]:
            print(single_Character + " found at index " + str(counter))
            instanceCounter = instanceCounter + 1

        counter = counter + 1
        if single_Character == five_Word[3]:
            print(single_Character + " found at index " + str(counter))
            instanceCounter = instanceCounter + 1

        counter = counter + 1
        if single_Character == five_Word[4]:
            print(single_Character + " found at index " + str(counter))
            instanceCounter = instanceCounter + 1

        if instanceCounter <= 0:
            print("No instances of " + single_Character + " found in " + five_Word)
        if instanceCounter > 1:
            print(str(instanceCounter) + " instances of " + single_Character + " found in " + five_Word)
        if instanceCounter == 1:
            print(str(instanceCounter) + " instance of " + single_Character + " found in " + five_Word)
