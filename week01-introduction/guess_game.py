import random

print("NUMBER GUESS GAME")

# Set the secret value (1 - 100)
secret = random.randint(1, 100)
print(secret)

# Set a counter to 0. This will count how many guesses user had
counter = 0

# Set a variable to keep user's guess. 
# I use -1 so that whatever secret is, I will get into the loop
user_guess = -1

# Repeat as long as guess is different than secret
while user_guess != secret:

    # Ask user for their guess
    user_guess = int(input('Guess: '))
    counter = counter + 1

    # Check value and display proper message
    if user_guess > secret:
        print("Go Down")
    elif user_guess < secret:
        print("Go Up")
    else:
        print(f"Found in {counter} guesses")

print("GAME OVER")
