#!/usr/bin/python3

"""
== Лото ==

Правила игры в лото.

Игра ведется с помощью специальных карточек, на которых отмечены числа, 
и фишек (бочонков) с цифрами.

Количество бочонков — 90 штук (с цифрами от 1 до 90).

Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр, 
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:

--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86 
--------------------------

В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается 
случайная карточка. 

Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.

Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.
	
Побеждает тот, кто первый закроет все числа на своей карточке.

Пример одного хода:

Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71   
--------------------------
-- Карточка компьютера ---
 7 87     - 14    11      
      16 49    55 88    77    
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)

Подсказка: каждый следующий случайный бочонок из мешка удобно получать 
с помощью функции-генератора.

Подсказка: для работы с псевдослучайными числами удобно использовать 
модуль random: http://docs.python.org/3/library/random.html

"""

import random
import sys


# Так и не получилось прикрутить проверку ряда на == 'X'
# Вернее в какой-то момент получилось, захотел сделать красивее - и доломал :(

class Gambler(object):
    def __init__(self):
        self.card = Card()
        self.points = 0

    def cross(self, number=None):
        if self.check_number(number):
            print('''Crossed out!
    AI is playing...''')
            self.points += 1
            self.card.update(number)
        else:
            print('''No such number in your card!
    ~~~GAME OVER!~~~
            ''')
            sys.exit()

    def next(self, number=None):
        if self.check_number(number):
            print('''You missed the number! Be more attentive next time!
             ~~~GAME OVER!~~~
                  ''')
            sys.exit()
        else:
            pass

    def check_number(self, number):
        line = self.card.store_card()
        for seq in line:
            for el in seq:
                if el == number:
                    return True
        return False


class Human(Gambler):
    def __init__(self):
        super().__init__()
        self.card.print_new_card()

    def make_turn(self, number=None):
        print('**** YOUR CARD ****')
        self.card.show_card()
        print('''      Getting number!
        *rolling*
         ******* 
          ***** 
           ***''')
        print('Number is: ', number)
        print('''What now?
    "x" to cross out the number
    "n" to draw next number 
    "q" to end the game''')

        turn = input('')
        if turn == 'x':
            self.cross(number)
        if turn == 'n':
            self.next(number)
        if turn == 'q':
            print('NO WINNER TODAY! Thanks for playing and have a nice day!')
            sys.exit()
        while turn not in ('x', 'n', 'q'):
            turn = input('Invalid input!')


class Computer(Gambler):
    def __init__(self):
        super().__init__()
        self.card.print_new_card()

    def make_turn(self, number=None):
        print('***** AI CARD *****')
        if self.check_number(number):
            self.points += 1
        self.card.update(number)
        self.card.show_card()


class Card(object):
    def __init__(self):
        self.all_cards = [x for x in range(1, 91)]
        self.numbers_max = 15
        self.card = self.print_new_card()

    def print_new_card(self):
        c = 0
        self.random_numbers = random.sample(self.all_cards, self.numbers_max)
        self.card = [['' for x in range(9)] for i in range(3)]
        for i in range(len(self.card)):
            for j in range(len(self.card[i])):
                if j <= 4:
                    self.card[i][j] = self.random_numbers[c]
                    c += 1
        for i in range(len(self.card)):
            random.shuffle(self.card[i])
        return self.card

    def store_card(self, number=None):
        self.c = self.card[:]
        if self.update(number):
            self.c = self.update(number)
        return self.c

    # def check_row(self):
    #     self.c = self.card[:]
    #     for x in self.c:
    #         if list(filter(None, x))
    #
    #
    #         if all(list(filter(None, list))) == 'X':
    #             return True

    # def check_equal(self):
    #     list =
    #     return list[1:] == list[:-1]


    def show_card(self):
        for i in self.store_card():
            print(' '.join(map(str, i)))
        print('*******************')

    def update(self, number):
        for seq in self.card:
            for el in range(len(seq)):
                if seq[el] == number:
                    seq[el] = 'X'
        return self.card


class NumbersBank(object):
    def __init__(self):
        self.pool = [x for x in range(1, 91)]

    def roll(self):
        pick = random.choice(self.pool)
        self.pool.remove(pick)
        return pick


if __name__ == '__main__':
    print('LOTTERY 5/90! v. 1.0')
    answer = input('Wanna play? Type "y" or "n":')
    if answer == 'n':
        print('Maybe another time! See you in Vegas!')
        sys.exit()
    while answer not in ('y', 'n'):
        answer = input('Invalid input!')

    bank = NumbersBank()
    player = Human()
    AI = Computer()
    card = Card()

    while True:
        num = bank.roll()
        player.make_turn(num)
        AI.make_turn(num)
        print('Your points: ', player.points)
        print('AI points: ', AI.points)
        # if card.check_row():
        #     print('Row crossed out! Game finished!')
        #     sys.exit()
        if player.points == 5:
            print('YOU WON!')
            sys.exit()
        elif AI.points == 5:
            print('AI WON!')
            sys.exit()
