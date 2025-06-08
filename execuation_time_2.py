#1. 실행시간 측정(2) 여러개 샘플끼리 비교하기
import time
import random as r

def FindMax(seq):
    max=-1
    for element in seq:
        if element>max:
            max=element
    return max

n_samp=[10**5,10**6,10**7,10**8]
for samp in n_samp:
    t_begin=time.time()
    number=[r.randint(0,samp) for i in range(samp)]
    FindMax(number)
    t_end=time.time()
    print(f"{samp}개의 데이터 최댓값 찾기 시간={t_end-t_begin}sec")


