import math
import os
import random
import re
import sys
import collections 

if __name__ == '__main__':
    s = input().strip()
    scount = collections.Counter(sorted(s)).most_common()
    scount = sorted(scount, key=lambda x: (x[1] * -1, x[0]))
    for i in range(0, 3):
        print(scount[i][0], scount[i][1])