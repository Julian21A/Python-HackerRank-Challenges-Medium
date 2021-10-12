import collections;

dic = collections.OrderedDict()
for i in range(int(input())):
    txt=input()
    if txt in dic: dic[txt]+=1
    else: dic[txt]=1
print(len(dic));

for k,v in dic.items():
    print(v,end=" ")