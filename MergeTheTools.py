def merge_the_tools(string, k):
    l = []
    m = 0
    for i in range(len(string)// k):
        l.append(string[m:m+k])
        m+=k
    # print(l)
    for v in l:
#       print(list(v))
#       print(dict.fromkeys(list(v)))
#       print(dict.fromkeys(list(v), 1)) # convert list to dictionary
#       print(dict.fromkeys(list(v)).keys())
#       print(list(dict.fromkeys(list(v)).keys())) # converting to list
        print(''.join(list(dict.fromkeys(list(v)).keys()))) # join list with dictionary


string, k = input(), int(input())
merge_the_tools(string, k)
