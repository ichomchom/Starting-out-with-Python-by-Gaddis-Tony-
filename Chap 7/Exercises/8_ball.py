import random

def main():
    #Open file 
    file = open('8_ball_responses.txt', 'r')

    #Read the first line of the file
    line = file.readline()

    #Create list
    responses = []

    #Do loop to read the rest of the file by checking if the line empty or not
    while line != '':
        #Strip \n from the word
        line = line.rstrip('\n')

        #Add to the list
        responses.append(line)

        #Read next line
        line = file.readline()

    #Close file
    file.close()
    
    answer(responses)

#Run the loop for user to ask question
def answer(responses):
    more = 'y'
    input('what is your question?')
    while more == 'y' or more == 'Y':
        print(responses[random.randint(0, len(responses) - 1)])    
        more = input('Anoter question? Press y \n')
main()    
