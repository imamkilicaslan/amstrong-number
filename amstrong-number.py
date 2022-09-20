while True:
    number = input("write a number \n")

    numLenght = len(number)
    amstrongNumberQuestioning = 0
    for numberChar in number:
        amstrongNumberQuestioning += int(numberChar)**numLenght

    if int(number) == amstrongNumberQuestioning:
        print(amstrongNumberQuestioning, "is an amstrong number")
    else:
        print(number, "is not an amstrong number")
