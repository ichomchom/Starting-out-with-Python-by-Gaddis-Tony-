def main():
    infile = open('unique.txt', 'r')
    content = infile.read()
    unique_set = set()
    for char in content:
        unique_set.add(char)
    print(unique_set)

main()
