def main():
    char_list = [' ', ',', '.', '?', '0', '1', '2', '3',
                 '4', '5', '6', '7', '8', '9', 'A', 'B',
                 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'F',
                 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
                 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    code_list = [' ', '--..--', '.-.-.-', '..--..', '-----',
                 '.----', '..---', '...--', '....-', '.....',
                 '-....', '--...', '---..', '----.', '.-',
                 '-...', '-.-.', '-..', '.', '..-.', '--.',
                 '....', '..', '.---', '-.-', '.-..', '--',
                 '-.', '---', '.--.', '--.-', '.-.', '...',
                 '-', '..-', '...-', '.--', '-..-', '-.-', '--..']
    
    string = input('Please enter phase to convert to morse code: ').upper()
    for char in string:
        for i in range(0, len(char_list)):
            if char == char_list[i]:
                print(code_list[i],' ', end='')  

main()
