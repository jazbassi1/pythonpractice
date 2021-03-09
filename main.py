def reverseWordOrder():
    userInput = input("Please enter string of words \n")
    #print(userInput) - printing user input
    wordList = userInput.split(' ')
    # print(wordList) ' ' - prints the string as a list

    count = len(wordList)
    count = count - 1 # initially starts count at 3

    while count >= 0:

        print(wordList[count], end=' ') #end parameter with ' ' blank space to not give new lines for each iteration
        count = count - 1


reverseWordOrder()