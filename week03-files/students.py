
file = open("data.csv")

lines = file.readlines()

labels = lines[0].strip().split(',')

total = 0
counter = 0

for line in lines[1:]:
    student = line.strip().split(',')
    print(f"{labels[0]}: {student[0]}, {labels[1]}: {student[1]}, {labels[2]}: {student[2]}")
    total = total + float(student[2])
    counter = counter + 1

print(f"Average GPA: {total/counter}")