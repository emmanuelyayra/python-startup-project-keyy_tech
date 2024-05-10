import time
import random
import sys

print("""             DICE ROLLING PROGRAM 
        Simulate Rolling Dice in Python
  ----------------------------------------------
""")


# Function that rolls the dice
def roll_a_dice(number_of_dice, number_of_sides):
    results = []  # Initialize an empty list to store results
    for die_number in range(1, number_of_dice + 1):
        roll_result = random.randint(1, number_of_sides)
        results.append(f"Die number {die_number}: {roll_result}")  # Append result to the list
    return results  # Return the list of results
1

while True:
    question = input("Type 1 to roll the dice or type 0 to quit: ")
    if question.isdigit():
        question = int(question)
    else:
        print("\nPlease enter a number.\n")
        continue
    time.sleep(1)

    if question == 1:
        break
    elif question == 0:
        sys.exit()
    else:
        print("\nPlease enter 1 to continue or 0 to quit.\n")
        continue
time.sleep(0.5)

while True:
    if question == 1:
        number_of_dice = input("Enter the number of dice: ")
        if number_of_dice.isdigit():
            number_of_dice = int(number_of_dice)
        else:
            print("\nPlease enter a number.\n")
            continue
    time.sleep(0.5)

    while True:
        number_of_sides = input("Enter the number of sides on each die: ")
        if number_of_sides.isdigit():
            number_of_sides = int(number_of_sides)
            break
        else:
            print("\nPlease enter a number.\n")
            continue

    print(f"\nRolling {number_of_dice} dice with {number_of_sides} sides...\n")
    time.sleep(0.5)

    result_dice = roll_a_dice(number_of_dice, number_of_sides)
    for result in result_dice:
        print(result)  # Print each result separately
        time.sleep(1)

    while True:
        play_again = input("\nWant to roll again? (yes/no): ").lower()
        if play_again == 'yes':
            print("\n")
            break
        elif play_again == "no":
            time.sleep(1)
            sys.exit("\nThanks for rolling dice with us!")
        else:
            print("Please enter 'yes' to roll again or 'no' to exit.")
            continue

    if question == 0:
        sys.exit()
    time.sleep(1)
