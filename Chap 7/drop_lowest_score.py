def main():
    #Get test score from user
    scores = get_scores()

    #Get total of test scores
    total = get_total(scores)

    #Get the lowest test score
    lowest = min(scores)

    #Substract the lowest from total
    total -= lowest

    #Cal avg, -1 because drop 1 lowest
    avg = total / (len(scores) - 1)

    #Display avg
    print('The average, with the lowest score dropped is:', avg)
    
def get_scores():
    #Create empty list
    test_scores = []
    
    #Create a var control loop
    again = 'y'

    #Get values from user
    while again == 'y' :
        #Get score and add to list
        num = int(input('Enter a test score: '))
        test_scores.append(num)

        #Continue?
        print('Do you want to add another number?')
        again = input('y = yes, anything else = no: ')
        print()

    #return list
    return test_scores

def get_total(value_list):
    #Create var as accumulator
    total = 0.0

    #Cal the total
    for num in value_list:
        total += num

    return total

main()        

    
