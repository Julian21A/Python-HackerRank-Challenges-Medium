import itertools as it

a = int(input())
list1 =(list(map(str,input().split())))
b = int(input())

combinaciones=list(it.combinations(list1,b))
repeticion=filter(lambda c: 'a' in c, combinaciones)
output=(len(list(repeticion)))/len(combinaciones)
print("{0:.3}".format(output))
        