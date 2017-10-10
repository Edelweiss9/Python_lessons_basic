# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os
import shutil


# Создание папок вида dir_n

def folderNumCreator(n):
    for i in range(0, n):
        try:
            os.mkdir(os.path.join(os.getcwd(), 'dir_{}'.format(i)))
            print('Folder dir_{} created.'.format(i))
        except FileExistsError:
            print('Folder dir_{} already exists!'.format(i))
            continue


# Удаление n-папок вида dir_n от меньшего имени

def folderNumDeleter(n):
    for i in range(0, n):
        try:
            shutil.rmtree(os.path.join(os.getcwd(), 'dir_{}'.format(i)))
        except NameError:
            print('Folder dir_{} does not exist!.'.format(i))


# Удаление папки

def specFolderDeleter():
    path = str(input('WARNING! This will delete even non-empty folder! Enter dir: '))
    try:
        shutil.rmtree(os.path.join(os.getcwd(), '{}'.format(path)))
        print('Folder "{}" deleted!'.format(path))
    except FileNotFoundError as err:
        print(err)


# Создание папки

def specFolderCreator():
    name = str(input('Enter folder name: '))
    try:
        os.mkdir(name)
        print('Folder "{}" created'.format(name))
    except FileExistsError as err:
        print(err)


# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

def listFolders():
    dir_list = next(os.walk('.'))[1]
    print(dir_list)


# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

def copyCurrentFile():
    new = __file__ + '.copy.py'
    shutil.copy2(os.path.abspath(__file__), new)
    print('File copied: ' + os.path.abspath(__file__), new)


# -----------------------------------------------------------------------------
# Export:

def pathChanger():
    path = str(input('Enter path: '))
    try:
        os.chdir(path)
        print('Changed dir to: ' + os.getcwd())
    except FileNotFoundError:
        print('Dir "{}" not found!'.format(path))


def helpCall():
    print('"cd" - change directory: <path> or <folder_name> if folder is in current dir')
    print('"li" - display folders in current directory')
    print('"df" - delete folder')
    print('"cf" - create folder')
    print('"help" - available commands')
    print('"q" - exit')
