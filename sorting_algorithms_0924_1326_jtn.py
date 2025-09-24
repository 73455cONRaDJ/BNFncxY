# 代码生成时间: 2025-09-24 13:26:04
import numpy as np"""
Sorting algorithms implementation using Python and NumPy.

The program contains multiple sorting algorithms and provides error handling,
# 增强安全性
along with documentation and comments for clarity and maintainability.
"""

# Define a function to perform bubble sort
# NOTE: 重要实现细节
def bubble_sort(arr):
    n = len(arr)
    # Traverse through all array elements
# NOTE: 重要实现细节
    for i in range(n):
        # Last i elements are already in place, no need to check them
# 扩展功能模块
        for j in range(0, n-i-1):
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Define a function to perform selection sort
def selection_sort(arr):
    n = len(arr)
    # Traverse through all array elements
    for i in range(n):
        # Find the minimum element in remaining unsorted array
        min_idx = i
        for j in range(i+1, n):
            if arr[min_idx] > arr[j]:
# 优化算法效率
                min_idx = j
# 增强安全性
        # Swap the found minimum element with the first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# Define a function to perform insertion sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        # Move elements of arr[0..i-1], that are greater than key, to one position ahead
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr
# 优化算法效率

# Define a function to perform merge sort
def merge_sort(arr):
    if len(arr) > 1:
        # Finding the midpoint
        mid = len(arr)//2
# TODO: 优化性能
        # Dividing the array elements into 2 halves
# 改进用户体验
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0
        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
# TODO: 优化性能
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
# 优化算法效率
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

    return arr

# Define a function to perform quick sort
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
# 添加错误处理
    else:
# 增强安全性
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)

# Define a function to sort array using NumPy
def numpy_sort(arr):
# 优化算法效率
    return np.sort(arr)
# 扩展功能模块

# Example usage
if __name__ == '__main__':
    arr = np.array([64, 34, 25, 12, 22, 11, 90])
# 添加错误处理
    
    try:
        print("Original array: ", arr)
        print("Sorted array using bubble sort: ", bubble_sort(arr.copy()))
        print("Sorted array using selection sort: ", selection_sort(arr.copy()))
        print("Sorted array using insertion sort: ", insertion_sort(arr.copy()))
        print("Sorted array using merge sort: ", merge_sort(arr.copy()))
        print("Sorted array using quick sort: ", quick_sort(arr.copy()))
        print("Sorted array using NumPy: ", numpy_sort(arr.copy()))
    except Exception as e:
        print("An error occurred: ", str(e))