# child class got the properties & methods of parent class is called inheritance.
# avoids repeating code



class parent:
    def surname(self):                 
        print("Surname is Sarma")  

class child1(parent):    
    def name(self):
        print("Name is child1")
class child2(parent):
    def name(self):
        print("Name is child2")
class child3(parent):
    def name(self):
        print("Name is child3")

c1 = child1()
c2 = child2()
c3 = child3()

c1.name()
c1.surname()

c2.name()
c2.surname()

c3.name()
c3.surname()
