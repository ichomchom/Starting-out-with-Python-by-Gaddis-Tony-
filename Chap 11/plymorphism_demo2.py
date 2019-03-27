import animals

def main():
    #Create Mammal obj, Dog obj, Cat obj
    mammal = animals.Mammal('regular animal')
    dog = animals.Dog()
    cat = animals.Cat()

    #Display information each one
    print('Here are some animals and')
    print('the sounds they make.')
    print('-------------------------')
    show_mammal_info(mammal)
    print()
    show_mammal_info(dog)
    print()
    show_mammal_info(cat)
    print()
    show_mammal_info('I am a string')

#show_mammal info func accepts an object as an argument, and calls
    #its show_species and make_sound methods

def show_mammal_info(creature):
    if isinstance(creature, animals.Mammal):
        creature.show_species()
        creature.make_sound()
    else:
        print('That is not a Mammal')

main()
