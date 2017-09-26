# Задача-1:
# Дан список, заполненный произвольными целыми числами, получите новый список,
# элементами которого будут квадратные корни элементов исходного списка,
# но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь
# Пример: Дано: [2, -5, 8, 9, -25, 25, 4]   Результат: [3, 5, 2]

a = [2, -5, 8, 9, -25, 25, 4]
b = []

for i in a:
    if i > 0:
        if (math.sqrt(i)) % 1 == 0:
            i = math.sqrt(i)
            b.append(int(i))
print(b)

# Задача-2: Дана дата в формате dd.mm.yyyy, например: 02.11.2013.
# Ваша задача вывести дату в текстовом виде, например: второе ноября 2013 года.
# Склонением пренебречь (2000 года, 2010 года)

days = {
    '01': 'First',
    '02': 'Second',
    '03': 'Third',
    '04': 'Fourth',
    '05': 'Fifth',
    '06': 'Sixth',
    '07': 'Seventh',
    '08': 'Eighth',
    '09': 'Ninth',
    '10': 'Tenth',
    '11': 'Eleventh',
    '12': 'Twelfth',
    '13': 'Thirteenth',
    '14': 'Fourteenth',
    '15': 'Fifteenth ',
    '16': 'Sixteenth ',
    '17': 'Seventeenth',
    '18': 'Eighteenth',
    '19': 'Nineteenth',
    '20': 'Twenty',
    '21': 'Twenty first',
    '22': 'Twenty second',
    '23': 'Twenty third',
    '24': 'Twenty fourth',
    '25': 'Twenty fifth',
    '26': 'Twenty sixth',
    '27': 'Twenty seventh',
    '28': 'Twenty eighth',
    '29': 'Twenty ninth',
    '30': 'Thirty',
    '31': 'Thirty first'
}

months = {
    '01': 'January',
    '02': 'February',
    '03': 'March',
    '04': 'April',
    '05': 'May',
    '06': 'June',
    '07': 'July',
    '08': 'August',
    '09': 'September',
    '10': 'October',
    '11': 'November',
    '12': 'December'
}

while True:
    date = input('Enter date dd.mm.yyyy: ').split('.')
    try:
        if len(date) == 3 and int(date[0]) in range(1, 32) and int(date[1]) in range(1, 13) and int(date[2]) in range(1, 10000):
            print('{} {} {} year'.format(days[date[0]], months[date[1]], date[2]))
            break
    except ValueError:
        print('Numbers only!')
        continue
    else:
        print('Only dd.mm.yyyy accepted!')

#Мне не очень нравится длина 74 строчки, как это прилично сделать?


# Задача-3: Напишите алгоритм, заполняющий список произвольными целыми числами
# в диапазоне от -100 до 100. В списке должно быть n - элементов.
# Подсказка:
# для получения случайного числа используйте функцию randint() модуля random

import random

while True:
    try:
        n = int(input('Enter positive number: '))
        if n > 0:
          print([random.randint(-100, 100) for num in range(n)])
          break
    except ValueError:
        print('Error! No floats or symbols!')
        continue
    else:
        print('Error! Positive only!')

# Задача-4: Дан список, заполненный произвольными целыми числами.
# Получите новый список, элементами которого будут: 
# а) неповторяющиеся элементы исходного списка:
# например, lst = [1, 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 2, 4, 5, 6]
# б) элементы исходного списка, которые не имеют повторений:
# например, lst = [1 , 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 4, 6]

list_one = [1, 2, 4, 5, 6, 2, 5, 2]

print(list(set(list_one)))

list_two = []

for i in list_one:
    if list_one.count(i) == 1:
        list_two.append(i)
print(list_two)

