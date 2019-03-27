import pickle

#main
def main():
    again = 'y' #Control loop repetition

    #Open file for binary writing
    output_file = open('info.dat', 'wb')

    #Get data until user want to stop
    while again.lower() == 'y':
        #Get data about a person and save it
        save_data(output_file)

        #Does the user want to enter more data?
        again = input('Enter more data? (y/n): ')

    #Close file
    output_file.close()

#Save_data func gets data about a person, store in dictionary
#then pickles the dictionary to the specified file
def save_data(file):
    #Create empty dict
    person = {}

    #Get data for person and store
    person['name'] = input('Name: ')
    person['age'] = input('Age: ')
    person['weight'] = float(input('Weight: '))

    #pickle the dictionary
    pickle.dump(person, file)

main()    
