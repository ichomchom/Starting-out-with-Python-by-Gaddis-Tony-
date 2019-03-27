def main():
    list = [ 1, 43, 5, 4, 6, 7, 34]
    num = 5

    func(list, num)

def func(list, num):
    for i in range(len(list)):
        if num < list[i]:
            print(list[i])

main()
