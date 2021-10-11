
import math
import os
import random
import re
import sys
import datetime as dt

# Complete the time_delta function below.
def time_delta(t1, t2):
    formatofecha='%a %d %b %Y %H:%M:%S %z'  
    return(str(int(abs(((dt.datetime.strptime(t1,formatofecha))-(dt.datetime.strptime(t2,formatofecha))).total_seconds()))))
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input())
    for t_itr in range(t):
        t1 = input()
        t2 = input()
        delta = time_delta(t1, t2)
        fptr.write(delta + '\n')
    fptr.close()
