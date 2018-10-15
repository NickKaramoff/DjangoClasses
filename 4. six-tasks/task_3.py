def task_three(number):
    while number > 0:
        if (number % 10) % 2 != 0:
            print(number % 10)
            return True
        number //= 10
    return False


print(task_three(345))
print(task_three(666))
