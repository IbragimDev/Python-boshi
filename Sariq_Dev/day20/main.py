# Object haqida


class Student:
    def __init__(
        self,
        name,
        lastName,
        born,
    ):
        self.name = name
        self.lastName = lastName
        self.born = born

    def get_name(self):
        return self.name

    def get_age(self, year):
        return year - self.born


student1 = Student("Dima", "Olimov", 2000)
student2 = Student("Olim", "Husanov", 2006)
student3 = Student("Husan", "Hasanov", 2001)
print(student1.get_name())
print(student1.get_age(2023))
print(student2.get_age(2023))
