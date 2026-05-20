# Add method to increase salary by a percentage.

class Emp:
    def __init__(self, name, current_salary):
        self.name = name
        self.current_salary = current_salary
        
    def sal_inc(self):
        new_salary = self.current_salary + (self.current_salary/100)
        print("Mr.", self.name,", your salary",self.current_salary  ,"just increased by 1% and it's", int(new_salary),"now.")


emp = Emp("Bishal", 30000)
emp.sal_inc()