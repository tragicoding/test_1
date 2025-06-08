import time
from random import randint

def Findmax(seq):
    cur=0
    max=-1
    for element in seq:
        if element>max:
            max=element
            cur+=1
    return max,cur

n_samp=[10**5,10**6,10**7,10**8]
for samp in n_samp:
    number=[randint(0,samp) for samp in range(samp)]
    max,cur=Findmax(number)
    print(f"최댓값={max},갱신횟수={cur}")    