import time
import random
import tracemalloc

# 메뉴 출력
def menu_arr():
    print("데이터 크기를 선택하세요:")
    print("1: 10^1")
    print("2: 10^2")
    print("3: 10^3")
    print("4: 10^4")
    print("5: 10^5")
    print("6: 10^6")
    print("7: 10^7")
    print("8: 10^8")

# 데이터 크기 선택 입력
def input_arr_size():
    element = int(input("선택 (1~8): "))
    return element

# 배열 생성
def make_arr(arr_number):
    return [random.randint(0, arr_number + 1) for _ in range(arr_number)]

# 성능 측정 함수
def measure_performance(sort_func, arr):
    tracemalloc.start()
    start_time = time.time()
    sort_func(arr)
    end_time = time.time()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    execution_time = end_time - start_time
    execution_memory = peak / 1024  # KB
    return execution_time, execution_memory

# 버블 정렬
def burble(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - 1, i, -1):
            if arr[j - 1] > arr[j]:
                arr[j - 1], arr[j] = arr[j], arr[j - 1]

# 선택 정렬
def selection(arr):
    n = len(arr)
    for i in range(n - 1):
        im = i
        for j in range(i + 1, n):
            if arr[j] < arr[im]:
                im = j
        arr[i], arr[im] = arr[im], arr[i]

# 삽입 정렬
def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        cur = arr[i]
        j = i
        while j > 0 and arr[j - 1] > cur:
            arr[j] = arr[j - 1]
            j -= 1
        arr[j] = cur

# 퀵 정렬 (비파괴)
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    less = [x for x in arr[1:] if x < pivot]
    greater = [x for x in arr[1:] if x >= pivot]
    return quick_sort(less) + [pivot] + quick_sort(greater)

# 병합 정렬 (비파괴)
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# 메인 실행 함수
def main():
    menu_arr()
    size_choice = input_arr_size()

    sizes = {i: 10**i for i in range(1, 9)}
    arr_size = sizes.get(size_choice, 10)
    original_array = make_arr(arr_size)

    sort_list = [
        ("버블", burble),
        ("선택", selection),
        ("삽입", insertion_sort),
        ("퀵", lambda arr: quick_sort(arr)),      # 비파괴 정렬
        ("병합", lambda arr: merge_sort(arr))     # 비파괴 정렬
    ]

    for name, sort_func in sort_list:
        arr_copy = original_array.copy()
        execution_time, execution_memory = measure_performance(sort_func, arr_copy)
        print(f"[{name} 정렬] {arr_size}개 데이터 → 시간: {execution_time:.4f}초 / 메모리: {execution_memory:.2f}KB")

# 무한 루프 실행
while True:
    main()
