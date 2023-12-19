# Задание 4
class Student:
    school = "111 School"

    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def get_info(self):
        return f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}, School: {self.school}"

    @staticmethod
    def is_teenager(age):
        return age > 12 and age < 18

    @classmethod
    def get_school_name(self):
        return self.school


# Example usage
student1 = Student("Alice", 15, 10)
print(student1.get_info())

print(Student.is_teenager(14))

print(Student.get_school_name())