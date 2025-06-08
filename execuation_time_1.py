#execuation time(1)
#알고리즘 성능 측정의 첫번째 방법 1. 실행시간 측정

import time
import random as r

def find_max(seq):
    max=-1
    for element in seq:
        if element>max:
            max=element
    return max

t_begin=time.time()
n_samp=10**8
number=[r.randint(0,10**8) for i in range(n_samp)]
find_max(number)
t_end=time.time()
print("elapsed time=",t_end-t_begin,"sec")