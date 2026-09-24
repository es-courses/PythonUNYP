
# LISTS

a = [12, 15, 17, 19, 22, 28]
print(a[0])
print(len(a))

# find the value at the last position
print(a[len(a) - 1])
print(a[-1])

print(sum(a)/len(a))

# Iterate through a list (traditional way)
for i in range(0, len(a)):
    print(a[i])

# Iterate in simple pythonian way
for value in a:
    print(value)


# List range
print(a[1:3])
print(a[:3])
print(a[3:])

# LISTS of 2 Dimentions

data = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(data[0])
print(data[0][1])

a[0] = 11
print(a)

a.append(27)
print(a)


# TUPLES  (are immutable)

b = (3, 6, 8, 12, 17, 19)


# DICTIONARIES 

student = {'id': 80, 'name': 'Nick', 'gpa': 3.5}
print(student['name'])


for key in student:
    print(key, student[key])

for key, value in student.items():
    print(key, value)


students = [
    {'id': 80, 'name': 'Nick', 'gpa': 3.5},
    {'id': 81, 'name': 'Ann', 'gpa': 3.8},
    {'id': 80, 'name': 'John', 'gpa': 3.0}
]

for s in students:
    print(f"{s['name']}, GPA: {s['gpa']}")


# STRING is a LIST of characters

sentence = "This is an example of Strings in Python"
print(sentence[0])
print(len(sentence))
print(sentence[5:10])
print(sentence[-1])

