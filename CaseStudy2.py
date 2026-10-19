# Bhavana Sri 2600308 - Case Study 2
class Student:
    def __init__(self, roll, name, marks):
        self.roll = roll
        self.name = name
        self.marks = marks
    def display(self):
        print(f"Roll: {self.roll}, Name: {self.name}, Marks: {self.marks}")
    def grade(self):
        if self.marks >= 90:
            return "A"
        elif self.marks >= 75:
            return "B"
        else:
            return "C"

s1 = Student(2600308, "Bhavana Sri", 85)
s1.display()
print("Grade:", s1.grade())
