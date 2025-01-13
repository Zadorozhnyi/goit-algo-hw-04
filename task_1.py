import timeit
import random
import matplotlib.pyplot as plt
import pandas as pd

# Merge Sort implementation
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# Insertion Sort implementation
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Timsort (using Python's built-in sorted)
def timsort(arr):
    return sorted(arr)

# Test function for timing
def measure_time(sort_function, data):
    return timeit.timeit(lambda: sort_function(data.copy()), number=1)

# Generate datasets
sizes = [10**3, 10**4, 10**5, 10**6]
random_data = {size: [random.randint(0, 100000) for _ in range(size)] for size in sizes}

# Measure execution times
merge_times = []
insertion_times = []
timsort_times = []

for size in sizes:
    data = random_data[size]
    merge_times.append(measure_time(merge_sort, data))
    
    # Insertion sort is inefficient for large sizes
    if size <= 10**4:
        insertion_times.append(measure_time(insertion_sort, data))
    else:
        insertion_times.append(None)
    timsort_times.append(measure_time(timsort, data))

# Display numerical results
results = pd.DataFrame({
    'Size': sizes,
    'Merge Sort Time (s)': merge_times,
    'Insertion Sort Time (s)': insertion_times,
    'Timsort Time (s)': timsort_times
})

results.to_csv("sorting_algorithm_comparison.csv", index=False)
print("Results saved to 'sorting_algorithm_comparison.csv'.")
print(results)

# Plot results
plt.figure(figsize=(10, 6))
plt.plot(sizes, merge_times, label='Merge Sort', marker='o')
plt.plot(sizes[:len(insertion_times)], insertion_times, label='Insertion Sort', marker='o')
plt.plot(sizes, timsort_times, label='Timsort (Python sorted)', marker='o')
plt.xscale('log')
plt.yscale('log')
plt.xlabel('Input Size (log scale)')
plt.ylabel('Execution Time (log scale)')
plt.title('Comparison of Sorting Algorithms')
plt.legend()
plt.grid(True)
plt.show()
