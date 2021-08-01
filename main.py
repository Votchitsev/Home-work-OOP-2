class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course \
                in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def av_grades(self):
        if self.grades == {}:
            return 'Не оценивается'
        else:
            s = []
            for i in self.grades.values():
                s += i
            return round((sum(s) / len(s)), 1)

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Ошибка')
            return
        else:
            return self.av_grades() < other.av_grades()

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашнее задание: {self.av_grades()}\n' \
               f'Курсы в процессе обучения: {", ".join(self.courses_in_progress)}\n' \
               f'Завершенные курсы: {", ".join(self.finished_courses)}'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def av_grades(self):
        if self.grades == {}:
            return 'Не оценивается'
        else:
            s = []
            for i in self.grades.values():
                s += i
            return sum(s) / len(s)

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Ошибка')
            return
        else:
            return self.av_grades() < other.av_grades()

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.av_grades()} '


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if not isinstance(student, Student) or course not in self.courses_attached or course not in \
                student.courses_in_progress:
            return 'Ошибка'
        else:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'


student_1 = Student('Vasily', 'Pupkin', 'M')
student_2 = Student('Karl', 'Hlamkin', 'M')
lecturer_1 = Lecturer('Sasha', 'Pupkina')
lecturer_2 = Lecturer('Sergey', 'Vorobey')
reviewer_1 = Reviewer('Dima', 'Mitin')
reviewer_2 = Reviewer('Andrey', 'Sergeev')

lecturer_1.courses_attached += ['Python', 'Java Script']
lecturer_2.courses_attached += ['PHP', 'C++']

student_1.courses_in_progress += ['Python']
student_2.finished_courses += ['Java Script']
student_1.courses_in_progress += ['PHP']
student_2.courses_in_progress += ['C++']

student_1.rate_lecturer(lecturer_1, 'Python', 7)
student_2.rate_lecturer(lecturer_2, 'C++', 5)
student_1.rate_lecturer(lecturer_2, 'PHP', 2)
student_1.rate_lecturer(lecturer_1, 'Python', 6)

reviewer_1.courses_attached += ['Python', 'Java Script']
reviewer_2.courses_attached += ['PHP', 'C++']
reviewer_2.rate_hw(student_1, 'PHP', 9)
reviewer_2.rate_hw(student_1, 'PHP', 7)
reviewer_2.rate_hw(student_2, 'C++', 9)


def av_grade_of_homework(ls, name):
    list_of_grades = []
    for i in ls:
        list_of_grades += (i.grades.get(name, []))
    if len(list_of_grades) != 0:
        return round((sum(list_of_grades) / len(list_of_grades)), 1)
    else:
        return 'Ошибка: Отсутствуют оценки по данным предметам.'


def av_grade_lecturers(ls, name):
    list_of_grades = []
    for i in ls:
        list_of_grades += (i.grades.get(name, []))
    if len(list_of_grades) != 0:
        return round((sum(list_of_grades) / len(list_of_grades)), 1)
    else:
        return 'Ошибка: Отсутствуют оценки по данным предметам.'


list_of_students = [student_1, student_2]
name_of_course = 'C++'
print(av_grade_of_homework(list_of_students, name_of_course))

list_of_lecturers = [lecturer_1, lecturer_2]
print(av_grade_lecturers(list_of_lecturers, name_of_course))

print(student_1 < student_2)
print(lecturer_1 > lecturer_1)
