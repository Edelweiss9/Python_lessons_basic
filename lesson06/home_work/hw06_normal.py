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

    # Отдельно функцию для родителей (несовпадающие фамилии)

    def __str__(self):
        return '{} {}, {}, {}'.format(self.last_name, self.first_name,
                                      self.otousan, self.okaasan)

    def __repr__(self):
        return '{} {}, {}, {}'.format(self.last_name, self.first_name,
                                      self.otousan, self.okaasan)


class Teacher(Human):
    def __init__(self, id, last_name, first_name, subjects):
        Human.__init__(self, id, last_name, first_name)
        self.subjects = subjects

    def __str__(self):
        return '{} {}, {}'.format(self.last_name, self.first_name,
                                  self.subjects)

    def __repr__(self):
        return '{} {}, {}'.format(self.last_name, self.first_name,
                                  self.subjects)


class Subject:
    def __init__(self, id, subject):
        self.id = id
        self.subject = subject

    def __str__(self):
        return '{}'.format(self.subject)

    def __repr__(self):
        return '{}'.format(self.subject)


class Grade:
    def __init__(self, id, grade, pupils, teachers):
        self.id = id
        self.grade = grade
        self.pupils = pupils
        self.teachers = teachers

    def __str__(self):
        return '{}. {}. {}.'.format(self.grade, self.pupils, self.teachers)

    def __repr__(self):
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
        for i in teachers:
            print(teachers[i].subjects)


sub1 = Subject('id_ninjutsu', 'Ninjutsu')
sub2 = Subject('id_ninja_history', 'Ninja_history')
sub3 = Subject('id_genjutsu', 'Genjutsu')

t0 = Teacher(1, 'Hatake', 'Kakashi', {sub1.id: sub1})
t1 = Teacher(2, 'Sarutobi', 'Hiruzen', {sub2.id: sub2})
t2 = Teacher(3, 'Uchiha', 'Izuna', {sub3.id: sub3})

p0 = Pupil(4, 'Uzumaki', 'Naruto', Human(10, 'last_name', 'otousan'),
           Human(11, 'last_name', 'okaasan'), 'grade_7')
p1 = Pupil(5, 'Uchiha', 'Sasuke', Human(12, 'last_name', 'otousan'),
           Human(13, 'last_name', 'okaasan'), 'grade_7')
p2 = Pupil(6, 'Inuzuka', 'Kiba', Human(14, 'last_name', 'otousan'),
           Human(15, 'last_name', 'okaasan'), 'grade_8')
p3 = Pupil(7, 'Aburame', 'Shino', Human(16, 'last_name', 'otousan'),
           Human(17, 'last_name', 'okaasan'), 'grade_9')

grade_7 = Grade(77, 'Grade 7', {p0.id: p0, p1.id: p1}, {t0.id: t0})
grade_8 = Grade(88, 'Grade 8', {p1.id: p1, p2.id: p2}, {t1.id: t1, t2.id: t2})
grade_9 = Grade(99, 'Grade 9', {p2.id: p2, p3.id: p3}, {t2.id: t2})

subjects = {
    'id_ninjutsu': sub1,
    'id_ninja_history': sub2,
    'id_genjutsu': sub3,
}

teachers = {}
parents = {}

grades = {
    grade_7.id: grade_7,
    grade_8.id: grade_8,
    grade_9.id: grade_9,
}

pupils = {
    p0.id: p0,
    p1.id: p1,
    p2.id: p2,
    p3.id: p3,
}

school = School('Konoha Ninja Academy', teachers, grades, pupils)

print('Grades:\n', school.grades)
print('***')
# print('Pupils in grade 7:\n')
# school.display_pupils('grade_7')
print('***')
# school.show_subjects_of_pupil(4)
print('***')
# print(p0.otousan)
# print(p0.okaasan)
print('***')
# print(school.display_teachers_grades('grade_7'))
#
#
# ***Unfinished***
#
# 0) Parents names as dict?
# 1) ID
# 2) KeyError 104, 161
# 3)
# 4)
