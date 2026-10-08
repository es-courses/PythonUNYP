import random

def create_display_from_secret(secret, correct):
    display = secret[0]
    for i in range(1, len(secret)-1):
        if secret[i] in correct:
            display = display + secret[i]
        else:
            display = display + '_'
    display = display + secret[-1]
    return display

# Set a pool of words
words = ['programming', 'debugging', 'inheritance', 'polymorphism', 'encapsulation', 'composition']

# Select a random word 
last = len(words) - 1
r = random.randint(0, last)
secret = words[r]

# print(f"Last is {last}")
# print(f"r is {r}")
print(f"secret is: {secret}")

wrong = []
correct = []


# Construct the display word (with underscores)
display = create_display_from_secret(secret, correct)

# LOOP until found or hanged (actually start an endless loop, and stop in the loop if necessary)
while True:

    # Display 
    print(display)
    

    # Ask user to guess
    answer = input("Guess a letter: ")

    if len(answer) > 1:
        print("Please type one letter only.")
        continue

    # Check 
    if answer in secret:
        if answer not in correct:
            correct.append(answer)
    else: 
        if answer not in wrong:
            wrong.append(answer)

    # print(f"Correct: {correct}")
    # print(f"Wrong: {wrong}")

    # Construct the display word (with underscores)
    display = create_display_from_secret(secret, correct)

    # If found -> Display "Found!"
    if display == secret:
        print("Found!")
        break

    # If hanged -> Display "You are Hanged :("
    if len(wrong) == 6:
        print("You are Hanged :(")
        break


# Game Over
print("GAME OVER")