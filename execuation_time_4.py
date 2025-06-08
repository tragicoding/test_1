#numpy로 측정하기
#numpy가 python 보다 성능이 더 뛰어남.

import time
import numpy as np

duration=[]
for n_samp in [10**5,10**6,10**7,10**8]:
    numbers=np.random.randint(0,n_samp,size=n_samp)
    t_begin=time.time()
    maxval=np.max(numbers)
    t_end=time.time()
    duration.append(t_end-t_begin)
    print(duration)