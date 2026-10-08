
num = int(input("Give a number: ")) 

remainders = [] 

current = num 

while current > 0:
    remainder = current % 2
    remainders.append(remainder)
    current = current // 2

print(remainders)

binary = ''
for value in remainders:
    binary = str(value) + binary 

print(binary)