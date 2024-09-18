def bubble_sort(arr):
    n = len(arr)
    # Traverse through all elements
    for i in range(n):
        swapped = False
        # Last i elements are already sorted
        for j in range(0, n - i - 1):
            # Swap if the element is greater than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        # If no two elements were swapped, the array is already sorted
        if not swapped:
            break
    return arr
