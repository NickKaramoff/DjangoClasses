def task_one(numbers):
    for number in numbers:
        if number % 2 == 0:
            return True
    return False


print(task_one((23, 43, 45, 65, 75, 85, 73)))
print(task_one((23, 43, 45, 65, 75, 66, 73)))
