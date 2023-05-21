def find_min_max(arr):
    n = len(arr)

    # Base case for recursion
    if n == 1:
        return arr[0], arr[0]

    # Recursive case
    elif n == 2:
        return (arr[0], arr[1]) if arr[0] < arr[1] else (arr[1], arr[0])

    else:
        mid = n // 2
        left_min, left_max = find_min_max(arr[:mid])
        right_min, right_max = find_min_max(arr[mid:])

        return min(left_min, right_min), max(left_max, right_max)

# Input
arr = [2, 7, 3, 6, 5, 1, 9, 4, 8]
min_val, max_val = find_min_max(arr)
print("Minimum:", min_val)
print("Maximum:", max_val)
