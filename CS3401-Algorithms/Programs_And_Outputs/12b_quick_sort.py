def partition(array, low, high):
    # Choose the rightmost element as pivot
    pivot = array[high]
    # Pointer for the greater element
    i = low - 1
    # Traverse through all elements
    # Compare each element with pivot
    for j in range(low, high):
        if array[j] <= pivot:
            # If element smaller than pivot is found
            # Swap it with the greater element pointed by i
            i = i + 1
            # Swapping element at i with element at j
            (array[i], array[j]) = (array[j], array[i])
    # Swap the pivot element with the greater element specified by i
    (array[i + 1], array[high]) = (array[high], array[i + 1])
    # Return the position from where partition is done
    return i + 1

# Function to perform QuickSort
def quickSort(array, low, high):
    if low < high:
        # Find pivot element such that
        # elements smaller than pivot are on the left
        # elements greater than pivot are on the right
        pi = partition(array, low, high)
        # Recursive call on the left of pivot
        quickSort(array, low, pi - 1)
        # Recursive call on the right of pivot
        quickSort(array, pi + 1, high)

# Driver code to test above
import matplotlib.pyplot as plt
import time

ot = []
T = int(input("Enter the number of executions: "))
temp = 0
X = []
for j in range(T):
    n = int(input("Enter n: "))
    X.append(n)

    arr = []
    for i in range(n):
        ele = int(input("Enter Element: "))
        arr.append(ele)

    print("The list is", arr)

    start = time.time()
    quickSort(arr, 0, n - 1)
    end = time.time()

    tn = end - start
    print('Sorted Array in Ascending Order:')
    print(arr)

    temp += 1
    ot.append(tn)
    print("\nExecution Time:", tn)

# Plot a graph
Y = ot
plt.plot(X, Y)
plt.show()
