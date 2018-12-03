def our_range(*args):
    start = 0
    end = 10
    step = 1

    if len(args) == 1:
        end = args[0]
    elif 2 <= len(args) <= 3:
        start = args[0]
        end = args[1]
        if len(args) == 3:
            step = args[2]
    elif len(args) > 3:
        raise SyntaxError

    i = start
    while i < end:
        yield i
        i += step


for j in our_range(5):
    print(j)
print()

for j in our_range(2, 6):
    print(j)
print()

for j in our_range(3, 30, 9):
    print(j)
