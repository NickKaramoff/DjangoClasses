import os
import shutil
from functools import reduce


def show_files():
    walk = os.walk(os.getcwd()).__next__()

    directories = walk[1]
    directories.sort()
    files = walk[2]
    files.sort()

    print('folders:')
    for directory in directories:
        print('\t%s' % directory)

    print('files:')
    for file in files:
        print('\t%s' % file)


def print_directory():
    print(os.getcwd())


def change_directory(path='.'):
    os.chdir(path)


def print_file(path):
    try:
        file = open(path)
        for line in file.readlines():
            print(line)
    except FileNotFoundError:
        print("File not found: %s" % path)


def create_folder(name):
    os.mkdir('%s/%s' % (os.getcwd(), name))


def copy_file(old_path, new_path):
    shutil.copy(old_path, new_path)


def super_copy_file(path, amount):
    width = len(str(amount))

    for i in range(int(amount)):
        path_arr = path.split('.')

        new_path = reduce(lambda acc, elem: acc + elem, path_arr[:-1])
        new_path += '_' + str(i + 1).zfill(width)
        new_path += '.' + path_arr[-1]

        copy_file(path, new_path)


def move_file(old_path, new_path):
    shutil.move(old_path, new_path)


def delete_file(name):
    os.remove('%s/%s' % (os.getcwd(), name))


def rename_file(name, new_name):
    os.renames(name, new_name)


def print_help():
    max_command_width = 16 + 1

    print("%s prints path to current directory" %
          "pwd".ljust(max_command_width))

    print("%s change current directory" %
          "cd DIRNAME".ljust(max_command_width))

    print("%s prints contents of current directory" %
          "ls".ljust(max_command_width))

    print("%s prints contents of file" %
          "cat FILE".ljust(max_command_width))

    print("%s copies file" %
          "cp FILE LOCATION".ljust(max_command_width))

    print("%s copies file many times" %
          "scp FILE AMOUNT".ljust(max_command_width))

    print("%s moves file" %
          "mv FILE LOCATION".ljust(max_command_width))

    print("%s shows this text" %
          "help".ljust(max_command_width))

    print("%s exits the program" %
          "exit".ljust(max_command_width))

    print("%s exits the program" %
          "q".ljust(max_command_width))


is_running = True

while is_running:
    command = input('$ ')

    command = command.split(' ')

    if command[0] == 'exit' or command[0] == 'q':
        is_running = False
    elif command[0] == 'help':
        print_help()
    elif command[0] == 'ls':
        show_files()
    elif command[0] == 'cd':
        if len(command) > 1:
            change_directory(command[1])
        else:
            print('Error: Directory not provided!')
    elif command[0] == 'pwd':
        print_directory()
    elif command[0] == 'cat':
        if len(command) > 1:
            print_file(command[1])
        else:
            print('Error: File not provided!')
    elif command[0] == 'mkdir':
        if len(command) > 1:
            create_folder(command[1])
        else:
            print('Error: Directory name not provided!')
    elif command[0] == 'cp':
        if len(command) > 2:
            copy_file(command[1], command[2])
        elif len(command) > 1:
            print('Error: Destination not provided!')
        else:
            print('Error: Source and destination not provided!')
    elif command[0] == 'scp':
        if len(command) > 2:
            super_copy_file(command[1], command[2])
        elif len(command) > 1:
            print('Error: Amount not provided!')
        else:
            print('Error: File and amount not provided!')
    elif command[0] == 'mv':
        if len(command) > 2:
            move_file(command[1], command[2])
        elif len(command) > 1:
            print('Error: Destination not provided!')
        else:
            print('Error: Source and destination not provided!')

    else:
        print("Error: Unsupported command!")
        print("Print 'help' to get the list of supported commands")

    print()
