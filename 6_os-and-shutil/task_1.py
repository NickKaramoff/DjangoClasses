import os
from datetime import datetime


def list_files_between(path, date_1, date_2):
    date_1 = datetime.strptime(date_1, "%d.%m.%Y")
    date_2 = datetime.strptime(date_2, "%d.%m.%Y")

    os.chdir(path)

    for file in os.listdir(os.getcwd()):
        file_date = datetime.fromtimestamp(os.path.getmtime(file))
        if date_1 < file_date < date_2:
            print(file)


in_path = input('Input path: ')
in_start_date = input('Input start date: ')
in_end_date = input('Input end date: ')

list_files_between(in_path, in_start_date, in_end_date)
