#Program count vowles and consonants in a sentence
def main():
    
    string = input('Enter a sentence: ')
    print('Number of vowel in the sentences are: '+ str(vowel(string)))
    vowelCounter = (vowel(string))
    print('Number of consonant in the sentences are: '+ str(consonant(string, vowelCounter)))

#Vowel func. check if the string has any vowel add 1 to counter    
def vowel(string):
    counter = 0
    for char in string:
        if char == 'u':
            counter += 1
        elif char == 'e':
            counter += 1
        elif char == 'o':
            counter += 1
        elif char == 'a':
            counter += 1
        elif char == 'i':
            counter += 1
        else:
            continue
    return counter

#Cosonant func. pass the string and vowel counter as parameter
#check space in the string, the length of sentence - (vowel + space) = cosonant
def consonant(string, counter):
    space = 0
    consonant = 0
    for char in string:
        if char == ' ':
            space += 1
        else:
            continue
    consonant = len(string) - (counter + space)
    return consonant

main()
