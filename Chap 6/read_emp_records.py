def main():
    #Open the employees.txt file
    emp_file = open('employees.txt', 'r')

    #Read the first line from file
    name = emp_file.readline()

    #If a field was read, continue
    while name != '':
        #Read ID number field
        id_num = emp_file.readline()

        #Read Department
        dept = emp_file.readline()

        #Strip the new lines
        name = name.rstrip('\n')
        id_num = id_num.rstrip('\n')
        dept = dept.rstrip('\n')

        #Display
        print('Name:', name)
        print('ID:', id_num)
        print('Department:', dept)
        print()

        #Read the name for the next record
        name = emp_file.readline()

    emp_file.close()

main()
