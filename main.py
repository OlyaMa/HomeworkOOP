class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def _average_rate(self):
        sum = 0
        counter = 0
        for grades in self.grades.values():
            for grade in grades:
                sum += grade
                counter += 1
        return sum / counter

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Not a student!')
            return
        return self._average_rate() < other._average_rate()

    def __str__(self):
        res = f'''Имя: {self.name}
Фамилия: {self.surname}
Средняя оценка за домашние задания: {round(self._average_rate(), 1)}
Курсы в процессе изучения: {",".join(self.courses_in_progress)}
Завершенные курсы: {",".join(self.finished_courses)}
'''
        return res


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def _average_rate(self):
        sum = 0
        counter = 0
        for grades in self.grades.values():
            for grade in grades:
                sum += grade
                counter += 1
        return sum / counter

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Not a lecturer!')
            return
        return self._average_rate() < other._average_rate()

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {round(self._average_rate(),1)}\n'
        return res


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\n'
        return res


iron_man = Lecturer('Toni', 'Stark')
iron_man.courses_attached += ['Python']
iron_man.courses_attached += ['Technology']

dr_strange = Lecturer('Stiven', 'Strange')
dr_strange.courses_attached += ['Chemistry']
dr_strange.courses_attached += ['Magic']
dr_strange.courses_attached += ['Python']

capitan_am = Reviewer('Stiv', 'Rogers')
capitan_am.courses_attached += ['Chemistry']
capitan_am.courses_attached += ['Magic']

hulk = Reviewer('Bruce', 'Bennet')
hulk.courses_attached += ['Python']
hulk.courses_attached += ['Technology']

spider_man = Student('Peter', 'Parker', 'm')
spider_man.courses_in_progress += ['Python']
spider_man.courses_in_progress += ['Technology']
spider_man.finished_courses += ['Chemistry']
spider_man.finished_courses += ['Magic']

scarlet_witch = Student('Vanda', 'Maksimoff', 'w')
scarlet_witch.courses_in_progress += ['Chemistry']
scarlet_witch.courses_in_progress += ['Magic']
scarlet_witch.courses_in_progress += ['Python']
scarlet_witch.finished_courses += ['Technology']

nik_fury = Mentor('Nik', 'Fury')
cap_marv = Mentor('Karol', 'Denvers')

capitan_am.rate_hw(scarlet_witch, 'Chemistry', 10)
capitan_am.rate_hw(scarlet_witch, 'Magic', 10)
hulk.rate_hw(scarlet_witch, 'Python', 6)
hulk.rate_hw(spider_man, 'Python', 9)
hulk.rate_hw(spider_man, 'Technology', 10)

spider_man.rate_hw(iron_man, 'Python', 10)
spider_man.rate_hw(dr_strange, 'Python', 8)
spider_man.rate_hw(iron_man, 'Technology', 8)
scarlet_witch.rate_hw(dr_strange, 'Chemistry', 9)
scarlet_witch.rate_hw(dr_strange, 'Magic', 10)
scarlet_witch.rate_hw(iron_man, 'Python', 7)

print(spider_man)
print(scarlet_witch)
print(spider_man < scarlet_witch)
print(scarlet_witch < spider_man)
print(iron_man)
print(dr_strange)
print(capitan_am)
print(hulk)


def av_grade_student(list, course):
    sum = 0
    counter = 0
    for student in list:
        for grade in student.grades[course]:
            sum += grade
            counter += 1
    return round(sum / counter, 1)


def av_grade_lecturer(list, course):
    sum = 0
    counter = 0
    for lecturer in list:
        for grade in lecturer.grades[course]:
            sum += grade
            counter += 1
    return round(sum / counter, 1)


print(f'Средняя оценка за домашние задания в рамках курса: {av_grade_student([spider_man, scarlet_witch], "Python")}')
print(f'Средняя оценка за лекции всех лекторов в рамках курса: {av_grade_lecturer([iron_man, dr_strange], "Python")}')