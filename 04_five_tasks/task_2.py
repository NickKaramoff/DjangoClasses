def task_two(numbers):
    prev_number = 0
    for number in numbers:
        if number > 0 and prev_number % 2 == 0:
            return False
        prev_number = number
    return True


print(task_two((-1, 26, -3, 44)))
print(task_two((-1, 26, -2, 44)))
