print("Hello World!")

salary = 1100
print(salary)

name = "John Doe"
print(name)

tax_rate = 23.6
print(tax_rate)

order_completed = False 
print(order_completed)

age = int(input("Type your age: "))
print(age)

if age <= 25:
    print("You are young")
elif 25 < age <= 50:
    print("You are old")
else:
    print("You are too old")


category = int(input("Product category: "))

match category:
    case 1:
        tax = 12
    case 2:
        tax = 20
    case 3:
        tax = 45
    case _:
        print("Wrong category")
        tax = 0

print(tax)


print("FOR LOOP")
for i in range(3, 10):
    print(i)


print("WHILE LOOP")
i = 3
while i < 10:
    print(i)
    i = i + 1


print("GAME")
answer = "Y"
while answer == "Y":
    print("Game running")
    answer = input("Continue? Y/N: ")
print("Game Over")


major = input("What is your major: ")
gpa = float(input("Your GPA: "))

print("Your GPA is " + str(gpa) + " for " + major + " major")

print("Your GPA is", gpa, "for", major, "major")

print(f"Your GPA is {gpa} for {major} major")