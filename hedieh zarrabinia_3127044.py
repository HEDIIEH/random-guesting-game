import random

# Generate a random number between 1 and 100
AI_choice = random.randint(1, 100)

# Initialize the number of guesses and the best score
num_guesses = 0
best_score = None

# Start the game loop
while True:
    # Ask the user to guess the number or quit
    user_guess = input("Guess the number (between 1 and 100), or 'q' to quit: ")
    
    # If the user wants to quit, end the game
    if user_guess.lower() == "q":
        print("You are Genius, thank you for playing my game!")
        break
    
    try:
        # Convert the user input to an integer
        user_guess = int(user_guess)
    except ValueError:
        # If the user input is not a number, ask them to try again
        print("Invalid input. Please enter a number or 'q' to quit.")
        continue
    
    # Increment the number of guesses
    num_guesses += 1
    
    # Check if the user's guess is correct
    if user_guess == AI_choice:
        print(f"Congratulations! You guessed the number in {num_guesses} tries.")
        # Update the best score if this is the first game or the current game is better
        if best_score is None or num_guesses < best_score:
            best_score = num_guesses
            print(f"New best score: {best_score}!")
        break
    elif user_guess < AI_choice:
        print("Too low, try again.")
    else:
        print("Too high, try again.")
    
# End the game and show the best score if it exists
print("Game Over ..., see you later, bye")
if best_score is not None:
    print(f"Your best score is {best_score}.")
