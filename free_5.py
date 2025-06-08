import matplotlib.pyplot as plt
import random
import time
import tracemalloc
import csv

# 정렬 알고리즘 구현
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

# 성능 측정 함수
def measure(sort_func, arr):
    tracemalloc.start()
    start = time.time()
    sort_func(arr)
    end = time.time()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return round(end - start, 5), round(peak / 1024, 2)

# 테스트할 데이터 크기
data_sizes = [0, 10, 100, 500, 1000, 3000, 5000, 8000, 10000]

# 정렬 함수와 이름 매핑
sorts = {
    "버블": bubble_sort,
    "선택": selection_sort,
    "삽입": insertion_sort,
    "퀵": quick_sort,
    "병합": merge_sort
}

# 결과 저장
results = []

# 실행 및 결과 저장
for size in data_sizes:
    data = [random.randint(0, size) for _ in range(size)]
    for name, func in sorts.items():
        if name in ['버블', '선택', '삽입'] and size > 3000:
            results.append([name, size, None, None])
            continue
        t, m = measure(func, data)
        results.append([name, size, t, m])

# CSV 저장
results_sorted = sorted(results, key=lambda x: (x[1], x[0]))
with open("정렬_성능결과.csv", "w", newline='', encoding="utf-8-sig") as f:
    writer = csv.writer(f)
    writer.writerow(["정렬", "데이터 수", "실행 시간 (s)", "메모리 (KB)"])
    writer.writerows(results_sorted)

# 색상
colors = {"버블": "blue", "선택": "orange", "삽입": "green", "퀵": "red", "병합": "purple"}

# 그래프용 데이터 구성
time_results = {name: [] for name in sorts}
memory_results = {name: [] for name in sorts}

for name in sorts:
    for size in data_sizes:
        match = next((row for row in results if row[0] == name and row[1] == size), None)
        if match and match[2] is not None:
            time_results[name].append(match[2])
            memory_results[name].append(match[3])
        else:
            time_results[name].append(None)
            memory_results[name].append(None)

# 그래프
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 7))

for name in sorts:
    x = [size for i, size in enumerate(data_sizes) if time_results[name][i] is not None]
    y_time = [time_results[name][i] for i in range(len(data_sizes)) if time_results[name][i] is not None]
    y_mem = [memory_results[name][i] for i in range(len(data_sizes)) if memory_results[name][i] is not None]

    ax1.plot(x, y_time, label=name, color=colors[name], marker='o')
    ax2.plot(x, y_mem, label=name, color=colors[name], marker='s')

    # 주석 추가 (시간 그래프)
    for xi, yi in zip(x, y_time):
        ax1.annotate(f"{xi}\n{yi}s", (xi, yi), textcoords="offset points", xytext=(0,5), ha='center', fontsize=8)

    # 주석 추가 (메모리 그래프)
    for xi, yi in zip(x, y_mem):
        ax2.annotate(f"{xi}\n{yi}KB", (xi, yi), textcoords="offset points", xytext=(0,5), ha='center', fontsize=8)

# 설정
ax1.set_title("정렬 알고리즘별 실행 시간", fontsize=13)
ax1.set_xlabel("데이터 수")
ax1.set_ylabel("시간 (초)")
ax1.legend(title="정렬 방식")

ax2.set_title("정렬 알고리즘별 메모리 사용량", fontsize=13)
ax2.set_xlabel("데이터 수")
ax2.set_ylabel("메모리 (KB)")
ax2.legend(title="정렬 방식")

plt.tight_layout()
plt.savefig("정렬_그래프_주석포함.png")
plt.show()
