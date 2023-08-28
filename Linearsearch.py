def linear_search(arr, search_element):
    for element in arr:
        if element == search_element:
            print("The element is found")
            return
        
    print("The element is not found")

arr = list(map(int, input().split()))
element = int(input())
linear_search(arr, element)
