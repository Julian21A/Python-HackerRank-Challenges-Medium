def merge_the_tools(string, k):
    for i in zip(*[iter(string)]*k):
        substring=dict()
        print(''.join([substring.setdefault(c,c)for c in i if c not in substring]))
        

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)