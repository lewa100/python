import csv
import os

file1 = 'phone.txt'
file2 = 'phonebook.csv'
out = 'out.csv'
input_target_text = 'Введите вариант:'
input_row_number_text = 'Введите номер строки для копирования:'

enter_position = lambda text:int(input(text))
clear_console = lambda: os.system('cls' if os.name == 'nt' else 'clear')
clear_space = lambda s: list(map(lambda s: s.strip(), s))

def enter_position(text):
    while True:
        try:
            return int(input(text))
        except ValueError:
            print('Введите корректно число!')
            continue

def print_menu():
    clear_console()
    print("\n\t\t----====МЕНЮ====----")
    print(f"1.\t Распечатать файл {file1}")
    print(f"2.\t Распечатать файл {file2}")
    print(f"3.\t Копируем строку из файла {file1} в файл {file2}")
    print(f"4.\t Копируем строку из файла {file2} в файл {file1}")
    print("9.\t Выход\n")

def print_file(file):
    print(f"\n############ ФАЙЛ {file} ############")
    with open(file,'r', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter=",")
        for s in reader:
            s = clear_space(s)
            print(s)
    print()
    input("Press Enter to continue...")

def copy_row(file1,file2,num):
    row = list()
    with open(file1, 'r', encoding='utf-8') as f1:
        reader = csv.reader(f1, delimiter=",")
        lst = list(reader)
        if len(lst) < num:
            print(f"Строки с №{num} нет в файле {file1}")
            input("Press Enter to continue...")
            return
        row = clear_space(lst[num-1])
    print(row)
    with (open(file2, 'a', encoding='utf-8') as f2):
        writer = csv.writer(f2,delimiter=",")
        writer.writerow(row)
    input("Press Enter to continue...")

target = 0
while (target!=9):
    print_menu()
    target = enter_position(input_target_text)
    if target == 1:
        print_file(file1)
    elif target == 2:
        print_file(file2)
    elif target == 3:
        n = enter_position(input_row_number_text)
        copy_row(file1,file2,n)
    elif target == 4:
        n = enter_position(input_row_number_text)
        copy_row(file2,file1,n)

    elif target != 9:
        print('Введите корректно пункт меню!')
        input("Press Enter to continue...")



