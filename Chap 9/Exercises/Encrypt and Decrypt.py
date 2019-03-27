def main():
    #Create dictionary
    codes = {'A' : 'B',
             'B' : 'C',
             'C' : 'D',
             'D' : 'E',
             'E' : 'F',
             'F' : 'G',
             'G' : 'H',
             'H' : 'I',
             'I' : 'J',
             'J' : 'K',
             'K' : 'L',
             'L' : 'M',
             'M' : 'N',
             'N' : 'O',
             'O' : 'P',
             'P' : 'Q',
             'Q' : 'R',
             'R' : 'S',
             'S' : 'U',
             'U' : 'V',
             'V' : 'W',
             'W' : 'X',
             'X' : 'Y',
             'Y' : 'Z',
             'Z' : 'A'}
    #open the file code.txt to read
    input_file = open('code.txt', 'r')

    #Create enccrypt.txt file to write
    encrypt_file = open('encrypt.txt', 'w')

    
    decrypt_file = open('decrypt.txt', 'w')

    #read elements in the code.txt file
    file_contents = input_file.read()

    encrypt(file_contents, codes, encrypt_file)
    decrypt(codes, decrypt_file)
    
    input_file.close()
    
    decrypt_file.close()

#Encrypt
def encrypt(msg, codes, encrypt_file):
    for char in msg:
        encrypt_file.write(codes[char])
    encrypt_file.close()
    
#Decrypt
def decrypt(codes, decrypt_file):
    infile = open('encrypt.txt', 'r')
    content = infile.read()
    
    for char in content:
        decrypt_file.write(codes[char])
    infile.close()
main()        
