class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def CalculateGrade(self):
        if self.marks>90:
            return "A"
        elif self.marks>=75:
            return "B"
        else:
            return "F"
    
    def display(self):
        grade = self.CalculateGrade()
        print("Name:", self.name)
        print("Roll No:", self.roll_no)
        print("Marks:", self.marks)
        print("Grade:", grade)

s = Student("Osman",67,90)
s.display()

