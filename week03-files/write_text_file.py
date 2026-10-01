
# file = open("courses.txt", "w")
file = open("courses.txt", "a")

course = input("New course name: ")

file.write(f"{course}\n")