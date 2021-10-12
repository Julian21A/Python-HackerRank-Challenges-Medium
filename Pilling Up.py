import collections

N = int(input())

for _ in range(N):
    flag = True
    input()
    dq = collections.deque(map(int, input().strip().split()))
    if(dq[0] >= dq[-1]): max = dq.popleft()
    else: max = dq.pop()
    while dq:
        if(len(dq)==1):
            if(dq[0] <= max): break
            else:
                flag = False
                break
        else:
            if(dq[0]<=max and dq[-1]<=max):
                if(dq[0]>=dq[-1]): max = dq.popleft()
                else: max = dq.pop()
            elif(dq[0]<=max): max = dq.popleft()
            elif(dq[-1]<=max): max = dq.pop()
            else:
                flag = False
                break
    if flag: print("Yes")
    else: print("No")