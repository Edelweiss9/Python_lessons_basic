# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать
# в неограниченном кол-ве классов свой определенный предмет.
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе

class Human:
    def __init__(self, id, last_name, first_name):
        self.id = id
        self.last_name = last_name
        self.first_name = first_name

    def __str__(self):
        return '{} {}'.format(self.last_name, self.first_name)


class Pupil(Human):
    def __init__(self, id, last_name, first_name, grade, otousan, okaasan):
        Human.__init__(self, id, last_name, first_name)
        self.grade = grade
        self.otousan = otousan
        self.okaasan = okaasan

    def __str__(self):
        return '{} {}, {}, {}'.format(self.last_name, self.first_name,
                                      self.otousan, self.okaasan)


class Teacher(Human):
    def __init__(self, id, last_name, first_name, subject):
        Human.__init__(self, id, last_name, first_name)
        self.subject = subject

    def __str__(self):
        return '{} {}, {}'.format(self.last_name, self.first_name,
                                  self.subject)


class Subject:
    def __init__(self, id, subject):
        self.id = id
        self.subject = subject

    def __str__(self):
        return '{}'.self.subject


class Grade:
    def __init__(self, id, grade, pupils, teachers):
        self.id = id
        self.grade = grade
        self.pupils = pupils
        self.teachers = teachers

    def __str__(self):
        return '{}. {}. {}.'.format(self.grade, self.pupils, self.teachers)


class School:
    def __init__(self, title, teachers, grades, pupils):
        self.title = title
        self.teachers = teachers
        self.grades = grades
        self.pupils = pupils

    def __str__(self):
        return '{}'.format(self.title)

    def display_teachers_grades(self, grade_id):
        grade = self.grades[grade_id]
        print(grade.teachers)

    def display_grade_list(self):
        for grade in grades:
            print('{}. Pupils list: \n {}'.format(grade.grade, grade.pupils))

    def display_pupils(self, grade_id):
        print(self.grades[grade_id].pupils)

    def show_subjects_of_pupil(self, pupil_id):
        grade = self.pupils[pupil_id].grade
        teachers = self.grades[grade].teachers
        for t in teachers:
            print(teachers[t].subjects)


school = School('Konoha Ninja Academy', teachers, grades, pupils)

t0 = Teacher(1, 'Hatake', 'Kakashi', {sub1.id: sub1})
t1 = Teacher(2, 'Sarutobi', 'Hiruzen', {sub2.id: sub2})
t2 = Teacher(3, 'Uchiha', 'Izuna', {sub3.id: sub3})

subjects = {
    'id_ninjutsu': sub1,
    'id_ninja_history': sub2,
    'id_genjutsu': sub3
}

p0 = Pupil(4, 'Uzumaki', 'Naruto', Human(id, 'last_name', 'otousan'),
           Human(id, 'last_name', 'okaasan'), 'grade')


# ***Unfinished***
#
# 0) Grades + grades list + grade.grade check
# 1) Pupils list
# 2) Parents surname check
# 3) ID!
# 4) Names similarity in functions check
