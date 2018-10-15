import re


# def task1(filename):
#     file = open(filename)
#     spaces = 0
#     digits = 0
#     upper = 0
#     lower = 0
#     other = 0
#     for line in file:
#         for char in line:
#             if char.isspace():
#                 spaces += 1
#             elif char.isdigit():
#                 digits += 1
#             elif char.isupper():
#                 upper += 1
#             elif char.islower():
#                 lower += 1
#             else:
#                 other += 1
#     print("There are overall %d characters in this file." \
# % (spaces + digits + upper + lower + other))
#     print("- Spaces: %d" % spaces)
#     print("- Digits: %d" % digits)
#     print("- Letters: %d" % (upper + lower))
#     print("  - uppercase: %d" % upper)
#     print("  - lowercase: %d" % lower)
#     print("- Other symbols: %d" % other)
#
#
# task1("l2t1.txt")


# def task1ext(filename):
#     file = open(filename)
#     count = 0
#     for line in file:
#         words = line.split(' ')
#         for word in words:
#             word = word.strip()
#             if re.fullmatch(r"[^aeiouy].*([aeiouy]){2}", word):
#                 count += 1
#     print(count)
#
#
# task1ext("l2t1e.txt")


# def task2(filename):
#     file_url = open(filename)
#     file_ssh = open(filename[:4] + "_ssh.txt", "w")
#     for line in file_url:
#         line_ssh = re.sub(r"^https?://github.com/", "git@github.com:", line)
#         file_ssh.write(line_ssh)
#
#
# task2("l2t2.txt")

# def task2ext(filename):
#     file_url = open(filename)
#     file_ssh = open(filename[:4] + "_ssh_ext.txt", "w")
#     for line in file_url:
#         line = line.strip()
#         name_pattern = r"[A-Za-z0-9_-]+"
#         re_pattern = r"https?://github.com/(?P<user>%s)/(?P<repo>%s).git" % (
#             name_pattern, name_pattern)
#         p = re.compile(re_pattern)
#         m = re.search(p, line)
#         ssh_path = "git@github.com:%s/%s.git" % (
#             m.group("user"), m.group("repo"))
#         file_ssh.write(ssh_path + "\n")
#
#
# task2ext("l2t2.txt")


def task3(filename):
    file = open(filename)

    digits = {  # Чему равны буквы
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    for line in file:
        number = line.strip() # Убираем пробелы по краям и символы конца строк
        result = 0  # Будущее число

        for i in range(0, len(number) - 1):
            if digits[number[i]] < digits[number[i + 1]]:
                # Если следующая цифра по значению больше (напр., IX), то надо
                # вычесть значение текущей цифры
                result -= digits[number[i]]
            else:
                # Иначе мы прибавляем значение текущей цифры
                result += digits[number[i]]

        result += digits[number[-1]]  # Добавляем значение последней цифры
        print(result)


task3("l2t3.txt")
