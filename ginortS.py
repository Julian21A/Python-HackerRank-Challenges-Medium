up=[]
low=[]
pair=[]
odd=[]

for i in (str(input())):
    if i.isupper(): up.append(i)
    elif i.islower(): low.append(i)
    elif i.isdigit() and int(i)%2==0: pair.append(i)
    else: odd.append(i)

for i in (sorted(low)+sorted(up)+sorted(odd)+sorted(pair)):
    print(i,end='')