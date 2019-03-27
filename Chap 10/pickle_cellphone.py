import pickle
import cellphone

#Constant for filename
FILENAME = 'cellphones.dat'

def main():
    #Initialize a var to controll loop
    again = 'y'

    #Open a file
    outfile = open(FILENAME, 'wb')

    #Get data from user
    while again.lower() == 'y':
        #Get cell phone data
        man = input('Enter the manufacturer: ')
        mod = input('Enter the model number: ')
        retail = float(input('Enter the retail price: '))

        #Create cell phone object
        phone = cellphone.CellPhone(man, mod, retail)

        #pickle data
        pickle.dump(phone, outfile)

        #Get more data?
        again = input('Enter more data? (y/n): ')

    #close file
    outfile.close()
    print('The data was written to', FILENAME)

main()
