import pickle

#main
def main():
    end_of_file = False #Indicate end of file

    #open file for binary reading
    input_file = open('info.dat', 'rb')

    #Read to the end of file
    while not end_of_file:
        try:
            #Unpikcle the next object
            person = pickle.load(input_file)

            #Display
            display_data(person)
        except EOFError:
            #Set the flag to indicate end of file
            end_of_file = True
    #close file
    input_file.close()

#Display func
def display_data(person):
    print('Name:', person['name'])
    print('Age:', person['age'])
    print('Weight:', person['weight'])
    print()

main()    
