
class Student:
    def __init__(self, name, major):
        self.name = name
        self.major = major
        self.courses = {}

    def add_course(self, course, grade):
        if 0 < grade < 100:
            self.courses[course] = grade 
        else:
            print(f"Grade {grade} is invalid")

    def display_courses(self):
        for course in self.courses:
            grade = self.courses[course]
            print(f"{course}, grade: {grade}")

    def __str__(self):
        return f"{self.name}, major: {self.major}"


if __name__ == '__main__':
    a = Student('Bill', 'Business')
    print(a)
    b = a
    print(b)
    c = Student('Mark', 'Finance')
    print(c)

    c.add_course('python', 96)
    c.add_course('java', 82)
    c.add_course('SQL', 88)

    c.display_courses()