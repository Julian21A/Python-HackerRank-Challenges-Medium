n=list(map(int,input().split()))
arr=map(int,input().split())
fact1=set(map(int,input().split()))
fact2=set(map(int,input().split()))
happiness=0
for i in arr:
    if i in fact1:
        happiness+=1
    if i in fact2:
        happiness-=1
print(happiness)
    