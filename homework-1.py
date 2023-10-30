from statistics import mean

class Student:

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
        
    def __str__(self):
        return (f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {AverValue.all_courses_average_grade(self)}\nКурсы в процессе изучения: {', '.join(self.courses_in_progress)}\nЗавершенные курсы: {', '.join(self.finished_courses)}")
    
    # Операторы сравнения
    def __gt__(self, other):
        if isinstance(self, Student) and isinstance(other, Student):
            if AverValue.all_courses_average_grade(self) > AverValue.all_courses_average_grade(other):
                return f"Да. Студент {self.name} {self.surname} имеет средний балл больше, чем студент {other.name} {other.surname}."
            else:
                return f"Нет. Студент {self.name} {self.surname} имеет средний балл не лучше, чем студент {other.name} {other.surname}."
        else:
            return 'Нельзя сравнить студента и лектора.'
    def __eq__(self, other):
        if isinstance(self, Student) and isinstance(other, Student):
                if AverValue.all_courses_average_grade(self) == AverValue.all_courses_average_grade(other):
                    return f"Да. Студент {self.name} {self.surname} имеет средний балл, который такой же, как и у студента {other.name} {other.surname}."
                else:
                    return f"Нет. Студент {self.name} {self.surname} имеет средний балл, отличный от балла, который имет студент {other.name} {other.surname}."
        else:
            return 'Нельзя сравнить студента и лектора.'
    def __ne__(self, other):
        if isinstance(self, Student) and isinstance(other, Student):
            if AverValue.all_courses_average_grade(self) != AverValue.all_courses_average_grade(other):
                return f"Да. Студент {self.name} {self.surname} имеет средний балл, отличный от балла, который имет студент {other.name} {other.surname}."
            else:
                return f"Нет. Студент {self.name} {self.surname} имеет средний балл, который такой же, как и у студента {other.name} {other.surname}."
        else:
            return 'Нельзя сравнить студента и лектора.'
    def __lt__(self, other):
        if isinstance(self, Student) and isinstance(other, Student):
            if AverValue.all_courses_average_grade(self) < AverValue.all_courses_average_grade(other):
                return f"Да. Студент {self.name} {self.surname} имеет средний балл меньше, чем студент {other.name} {other.surname}."
            else:
                return f"Нет. Студент {self.name} {self.surname} имеет не меньше, чем студент {other.name} {other.surname}."
        else:
            return 'Нельзя сравнить студента и лектора.'
    

class Mentor:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class AverValue():

    def all_courses_average_grade(self):
        if len(self.grades) != 0:
            av_val = 0
            for course in self.grades:
                av_val += mean(self.grades.get(course)) 
                
            return round(av_val/len(self.grades), 1)
        else:
            return 0.0
    
    def one_course_average_grade(self, course):
        if len(self.grades) != 0:
            av_val = mean(self.grades.get(course)) 
            return round(av_val, 1)
        else:
            return 0.0


class Lecturer(Mentor):

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.courses_attached = []

    def __str__(self):
        return (f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {AverValue.all_courses_average_grade(self)}")

    # Операторы ссравнения
    def __gt__(self, other):
        if isinstance(self, Lecturer) and isinstance(other, Lecturer):
            if AverValue.all_courses_average_grade(self) > AverValue.all_courses_average_grade(other):
                return f"Да. Лектор {self.name} {self.surname} имеет средний балл больше, чем лектор {other.name} {other.surname}."
            else:
                return f"Нет. Лектор {self.name} {self.surname} имеет средний балл не лучше, чем лектор {other.name} {other.surname}."
        else:
            return 'Нельзя сравнить лектора и студента.'
    def __eq__(self, other):
        if isinstance(self, Lecturer) and isinstance(other, Lecturer):
            if AverValue.all_courses_average_grade(self) == AverValue.all_courses_average_grade(other):
                return f"Да. Лектор {self.name} {self.surname} имеет средний балл, который такой же, как и у лектора {other.name} {other.surname}."
            else:
                return f"Нет. Лектор {self.name} {self.surname} имеет средний балл, отличный от балла, который имет лектор {other.name} {other.surname}."
        else:
            return 'Нельзя сравнить лектора и студента.'
    def __ne__(self, other):
        if isinstance(self, Lecturer) and isinstance(other, Lecturer):
            if AverValue.all_courses_average_grade(self) != AverValue.all_courses_average_grade(other):
                return f"Да. Лектор {self.name} {self.surname} имеет средний балл, отличный от балла, который имет лектор {other.name} {other.surname}."
            else:
                return f"Нет. Лектор {self.name} {self.surname} имеет средний балл, который такой же, как и у лектора {other.name} {other.surname}."
        else:
            return 'Нельзя сравнить лектора и студента.'
    def __lt__(self, other):
        if isinstance(self, Lecturer) and isinstance(other, Lecturer):
            if AverValue.all_courses_average_grade(self) < AverValue.all_courses_average_grade(other):
                return f"Да. Лектор {self.name} {self.surname} имеет средний балл меньше, чем лектор {other.name} {other.surname}."
            else:
                return f"Нет. Лектор {self.name} {self.surname} имеет средний балл не меньше, чем лектор {other.name} {other.surname}."
        else:
            return 'Нельзя сравнить лектора и студента.'


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
        return (f"Имя: {self.name}\nФамилия: {self.surname}")


# Функция подходит и для студентов, и для лекторов
def count_av_value_of_course(people_list, course_name):
    counter = 0
    counter_sudent = 0
    for person in people_list:
        if course_name in person.grades:
            counter += AverValue.one_course_average_grade(person, course_name)
            counter_sudent += 1
    if counter_sudent > 0:
        return round(counter/counter_sudent, 1)
    else:
        return 0.0



# Создаем 2 студента
student_1 = Student('Harry','Maguire', 'Male')
student_1.courses_in_progress += ['Python', 'Git']
student_1.finished_courses += ['Введение']

student_2 = Student('Marry', 'Jane', 'Female')
student_2.courses_in_progress += ['Python', 'Java']
student_2.finished_courses += ['C++']

# Создаем 2 ревьюера
reviewer_1 = Reviewer('Some', 'Buddy')
reviewer_1.courses_attached += ['Python', 'Git']

reviewer_2 = Reviewer('Some', 'Buddy')
reviewer_2.courses_attached += ['Python', 'Java']

# Создаем 2 лектора
lecturer_1 = Lecturer('Migel', 'Ohara')
lecturer_1.courses_attached += ['Python', 'Git']

lecturer_2 = Lecturer('Miles', 'Morales')
lecturer_2.courses_attached += ['Python', 'Java']

# Оценивание студентов и лекторов
print('-'*40)
reviewer_1.rate_hw(student_1, 'Python', 9)
reviewer_1.rate_hw(student_1, 'Git', 9)
reviewer_2.rate_hw(student_1, 'Python', 10)
reviewer_2.rate_hw(student_2, 'Python', 8)
reviewer_2.rate_hw(student_2, 'Python', 8)
reviewer_1.rate_hw(student_2, 'Java', 8) #Не может сделать, т.к. у revieewer_1 нет Java

student_1.rate_lecturer(lecturer_1, 'Git', 10)
student_1.rate_lecturer(lecturer_2, 'Python', 10)
student_1.rate_lecturer(lecturer_2, 'Java', 10) #Не может сделать, т.к. у student_1 нет Java

student_2.rate_lecturer(lecturer_1, 'Python', 9)
student_2.rate_lecturer(lecturer_1, 'Python', 7)
student_2.rate_lecturer(lecturer_2, 'Python', 8)
student_2.rate_lecturer(lecturer_2, 'Java', 7) 

print('Оценки студентов:')
print(student_1.name, student_1.surname, student_1.grades)
print(student_2.name, student_2.surname, student_2.grades, '\n')
print('Оценки лекторов:')
print(lecturer_1.name, lecturer_1.surname, lecturer_1.grades)
print(lecturer_2.name, lecturer_2.surname, lecturer_2.grades)
print('\n'+'-'*40)

# Printing студента, лектора, ревьюера
print('Printing студента, лектора, ревьюера:\n')
print(student_1, '\n')
print(lecturer_1, '\n')
print(reviewer_1, '\n')
print('-'*40)

# Сравнение людей
print('Сравнение людей\n')
print('Студенты:')
print(f"{AverValue.all_courses_average_grade(lecturer_1)} == {AverValue.all_courses_average_grade(lecturer_2)}", student_1 == student_2)
print(f"{AverValue.all_courses_average_grade(lecturer_1)} != {AverValue.all_courses_average_grade(lecturer_2)}", student_1 != student_2)
print(f"{AverValue.all_courses_average_grade(lecturer_1)} > {AverValue.all_courses_average_grade(lecturer_2)}", student_1 > student_2)
print(f"{AverValue.all_courses_average_grade(lecturer_1)} < {AverValue.all_courses_average_grade(lecturer_2)}", student_1 < student_2, '\n')


print('Лекторы:')
print(f"{AverValue.all_courses_average_grade(lecturer_1)} == {AverValue.all_courses_average_grade(lecturer_2)}", lecturer_1 == lecturer_2)
print(f"{AverValue.all_courses_average_grade(lecturer_1)} != {AverValue.all_courses_average_grade(lecturer_2)}", lecturer_1 != lecturer_2)
print(f"{AverValue.all_courses_average_grade(lecturer_1)} > {AverValue.all_courses_average_grade(lecturer_2)}", lecturer_1 > lecturer_2)
print(f"{AverValue.all_courses_average_grade(lecturer_1)} < {AverValue.all_courses_average_grade(lecturer_2)}", lecturer_1 < lecturer_2)
print( '\n'+'-'*40)

print('Если сравнить студента и лектора:')
print(f"{student_1.name} {student_1.surname} == {lecturer_2.name} {lecturer_2.surname}.", student_1 == lecturer_2)
print(f"{lecturer_1.name} {lecturer_1.surname} != {student_2.name} {student_2.surname}.", lecturer_1 != student_2)
print( '\n'+'-'*40)


# Подсчет среднего балла
print('Подсчет среднего балла:\n')

print('Студенты:')
print(f'Python - {count_av_value_of_course([student_1, student_2], "Python")}')
print(f'Git - {count_av_value_of_course([student_1, student_2], "Git")}')
print(f'Java - {count_av_value_of_course([student_1, student_2], "Java")}')

print('\nЛекторы:')
print(f'Python - {count_av_value_of_course([lecturer_1, lecturer_2], "Python")}')
print(f'Git - {count_av_value_of_course([lecturer_1, lecturer_2], "Git")}')
print(f'Java - {count_av_value_of_course([lecturer_1, lecturer_2], "Java")}')
print('-'*40)