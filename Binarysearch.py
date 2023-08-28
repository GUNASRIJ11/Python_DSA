def binary_search(arr, search_element, low, high):
    if low <= high:
        mid = (low + high) // 2

        if arr[mid] == search_element:
            return mid

        elif arr[mid] < search_element:
            return binary_search(arr, search_element, mid + 1, high)

        else:
            return binary_search(arr, search_element, low, mid - 1)

    return -1


arr = list(map(int, input().split()))
search_element = int(input())
result = binary_search(arr, search_element, 0, len(arr) - 1)

if result != -1:
    print("Element found at index:", result)
else:
    print("Element not found")


