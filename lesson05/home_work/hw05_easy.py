# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os
import shutil

# if __name__ == "__main__":
#     pass

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


# Удаление конкретной папки

def specFolderDeleter(dir):
    try:
        shutil.rmtree(os.path.join(os.getcwd(), '{}'.format(dir)))
        print('Folder "{}" deleted!'.format(dir))
    except FileNotFoundError as err:
        print(err)


# Создание конкретной папки в текущей директории

def specFolderCreator(dir):
    try:
        os.mkdir(dir)
        print('Folder "{}" created'.format(dir))
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


# -----------------------------------------------------------------------------
# Export:

def pathChanger(new):
    try:
        os.chdir(new)
        print('Changed dir to: ' + os.getcwd())
    except FileNotFoundError:
        print('Dir "{}" not found!'.format(new))
