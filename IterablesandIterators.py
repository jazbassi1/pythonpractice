from itertools import combinations

n = int(input())
l = list(input().split())
k = int(input())
c = list(combinations(l, k)) # combination of lists
r = [i for i in c if 'a' in i]
print('%.3f'%(len(r)/ len(c)))