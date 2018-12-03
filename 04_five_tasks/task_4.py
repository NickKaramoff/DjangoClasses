def task_four(numbers, m, k):
    amt = 0
    for number in numbers:
        if number > m:
            amt += 1
    return amt <= k


print(task_four((12, 34, 56, 78), 20, 3))
print(task_four((12, 34, 56, 78), 20, 2))
