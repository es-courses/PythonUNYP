
import csv 

file = open("data.csv")

reader = csv.DictReader(file)

for student in reader:
    print(student)
    print(f"id: {student['id']}, name: {student['name']}, gpa: {student['gpa']}")
        