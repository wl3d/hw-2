class Student:
    def __init__(self, first_name, last_name, birth_date, height=160):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.height = height

first_student = Student("Ivan", "Ivanov", "12.02.2010", 186)
second_student = Student("Petr", "Petrov", "28.06.2009", 220)

print(first_student.first_name, first_student.last_name, first_student.birth_date, first_student.height)
print(second_student.first_name, second_student.last_name, second_student.birth_date, second_student.height)