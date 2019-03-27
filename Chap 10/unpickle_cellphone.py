import pickle
import cellphone

#Constant for filename
FILENAME = 'cellphones.dat'

def main():
    end_of_file = False

    #Open file
    infile = open(FILENAME, 'rb')

    #Read to the end of file
    while not end_of_file:
        try:
            #Unpickle object
            phone = pickle.load(infile)

            #Display cellphone data
            display_data(phone)

        except EOFError:
            #Set flag to indicate end of file
            end_of_file = True

    #close file
    infile.close()

def display_data(phone):
    print('Manufacturer:', phone.get_manufact())
    print('Model Number:' , phone.get_model())
    print('Retail Price: $', format(phone.get_retail_price(), '.2f'), sep='')
    print()

main()
