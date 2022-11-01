class Person:
    def __init__(self, first_name, last_name, age) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}, {self.age} years old'


class Student(Person):
    def __init__(self, first_name, last_name, age, group) -> None:
        super().__init__(first_name, last_name, age)
        self.group = group

    def __str__(self) -> str:
        return f'{super().__str__()} from {self.group} group'

class Teacher(Person):
    def __init__(self, first_name, last_name, age, subject) -> None:
        super().__init__(first_name, last_name, age)
        self.subject = subject

    def __str__(self) -> str:
        return f'{super().__str__()} teaching {self.subject}'


if __name__ == '__main__':
    person = Person('Dima', 'Shtrikker', 20)
    student = Student('Oleh', 'Borysevych', 19, 'KA-04')
    teacher = Teacher('Olena', 'Stepanivna', 36, 'Maths')

    print(f"Hi, I'm {person}.")
    print(f"Hi, I'm {student}.")
    print(f"Hi, I'm {teacher}.")
