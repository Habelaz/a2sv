class Solution:
    def select(self, arr, i):
        smallest_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        return smallest_index
    
    def selectionSort(self, arr, n):
        for i in range(n-1):
            min_index = self.select(arr, i)
            arr[i], arr[min_index] = arr[min_index], arr[i]
