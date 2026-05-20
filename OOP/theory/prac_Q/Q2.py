# Create class Creator with attributes (name, username). Add method bio().

class Creator:

    def __init__(self, name, username):
        self.name = name
        self.username = username
        
        
    def bio(self):
        print("My name is ", self.name, "and my username is ", self.username)


bio = Creator("Bishal", "Bula_li_apni_maut")

bio.bio()