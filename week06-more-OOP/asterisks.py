

class AsteriskPattern:
    def __init__(self, n):
        self.n = n 

    def print_line(self):
        for i in range(0, self.n):
            print('*', end=' ')
        print()

    def print_box(self):
        for i in range(0, self.n):
            self.print_line()


n = int(input("Give a number: "))
ap = AsteriskPattern(n)
ap.print_box()