# def partition(low,high):

#     pivot = arr[low]
#     i = low
#     j = high
#     while(i<j):
#         i+=1
#         while True:
#             if arr[i]<=pivot:
#                 break
#             i+=1
        
#         j-=1
#         while True:
#             if arr[j] >pivot:
#                 break
#             j-=1

#         if i<j:
#             arr[i],arr[j] = arr[j],arr[i] 

#     arr[low],arr[j] = arr[j],arr[low]
#     return j
        
    

# def quicksort(arr,low,high):
#     if low<high:
#         j = partition(low,high)
#         quicksort(arr,low, j-1 )
#         quicksort(arr,j+1, high)
   




# arr  = [2,9,5,7,3,8,3]
# res = quicksort(arr,0,len(arr)-1)
# print(res)




def partition(arr, low, high):
    pivot = arr[low]
    i = low + 1
    j = high

    while True:
        while i <= j and arr[i] <= pivot:
            i += 1
        while i <= j and arr[j] > pivot:
            j -= 1
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            break

    arr[low], arr[j] = arr[j], arr[low]
    return j


def quicksort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        quicksort(arr, low, pivot_index - 1)
        quicksort(arr, pivot_index + 1, high)
    return arr


arr = [2, 9, 5, 7, 3, 8,0,1,4]
quicksort(arr, 0, len(arr) - 1)
print(arr)
