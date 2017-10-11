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



import hw05_easy as lib


def main():
    do = {
        'cd': lib.pathChanger,
        'li': lib.listFolders,
        'df': lib.specFolderDeleter,
        'cf': lib.specFolderCreator,
        'help': lib.helpCall,
    }

    print('What do you want me to do, human?')

    while True:
        answer = str(input())
        if answer in do:
            do[answer]()
        elif answer == 'q':
            break
        else:
            print('Invalid input, type "help".')
            continue


if __name__ == "__main__":
    main()
