import employee

def main():
    #Create empty list to hold the entry
    entry = []
    
    #Create loop to ask user input 3 persons information
    for count in range(0, 3):
        name = input('Enter name: ')
        id_num = input('Enter ID Number: ')
        dept = input('Enter Department: ')
        title = input('Enter Title: ')

        #cearte entry
        entry.append(employee.Employee(name, id_num, dept, title))
        print()
        
    for info in entry:
        print(info)
        print()
main()

