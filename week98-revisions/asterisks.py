
n = int(input("Number: "))

# Print Triangle
print("TRIANGLE")
for i in range(n):
    for j in range(i+1):
        print('*', end=' ')
    print()

print()
print("TREE")
asterisks = 1
spaces = n // 2
for i in range(n//2+1):
    for j in range(spaces):
        print(' ', end=' ')
    for j in range(asterisks):
        print('*', end=' ')
    asterisks = asterisks + 2
    spaces = spaces - 1
    print()
