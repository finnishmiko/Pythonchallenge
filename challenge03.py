'''
Python challenge 3
'''


def main():
    d = []
    counter = 0

    # read text file
    with open("challenge03.txt", "r") as myfile:
        data = myfile.read().replace('\n', '')
        print(data)

    i = 0
    index = 0
    result = []
    for x in data:
        if x.isupper() == True and i < 3:
            i += 1
        elif i == 4 and x.isupper() == True:
            i = 3
        elif i == 3 and x.isupper() == False:
            i = 5
        elif i > 4 and x.isupper() == True:
            i += 1
        else:
            i = 0

        if i == 8:
            if data[index-7].isupper() == False and data[index+1].isupper() == False:
                print(data[index-7:index+2])
                result += data[index-3]
                counter += 1
            i = 3

        prev = x
        index += 1
    print("Total: ", counter)
    print(result)


if __name__ == '__main__':
    main()
