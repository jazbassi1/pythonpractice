def happiness(inputArr, posSet, negSet):  #inputs set for array
    happiness = 0
    for value in inputArr:  # loop over inputArray
        if value in posSet:  # if in positive set increase happiness
            happiness += 1
        if value in negSet:  # if in negative set decrease happiness
            happiness -= 1

    return happiness


# read inputs

n, m = str(input()).split(' ')
inputArr = list(str(input()).split(' '))  # list of array
posSet = set((input()).split(' '))
negSet = set((input()).split(' '))

print(happiness(inputArr, posSet, negSet))
