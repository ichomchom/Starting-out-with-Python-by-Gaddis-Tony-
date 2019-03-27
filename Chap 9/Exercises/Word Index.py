def main():

    #Open Kennedy file to read
    infile = open('Kennedy.txt', 'r')

    #Create empty list to read content of the file
    content = []

    #Empty dictionary
    index = {}
    
    #Read every line on the file and split them by word
    for line in infile:
        content.append(line.split())

    #Since the list is 2D array, have to go throuhg each array
    #Since i be the line and j be the word in every line
    for i in range(0, len(content)):
        for j in range(0, len(content[i])):

            #Create temp list to put more value into one key
            temp = []

            #If the word not in dictionary yet
            #Add it to dictionary
            if content[i][j] not in index:

                #Add value line into word
                #Since list starts at 0, so we +1
                temp.append(i+1)
                index[content[i][j]] = temp
                
            else:

                #Since word already in dictionary we just
                #append the new value into dictionary
                index[content[i][j]].append(i+1)

    #Print key and value of dictionary                
    for key, val in index.items():
        print(key, val)

main()
