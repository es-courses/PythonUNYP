
valid = True 

# Read password from the user
password = input("Type password: ")

lower_count = 0
upper_count = 0
digit_count = 0
special_count = 0

# Check the length 
if len(password) < 8:
    valid = False
else:
    # Check each character if in letters (lower-upper), or in didgits, 
    # or in special characters @#!$%^&*_-
    for letter in password:
        if letter in "abcdefghijklmnopqrstuvwxyz":
            lower_count += 1
        elif letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            upper_count += 1
        elif letter in "0123456789":
            digit_count += 1
        elif letter in "@#!$%^&*_-":
            special_count += 1

    if lower_count == 0 or upper_count == 0 or digit_count == 0 or special_count == 0:
        valid = False



# If all tests pass, display OK, else display error message
if valid:
    print("OK")
else:
    print("Invalid password")