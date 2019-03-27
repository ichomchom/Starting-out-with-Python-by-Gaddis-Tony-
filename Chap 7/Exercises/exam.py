def main():  
    #Initialize for wrong and correct answers
    correct = 0
    wrong = 0
    key()
    answer()
    check_ans(correct, wrong)

#Def for key 
def key():
    key_file = open('key.txt', 'w')
    #Create the list for key
    key = ['A', 'C', 'A', 'A', 'D', 'B', 'C', 'A',
           'C', 'B', 'A', 'D', 'C', 'A', 'D', 'C', 'B',
           'B', 'D', 'A']

    #Write key list to key_file.txt
    for item in key:
        key_file.write(item + '\n')
    key_file.close()

#Def for answer file
def answer():
    ans_file = open('answer.txt', 'w')
    #Ask user to enter their answers and write answers to answer.txt
    for i in range(20):
        print('Enter your answer for number', i + 1, ': ', end='')
        ans = input()
        ans_file.write(ans + '\n')
    ans_file.close()

#Def for check_ans
def check_ans(correct, wrong):
    key_file = open('key.txt', 'r')
    ans_file = open('answer.txt', 'r')
    
    #Read content of file to list
    key = key_file.readlines()
    ans = ans_file.readlines()
    wrong_ans = []

    #Strip the \n of the letter in the list
    
    for i in range(len(key)):
        key[i] = key[i].rstrip('\n')
        ans[i] = ans[i].rstrip('\n')

        #Check if the answer match with the key
        if key[i] == ans[i]:
            correct += 1
        else:
            wrong += 1
            wrong_ans.append(i + 1)

    if correct >= 15:
        print('You passed.')
        print('You have', correct, 'correct answers.')
        print('You have', wrong, 'wrong answers.')
        print('Your wrong answers are: ', end='')
        print(wrong_ans)
    else:
        print('You failed, try again next time.')
        print('You have', wrong, 'wrong answers.')
        print('Your wrong answers are: ', end='')
        print(wrong_ans)

main()
