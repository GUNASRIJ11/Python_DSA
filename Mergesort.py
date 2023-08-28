# def merge_sort(arr):
#     if len(arr) <= 1:
#         return arr
    
#     mid = len(arr) // 2
#     left_half = arr[:mid]
#     right_half = arr[mid:]
    
#     left_half = merge_sort(left_half)
#     right_half = merge_sort(right_half)
    
#     return merge(left_half, right_half)

# def merge(left, right):
#     merged = []
#     i = j = 0
    
#     while i < len(left) and j < len(right):
#         if left[i] <= right[j]:
#             merged.append(left[i])
#             i += 1
#         else:
#             merged.append(right[j])
#             j += 1
    
#     while i < len(left):
#         merged.append(left[i])
#         i += 1
    
#     while j < len(right):
#         merged.append(right[j])
#         j += 1
    
#     return merged


# my_list = [9, 1, 6, 8, 4, 3, 2, 0]
# sorted_list = merge_sort(my_list)
# print(sorted_list)





def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        merge(arr, left, right)


def merge(arr, left, right):
    i = j = k = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i+=1

        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1


    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1


arr = [2, 9, 5, 7, 3, 8, 0, 1, 4]
merge_sort(arr)
print(arr)
