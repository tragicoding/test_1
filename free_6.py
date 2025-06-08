#파이썬의 동적 할당 실험
#생성하고 삭제하는 시간과 그냥 생성만 하는 시간이 같다면 자동할당
#생성하고 삭제하는 시간이 그냥 생성만 하는 시간과 다르다면 동적할당

import time
import gc

number_elements=100000
number_repeat=100000

def allocation():
    for i in range(number_repeat):
        l=[0]*number_elements

def allocation_1():
    for i in range(number_repeat):
        l=[0]*number_elements
        del l
        gc.collect()

#배열을 생성만 하는 시간간S
time_begin=time.time()
allocation()
time_end=time.time()
time_make=time_end-time_begin

#배열을 생성하고 삭제하는 시간간
time_begin_1=time.time()
allocation_1()
time_end_1=time.time()
time_make_1=time_end_1-time_begin_1

print(f"생성만 하는 시간={time_make} 생성하고 삭제하는 시간={time_make_1}")




