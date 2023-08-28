def bubble_sort(arr):
    n = len(arr)
    
    for i in range(n - 1):
      
        for j in range(n - i - 1):
        
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


my_list = [9, 1, 6, 8, 4, 3, 2, 0]
bubble_sort(my_list)
print(my_list)
