class PartyAnimal:
    x  = 0

    # Constructors can have additional parameters
    # These can be used to set up instance variables for a particular instance
    def __init__(self,z):
        self.name = z
        print(self.name,"constructed")

    def party(self):
        self.x = self.x + 1
        print("Parties {} attended:".format(self.name),self.x)

    def __del__(self):
        print(self.name,"destructed")

s = PartyAnimal("Sam")
s.party()
s.party()

j = PartyAnimal("John")
j.party()
j.party()
j.party()

s = "Hello"
print(s)
