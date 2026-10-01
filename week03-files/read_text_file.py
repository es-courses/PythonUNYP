
file = open("data.txt")

lines = file.readlines()

for line in lines:
    line = line.strip()
    print(line)