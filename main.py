# Import random module to generate a random numberx
import random


# Function to get a valid number
def get_valid_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter an whole number. 😅 ")


# Function to get a valid 'y' or 'n'
def get_yes_no(prompt):
    while True:
        response = input(prompt).strip().lower()
        if response in ("y", "n"):
            return response
        print("Please enter 'y' or 'n'.👹")


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

    # find number of attempts
    attempts = 0
    print(f"You have {max_attempts} 💀  attempts to guess the number.\n")

    # Guessing loop
    while attempts < max_attempts:
        guess = get_valid_int("Your guess: ")
        attempts += 1

        # Check if guess is too low or too high
        if guess < secret:
            print("Too low! 😅")
        elif guess > secret:
            print("Too high! 😅")
        else:
            # Display success message if guessed correctly
            print(f"\nGGs!🥳 You guessed it in {attempts} attempt(s).🥳 😁")
            return True

    print(
        f"\nGame Over 😭   you've used all {max_attempts} attempts. The number was {secret}. 😭"
    )
    return False
    # Guessing loop ends here


# Main game loop
def main():
    # Ask for user's name and greet them
    name = input("Whats your name: ")
    print(f"Hello, {name}! 🖐️   Welcome to the Number Guessing Game.\n")

    # Replay loop
    playing = True
    while playing:
        play_round()
        # Ask want to play again
        again = get_yes_no("\nDo you want to play again (y/n) 😱  : ")
        if again == "n":
            playing = False

    print(f"Thanks for playing, 👀 {name}! Goodbye! 🤞")


# Run the game
if __name__ == "__main__":
    main()
