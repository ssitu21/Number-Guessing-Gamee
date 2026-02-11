# Import random module to generate a random number
import random


# Function to get a valid integer input with error handling
def get_valid_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter an whole number.")


# Function to get a valid 'y' or 'n' response from the user
def get_yes_no(prompt):
    while True:
        response = input(prompt).strip().lower()
        if response in ("y", "n"):
            return response
        print("Please enter 'y' or 'n'.")


# Function to play one round of the game
def play_round():
    # Ask for number range
    low = get_valid_int("Enter the lowest number ")
    high = get_valid_int("Enter the highest number : ")
    # Ensure low_number is less than high_number
    while low >= high:
        print("Lower number must be less than higher numbwr. Try again.")
        low = get_valid_int("Enter the lower  number of the range: ")
        high = get_valid_int("Enter the upper number of the range: ")

    # Ask for number of attempts
    max_attempts = get_valid_int("How many attempts would you like? ")

    # Generate random number
    secret = random.randint(low, high)

    # Track number of attempts
    attempts = 0
    print(f"You have {max_attempts} attempts to guess the number.\n")


# Main game loop
def main():
    # Ask for user's name and greet them
    name = input("Whats your name: ")
    print(f"Hello, {name}! Welcome to the Number Guessing Game.\n")
    play_round()


# Run the game
if __name__ == "__main__":
    main()
