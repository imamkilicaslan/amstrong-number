while True:
    number = input("write a number \n")

    numLenght = len(number)
    result = 0

    for numberChar in number:
        result += int(numberChar)**numLenght

    if int(number) == result:
        print(number, "is an amstrong number")
    else:
        print(number, "is not an amstrong number")
