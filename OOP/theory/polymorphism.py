# same function name, but different behavior in different classes

class cat:
    def voice(self):
        print("Cat says meoww")

class dog:
    def voice(self):
        print("dog says Bhawww")

class cow:
    def voice(self):
        print("Cow says Mooooooooo")

a1 = cat()
a2 = dog()
a3 = cow()

anm = [a1, a2, a3]

for i in anm:
    i.voice()