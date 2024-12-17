def quick_sort(arr):
   
    if len(arr) <= 1:
        return arr
    else:
       
        pivot = arr[len(arr) // 2]
        
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        
        return quick_sort(left) + middle + quick_sort(right)

arr = [9, 7, 5, 11, 12, 2, 14, 3, 10, 6]
sorted_arr = quick_sort(arr)
print("Відсортований список:", sorted_arr)
