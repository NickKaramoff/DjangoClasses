import os
import shutil


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
    file = open(path)
    for line in file.readlines():
        print(line)


def create_file(name):
    pass


def create_folder(name):
    os.mkdir('%s/%s' % (os.getcwd(), name))


def copy_file(old_path, new_path):
    shutil.copy(old_path, new_path)


def move_file(old_path, new_path):
    shutil.move(old_path, new_path)


def delete_file(name):
    os.remove('%s/%s' % (os.getcwd(), name))


def rename_file(name, new_name):
    os.renames(name, new_name)


is_running = True

while is_running:
    command = input('> ')

    command = command.split(' ')

    if command[0] == 'exit':
        is_running = False
    elif command[0] == 'help':
        print("pwd\t\tprints path to current directory")
        print("cd\t\tchange current directory")
        print("ls\t\tprints contents of current directory")
        print("cat\t\tprints contents of file")
        print("cp\t\tcopies file")
        print("mv\t\tmoves file")
        print("help\t\tshows this text")
        print("exit\t\texits the program")
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
