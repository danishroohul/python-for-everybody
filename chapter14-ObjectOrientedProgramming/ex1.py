# Create a class named PartyAnimal
class PartyAnimal:
    # Initialize some variable
    x = 0

    # Define a function of a class
    # A function in a class basically shows the characteristcs of an object
    # in this object we are modifying the value of x
    def party(self):
        self.x = self.x + 1
        print("So far",self.x)

# Creating an object named 'an' of class PartyAnimal
# this is similar to l = list()
an = PartyAnimal()

# Telling the object 'an' to run the party code within it
an.party()
an.party()
an.party()

# The party code can also be run like this
# here you can understand how self keyword is replaced by the object name
PartyAnimal.party(an)

# We can also extract the value of variabes in the class like this
print(an.x)
