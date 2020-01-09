# This example shows the usage of constructors and destructors

# Create a class named PartyAnimal
class PartyAnimal:
    x = 0

    # Define a constructor function
    def __init__(self):
        print("object with value {} is constructed".format(self.x))

    # Party function
    def party(self):
        self.x = self.x + 1
        print("So far", self.x)

    # Destructor function
    def __del__(self):
        print("object with value {} is destructed".format(self.x))

# When an object is created, constructor is called
an = PartyAnimal()

an.party()
an.party()

# When an object is replaced/ destroyed, destructor is called
an = 4

print(an)
