
def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

# If the current py file is been executed
if __name__ == '__main__':
    value = int(input("Give a value: "))

    if is_even(value):
        print(f"{value} is EVEN")
    else:
        print(f"{value} is ODD")