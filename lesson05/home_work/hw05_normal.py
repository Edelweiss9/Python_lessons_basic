# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py

import os
import sys
import shutil
import hw05_easy as lib

print('sys.argv = ', sys.argv)


def helpCall():
    print('"cd" - change directory: cd <path> or cd <folder_name> if folder is in current dir')
    print('"li" - list folders in current directory')
    print('"df" - delete folder: df <folder_name>')
    print('"cf" - create folder: cf <folder_name>')
    print('"help" - available commands')
    print('"q" - exit')


def main():  # main(command, arg) - ?
    do = {
        'cd': lib.pathChanger,
        'li': lib.listFolders,
        'df': lib.specFolderDeleter,
        'cf': lib.specFolderCreator,
        'help': helpCall,
        'q': sys.exit
    }

    print('What do you want me to do, human?')
    print(list(do))
    answer = str(input())
    try:
        key = sys.argv[1]
    except IndexError:
        key = None
    if answer in list(do):  # argv должен быть в словаре do. как проверить? аргв должен проверяться по input?
        do.get(key)
    else:
        print('Invalid input, type "help" to get all available commands')

# 51: slice с первой части инпута, а не весь? сравнить с листом => выдать соотв функцию == из словаря

if __name__ == "__main__":
    main()

# try:
#     dir_name = sys.argv[2]
# except IndexError:
#     dir_name = None
#
# try:
#     key = sys.argv[1]
# except IndexError:
#     key = None
#
# if key:
#     if do.get(key):
#         do[key]()
#     else:
#         print('Invalid input, type "help" to get all available commands')
