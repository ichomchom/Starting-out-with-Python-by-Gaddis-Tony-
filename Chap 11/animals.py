class Mammal:

    def __init__(self, species):
        self.__species = species

    #show_species method display message indicating the mammal's species
    def show_species(self):
        print('I am a', self.__species)

    #make_sound method is the mammal's way of making sound
    def make_sound(self):
        print('Grrrr')

#Dog class is a subclass of Mammal class
class Dog(Mammal):

    #The __init__ method class the superclass's
    #__init__ method passing 'Dog' as the species
    
    def __init__(self):
        Mammal.__init__(self, 'Dog')

    def make_sound(self):
        print('Woof! Woof!')
class Cat(Mammal):

    def __init__(self):
        Mammal.__init__(self, 'Cat')

    def make_sound(self):
        print('Meow')
