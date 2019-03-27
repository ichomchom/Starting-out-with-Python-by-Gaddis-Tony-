def main():
    #Open file frequency.txt to read
    infile = open('frequency.txt', 'r')

    #Read data into conten var
    content = infile.read()

    #split space and put data into list
    list = content.split()

    #close file
    infile.close

    #We don't want . , ' in word
    unwanted_chars = ". , '"

    #create empty dictionary
    frequency = {}

    #Go through the list
    for raw_word in list:

        #Split the unwatned char from word
        word = raw_word.strip(unwanted_chars)

        #Check if word not in frequency or not if not + 1
        if word not in frequency:
            frequency[word] = 0
        frequency[word] += 1

    #print dictionary
    for word in frequency:
        print(word, frequency[word])
main()        
