# 재시작된 커널 환경에서 다시 코드 실행

import matplotlib.pyplot as plt
import random
import time
import tracemalloc
import csv

# 정렬 알고리즘 정의
def bubble_sort(arr):
    arr = arr.copy()
    for i in range(len(arr) - 1):
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def selection_sort(arr):
    arr = arr.copy()
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def insertion_sort(arr):
    arr = arr.copy()
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    less = quick_sort([x for x in arr[1:] if x < pivot])
    greater = quick_sort([x for x in arr[1:] if x >= pivot])
    return less + [pivot] + greater

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged += left[i:]
    merged += right[j:]
    return merged

# 시간 및 메모리 측정 함수 (한 번에)
def measure_time_and_memory(sort_func, arr):
    tracemalloc.start()
    start = time.time()
    sort_func(arr)
    end = time.time()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return round(end - start, 5), round(peak / 1024, 2)

# 데이터 크기
data_sizes = [10, 20, 30, 50, 100, 150, 200, 300, 400, 500, 1000, 1500, 2000, 2500, 3000]

# 정렬 알고리즘 매핑
sorts = {
    "Bubble": bubble_sort,
    "Selection": selection_sort,
    "Insertion": insertion_sort,
    "Quick": quick_sort,
    "Merge": merge_sort
}

# 결과 저장
time_results = {name: [] for name in sorts}
memory_results = {name: [] for name in sorts}

# 정렬 수행 및 측정
for size in data_sizes:
    data = [random.randint(0, size) for _ in range(size)]
    for name, func in sorts.items():
        t, m = measure_time_and_memory(func, data)
        time_results[name].append(t)
        memory_results[name].append(m)

# CSV 저장
with open("정렬_성능결과.csv", "w", newline='', encoding="utf-8-sig") as f:
    writer = csv.writer(f)
    writer.writerow(["Algorithm", "Data Size", "Time (s)", "Memory (KB)"])
    for name in sorts:
        for i, size in enumerate(data_sizes):
            writer.writerow([name, size, time_results[name][i], memory_results[name][i]])

# 색상 설정
colors = {
    "Bubble": "blue",
    "Selection": "orange",
    "Insertion": "green",
    "Quick": "red",
    "Merge": "purple"
}

# 그래프 그리기
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

for name in sorts:
    x = data_sizes
    y_time = time_results[name]
    y_mem = memory_results[name]
    ax1.plot(x, y_time, label=name, color=colors[name], marker='o')
    ax2.plot(x, y_mem, label=name, color=colors[name], marker='s')

    # 각 데이터 포인트에 값 주석 추가
    for i in range(len(x)):
        ax1.annotate(f"{y_time[i]}", (x[i], y_time[i]), textcoords="offset points", xytext=(0,5), ha='center', fontsize=8)
        ax2.annotate(f"{y_mem[i]}", (x[i], y_mem[i]), textcoords="offset points", xytext=(0,5), ha='center', fontsize=8)

# 시간 복잡도 그래프 설정
ax1.set_title("Execution Time by Sorting Algorithm")
ax1.set_xlabel("Number of Data")
ax1.set_ylabel("Time (s)")
ax1.legend()

# 메모리 복잡도 그래프 설정
ax2.set_title("Memory Usage by Sorting Algorithm")
ax2.set_xlabel("Number of Data")
ax2.set_ylabel("Memory (KB)")
ax2.legend()

plt.tight_layout()
plt.show()
