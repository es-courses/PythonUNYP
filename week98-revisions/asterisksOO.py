
class AsterisksPrinter:
    def __init__(self, n):
        self.n = n 
        print(f"New Asterisk Printer created with a value of {self.n}")

    def print_line_of_chars(self, ch, times):
        """ Prints a line repeating character ch, times times  """
        for j in range(times):
            print(ch, end=' ')

    def fix_tree_size(self):
        """ Sets the tree size to be always odd """
        if self.n % 2 == 0:
            size = self.n + 1
        else:
            size = self.n
        return size
    
    def draw_triangle(self):
        for i in range(self.n):
            self.print_line_of_chars('*', i+1)
            print()

    def draw_tree(self):
        asterisks = 1
        size = self.fix_tree_size()
        spaces = size // 2
        for i in range(n//2+1):
            self.print_line_of_chars(' ', spaces)
            self.print_line_of_chars('*', asterisks)
            asterisks = asterisks + 2
            spaces = spaces - 1
            print()

    def draw_diamond(self):
        pass



# This means that run the following code ONLY if I execute this file
# If I import it in another file, don't run
if __name__ == '__main__':
    n = int(input("Number: "))
    ap = AsterisksPrinter(n)
    print("TRIANGLE")
    ap.draw_triangle()
    print()
    print("TREE")
    ap.draw_tree()
    print()
    print("DIAMOND")
    ap.draw_diamond()