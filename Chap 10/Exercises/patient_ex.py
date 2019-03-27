import patient

def main():

    print_info(get_patient(),get_procedure())

#Get information of patient
def get_patient():
    
    firstname = input("Enter patient's first name: ")
    midname = input("Enter patient's middle name: ")
    lastname = input("Enter patient's last name: ")
    address = input("Enter patient's address: ")
    city = input("Enter patient's city: ")
    state = input("Enter patient's state: ")
    zipcode = input("Enter patient's zip code: ")
    phone = input("Enter patient's phone number: ")
    emer_name = input("Enter patient's emergency contact name: ")
    emer_phone = input("Enter patient's emergency contact phone number: ")
    print()
    
    #Create patient object and add infor to the object
    patient_info = patient.Patient(firstname, midname, lastname,
                 address, city, state, zipcode, phone, emer_name,
                 emer_phone)

    return patient_info

#Get information of the procedures   
def get_procedure():
    #Create procedures empty list
    proc = []
    
    #Create loop to enter 3 procedures
    for count in range(0, 3):
        name = input('Enter procedure name: ')
        date = input('Enter date: ')
        pract = input('Enter Practitioner: ')
        price = int(input('Enter the charge: '))
        print()
        #Create procedure object 
        proc.append(patient.Procedure(name, date, pract, price))

    return proc

#Print patient and procedures information
def print_info(patient_info, proc):
    print(patient_info)
    print()
    #Print 3 procedures
    for info in proc:
        print(info)
        print()
    print('Total charge: ', proc[0].get_price() + proc[1].get_price() + proc[2].get_price())


main()
