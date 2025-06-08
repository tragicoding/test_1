#실행시간 측정(3): 최댓값 갱신 횟수수

import time
from random import randint

def FindMax(seq):
    cur=0
    max=-1
    for element in seq:
        if element>max:
            max=element
            cur+=1
    return max,cur

sample=[10**4,10**5,10**6,10**7,10**8]
for sample_number in sample:
    number=[randint(0,k) for k in range(sample_number)]
    t_begin=time.time()
    max,cur=FindMax(number)
    t_end=time.time()
    print(f"elapsed time of {sample_number}={t_end-t_begin}, max={max},cur={cur}")



