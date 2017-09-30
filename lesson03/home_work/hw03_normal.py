# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def Fibonacci(n, m):
    a, b = 0, 1
    for i in range(m + 1):
        if i >= n:
            yield a
        a, b = b, a + b


print(*Fibonacci(5, 21))


# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


def sort_to_max(origin_list):
    if len(origin_list) <= 1:
        return origin_list
    else:

        go = 1
        while go < len(origin_list):
            for i in range(len(origin_list) - go):
                if origin_list[i] > origin_list[i + 1]:
                    origin_list[i], origin_list[i + 1] = origin_list[i + 1], origin_list[i]
            go += 1

    return origin_list


print(sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0]))


# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

def one_more_filter(func, data):
    return [i for i in data if func(i) == True]


# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

def is_para(a1, a2, a3, a4):
    return True if a1[1] == a4[1] or a2[1] == a3[1] and (abs(a1[0] - a2[0]) == abs(a3[0] - a4[0])) else False


c1 = (2, 2)
c2 = (2, 8)
c3 = (-9, 5)
c4 = (-8, 2)

print(is_para(c1, c2, c3, c4))
