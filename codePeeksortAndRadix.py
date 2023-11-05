import time
import tracemalloc

# Implementasi Peeksort
def peeksort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_half = peeksort(left_half)
    right_half = peeksort(right_half)

    return merge(left_half, right_half)

def merge(left, right):
    result = []
    left_idx, right_idx = 0, 0

    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1

    result.extend(left[left_idx:])
    result.extend(right[right_idx:])
    return result


# Implementasi Radix Sort dengan Counting Sort
def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    max_num = max(arr)
    exp = 1
    while max_num // exp > 0:
        counting_sort(arr, exp)
        exp *= 10


# Kompleksitas Waktu
def countKompleksitas(file, algorithm):
    tracemalloc.start()
    with open(file, 'r') as f:
        f = f.readlines()
    arr = [int(line.strip()) for line in f]

    if algorithm == 'peeksort':
        start_time = time.perf_counter()
        peeksort(arr)
        end_time = time.perf_counter()
        execution_time = (end_time - start_time) * 1000
    elif algorithm == 'radixsort':
        start_time = time.perf_counter()
        radix_sort(arr)
        end_time = time.perf_counter()
        execution_time = (end_time - start_time) * 1000

    print('Execution time untuk file {} dengan algoritma {} adalah {} ms'.format(file, algorithm, execution_time))

    print('Traced Memory (Current, Peak):', tracemalloc.get_traced_memory())
    tracemalloc.reset_peak()
    tracemalloc.stop()
    print()

files = ['smallSortedNumber.txt', 'smallRandomNumber.txt', 'smallReversedNumber.txt', 'mediumSortedNumber.txt', 'mediumRandomNumber.txt', 'mediumReversedNumber.txt', 'largeSortedNumber.txt', 'largeRandomNumber.txt', 'largeReversedNumber.txt']

for file in files:
    countKompleksitas(file, 'peeksort')
    countKompleksitas(file, 'radixsort')
    print()