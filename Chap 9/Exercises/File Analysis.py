def main():
    #Open file1 and file2 to read
    infile1 = open('file1.txt', 'r')
    infile2 = open('file2.txt', 'r')

    content1 = infile1.read()
    content2 = infile2.read()

    #unwanted chars
    unwanted_chars = "' , . " ""


    #create empty set
    set1 = set()
    set2 = set()

    #split space of the sentence and put every word in to list
    list1 = content1.split()
    list2 = content2.split()

    #Strip the unwanted chars in element and put it into set
    for var in list1:
        set1.add(var.strip(unwanted_chars))
    for var in list2:
        set2.add(var.strip(unwanted_chars))

    #print unique words
    unique_words(set1, set2)

    #words appear in both files
    same_words(set1, set2)

    #words appear in first file but not second
    first_file(set1, set2)

    #words appear in second file but not first
    second_file(set1, set2)

    #words appear either both files
    either_files(set1, set2)

def unique_words(set1, set2):
    print('Unique words in file1: ')
    for word in set1:
        print(word)
    print('\n')
    print('Unique words in file2: ')
    for word in set2:
        print(word)

def same_words(set1, set2):
    print('\n')
    print('Words that appear in both files: ')
    for word in set1.intersection(set2):
        print(word)

def first_file(set1, set2):
    print('\n')
    print('Words that appear in first file but not second file: ')
    for word in set1.difference(set2):
        print(word)

def second_file(set1, set2):
    print('\n')
    print('Words that appear in second file but not first file: ')
    for word in set2.difference(set1):
        print(word)

def either_files(set1, set2):
    print('\n')
    print('Word that appear either first or second file: ')
    for word in set1.union(set2):
        print(word)
  
main()
