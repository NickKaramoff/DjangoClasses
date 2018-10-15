from functools import reduce


def sign(x):
    if x > 0:
        return 1
    elif x == 0:
        return 0
    else:
        return -1


def maximum(numbers):
    m = numbers[0]
    for num in numbers:
        if num > m:
            m = num
    return m


print(maximum([3, 2, 65, 1, 22]))


def summator(*args):
    summ = 0
    for num in args:
        summ = summ + num
    return summ


print(summator(1, 2, 3, 4))


def fun_summator(*args):
    return reduce(lambda x, y: x if x > y else y, args)


def date(day=1, month=9, year=2018):
    months = ["January", "February", "March",
              "April", "May", "June",
              "July", "August", "September",
              "October", "November", "December"]

    return "Today is " + str(day) + " of " + months[month - 1] + " of " + str(year) + "."


print(date(5, 10, 1999))
