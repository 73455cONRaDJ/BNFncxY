# 代码生成时间: 2025-09-18 05:15:07
import numpy as np

# 定义排序算法的函数
class SortingAlgorithms:
    """
    排序算法的实现。
    """
    def bubble_sort(self, arr):
        """冒泡排序算法实现。

        参数：
        arr (np.ndarray): 需要排序的数组。

        返回：
        np.ndarray: 排序后的数组。
        """
        n = len(arr)
        for i in range(n):
            for j in range(0, n-i-1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr

    def selection_sort(self, arr):
        """选择排序算法实现。

        参数：
        arr (np.ndarray): 需要排序的数组。

        返回：
        np.ndarray: 排序后的数组。
        """
        n = len(arr)
        for i in range(n):
            min_idx = i
            for j in range(i+1, n):
                if arr[min_idx] > arr[j]:
                    min_idx = j
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
        return arr

    def insertion_sort(self, arr):
        """插入排序算法实现。

        参数：
        arr (np.ndarray): 需要排序的数组。

        返回：
        np.ndarray: 排序后的数组。
        """
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and key < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
        return arr

# 实例化排序算法类
sorting_algorithms = SortingAlgorithms()

# 生成随机数组
np.random.seed(0)  # 设置随机种子以获得可复现的结果
array_to_sort = np.random.randint(1, 100, size=10)

# 调用排序函数
sorted_array_bubble = sorting_algorithms.bubble_sort(array_to_sort.copy())
sorted_array_selection = sorting_algorithms.selection_sort(array_to_sort.copy())
sorted_array_insertion = sorting_algorithms.insertion_sort(array_to_sort.copy())

# 打印结果
print("Original array: ", array_to_sort)
print("Sorted array (Bubble Sort): ", sorted_array_bubble)
print("Sorted array (Selection Sort): ", sorted_array_selection)
print("Sorted array (Insertion Sort): ", sorted_array_insertion)