

def args_example(a, b, *args, **kwargs):
    print(f"a: {a}")
    print(f"b: {b}")
    print(f"args: {args}")
    print(f"kwargs: {kwargs}")


args_example(3, 4, 12, 15, 17, 18, target='xyz', value=88)





