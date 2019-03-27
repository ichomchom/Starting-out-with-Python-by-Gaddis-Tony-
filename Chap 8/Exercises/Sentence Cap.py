def main():
    string = input('Enter your string: ')  
    string_list = string.split('. ')
    sentences = [sentence[0].upper() + sentence[1:] for sentence in string_list]
    string2 = '. '.join(sentences)
    print(string2)
main()
 
