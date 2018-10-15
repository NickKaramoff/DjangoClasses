def task_five(numbers, k):
    amt = 0
    for number in numbers:
        if number % 5 == 0:
            amt += 1
    return amt == k


print(task_five((25, 35, 45, 36), 3))
print(task_five((25, 35, 45), 2))
