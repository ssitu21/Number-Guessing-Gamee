# Import random module to generate a random number
import random


# Function to get a valid integer input with error handling
def get_valid_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a whoe number.")


# Function to get a valid 'y' or 'n' response from the user
def get_yes_no(prompt):
    while True:
        response = input(prompt).strip().lower()
        if response in ("y", "n"):
            return response
        print("Please enter 'y' or 'n'.")


# Function to play one round of the game
def play_round():
    pass


# Main game loop
def main():
    # Ask for user's name and greet them
    name = input("Whats your name: ")
    print(f"Hello, {name}! Welcome to the Number Guessing Game.")


# Run the game
if __name__ == "__main__":
    main()
