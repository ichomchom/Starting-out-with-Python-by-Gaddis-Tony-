def main():
    #Get the num of emp records to creat
    num_emps = int(input('How many employee records do you want to creat? '))

    #Open file for writing
    emp_file = open('employees.txt', 'w')

    #Get each employee's data and write it to file
    for count in range(1, num_emps + 1):
        #Get the data for an employee
        print('Enter data for employee #', count, sep='')
        name = input('Name: ')
        id_num = input('ID number: ')
        dept = input('Department: ')

        #Write tha data as a record to the file
        emp_file.write(name + '\n')
        emp_file.write(id_num + '\n')
        emp_file.write(dept + '\n')

        #Display blank line
        print()

    #Close file
    emp_file.close()
    print('Employee records written to employees.txt.')

main()
