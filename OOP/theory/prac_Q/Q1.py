# Create class Student with name, class, marks. Add method get_percentage().

class Student:
    def __init__(self, name, cls, marks):
        self.name = name
        self.cls = cls
        self.marks = marks
    
    def percentage(self):
        count = 0
        sum = 0
        for i in self.marks:
            sum += i
            count += 1
        perc = sum/count
        print("Name is :" , self.name, ". Class is ", self.cls, ". Percentage is :", perc)

s1 = Student("Bishal", "MCA", [80,80,90,70,80])
s1.percentage()
