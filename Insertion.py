def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


my_list = [9, 1, 6, 8, 4, 3, 2, 0]
insertion_sort(my_list)
print(my_list)
