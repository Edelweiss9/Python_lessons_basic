# Задание-1:
# Доработайте реализацию программы из примера examples/5_with_args.py,
# добавив реализацию следующих команд (переданных в качестве аргументов):
#   cp <file_name> - создает копию указанного файла
#   rm <file_name> - удаляет указанный файл (запросить подтверждение операции)
#   cd <full_path or relative_path> - меняет текущую директорию на указанную
#   ls - отображение полного пути текущей директории
# путь считать абсолютным (full_path) -
# в Linux начинается с /, в Windows с имени диска,
# все остальные пути считать относительными.

# Важно! Все операции должны выполняться в той директории, в который вы находитесь.
# Исходной директорией считать ту, в которой был запущен скрипт.

# P.S. По возможности, сделайте кросс-платформенную реализацию.

import os
import sys
import shutil

print('sys.argv = ', sys.argv)


def print_help():
    print('help - list of commands')
    print('mkdir <dir_name> - create folder')
    print('cp <filename> - copy file')
    print('ping - table tennis!')


def make_dir():
    if not dir_name:
        print('Please enter folder name: mkdir <dir_name>')
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.mkdir(dir_path)
        print('Dir {} created'.format(dir_name))
    except FileExistsError:
        print('Dir {} already exists'.format(dir_name))


def cp():
    if not dir_name:
        print('Please enter folder to copy: cp <dir_name>')
        return
    # dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        new = '.copy'
        shutil.copy2(os.path.join(os.getcwd(), dir_name), new)
        print('File {} successfully copied.'.format(dir_name))
    except FileNotFoundError:
        print('File {} not found. Nothing to copy.'.format(dir_name))


def ping():
    print('PONG!')


do = {
    'help': print_help,
    'mkdir': make_dir,
    'ping': ping,
    'cp': cp
}
try:
    dir_name = sys.argv[2]
except IndexError:
    dir_name = None

try:
    key = sys.argv[1]
except IndexError:
    key = None

if key:
    if do.get(key):
        do[key]()
    else:
        print('Invalid input, type "help".')

# if __name__ == "__main__":
#     main()
