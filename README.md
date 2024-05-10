# Program Features

Dice Rolling Simulation The program simulates rolling multiple dice with specified numbers of sides, providing random outcomes for each roll, and offering an engaging and interactive experience for users.

User Interaction: It interacts with users through prompts and input requests, allowing them to specify the number of dice to roll and the number of sides on each die, enhancing user engagement and customization.

Input Validation: Validates user inputs to ensure they are valid integers, handling cases where non-integer inputs are provided, ensuring smooth execution and preventing errors.

Looping Structure: Utilizes while loops for continuous operation until the user decides to exit, enabling repetitive dice rolling or quitting the program as desired, providing flexibility and convenience.

Pause Between Rolls: Includes brief pauses between each roll of the dice, enhancing the user experience by providing a sense of timing and preventing rapid consecutive rolls.

Graceful Termination: Allows users to exit gracefully by entering '0' when prompted, terminating the program's execution without errors or interruptions, ensuring a smooth user experience.

Error Handling: Handles invalid inputs and prompts users to re-enter valid choices, ensuring smooth execution without crashing or unexpected behaviour, and improving program reliability.

Clear User Instructions: Provides clear instructions and prompts at each stage of the program, guiding users through the dice-rolling process and ensuring ease of use.

Randomness: Utilizes Python's random module to generate random outcomes for each dice roll, ensuring unpredictability and realism in the simulation.

Modular Design: Organizes code into functions, such as the roll_a_dice function, promoting code reusability and maintainability.


# Program Alogthrim

Start
Import necessary libraries like time, random, and sys for program functionality.
Define a function roll_a_dice to simulate rolling a specified number of dice with a given number of sides.
Initialize an empty list to store the results.
Iterate through each die:
Generate a random number between 1 and the number of sides.
Append the result to the results list.
Return the list of results.
Start an infinite loop:
Prompt the user to type '1' to roll the dice or '0' to quit.
If the input is not a digit, prompt the user to enter a number.
If the input is '1', break out of the loop.
If the input is '0', exit the program.
Otherwise, prompt the user to enter '1' to continue or '0' to quit.
Start an infinite loop:
Prompt the user to enter the number of dice.
Prompt the user to enter the number of sides on each die.
Display a message indicating the start of the rolling process.
Roll the dice using the roll_a_dice function.
Print each roll result with a delay for user visibility.
Prompt the user if they want to roll again.
If the input is 'yes', continue to the next iteration of the loop.
If the input is 'no', exit the program.
Otherwise, prompt the user to enter 'yes' to roll again or 'no' to quit.
Stop
