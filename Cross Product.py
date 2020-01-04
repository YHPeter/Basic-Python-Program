import numpy as np
import pandas as pd
n=10
def func(*args):
    size = len(args)
    idx = 1
    i = int(args[0])
    while idx < size:
        j = args[idx]
        # 用辗转相除法求i,j的最大公约数m
        b = i if i < j else j  # i，j中较小那个值
        a = i if i > j else j  # i,j中较大那个值
        r = b  # a除以b的余数
        while(r != 0):
            r = a % b
            if r != 0:
               a = b
               b = r
        f = i*j/b  # 两个数的最小公倍数
        i = f
        idx += 1
    return f    

while n:
    list1,list2 = [],[]
    try:
        for i in range(3):
            j = float(input(i+1))
            list1.append(j)
        for i in range(3):
            j = float(input(i+1))
            list2.append(j)
    except:
        continue

    print(np.array(list1),np.array(list2))
    print(np.cross(np.array(list1),np.array(list2)))