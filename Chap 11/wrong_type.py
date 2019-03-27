def main():
    #Pass a string to show_mammal_info
    show_mammal_info('I am a string')

def show_mammal_info(creature):
    creature.show_species()
    creature.make_sound()

main()
