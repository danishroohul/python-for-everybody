# Create a class named PartyAnimal
class PartyAnimal:
    x = 0

    # Define a constructor function
    def __init__(self,z):
        self.name = z
        print(self.name,"constructed")

    def party(self):
        self.x = self.x + 1
        print("Parties {} attended:".format(self.name),self.x)

    def __del__(self):
        print(self.name,"destructed")

# To inherit a class, put the class insidde paranthesis
class FootballFan(PartyAnimal):
    points = 0

    def touchdown(self):
        self.points = self.points + 7
        print(self.name, "points", self.points)

s = PartyAnimal("Sally")
s.party()

# Object j can run functions from class PartyAnimal too
j = FootballFan("John")
j.touchdown()
j.party()
