from student import Student

class Course:
    def __init__(self, title, credit):
        self.title = title
        self.credit = credit
        self.students = []


    def add_student(self, student):
        self.students.append(student)


    def roster(self):
        print("==== ROSTER ====")
        for student in self.students:
            print(student)


if __name__ == '__main__':
    a = Course('python', 4)
    a.add_student(Student('Geogre', 'IT'))
    a.add_student(Student('Michael', 'IR'))
    a.add_student(Student('Jenn', 'IT'))
    a.add_student(Student('Mary', 'Comm'))

    a.roster()
