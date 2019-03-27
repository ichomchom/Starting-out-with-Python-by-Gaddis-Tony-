def main():
    date_string = '11/26/2018'

    #split date
    date_list = date_string.split('/')

    #Display each piece
    print('Month:', date_list[0])
    print('Day:', date_list[1])
    print('Year:', date_list[2])

main()
