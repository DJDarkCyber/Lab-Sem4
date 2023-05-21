def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    # Create temp arrays
    L = [0] * n1
    R = [0] * n2

    # Copy data to temp arrays L[] and R[]
    for i in range(n1):
        L[i] = arr[l + i]
    for j in range(n2):
        R[j] = arr[m + 1 + j]

    # Merge the temp arrays back into arr[l..r]
    i = 0  # Initial index of first subarray
    j = 0  # Initial index of second subarray
    k = l  # Initial index of merged subarray

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # Copy the remaining elements of L[], if there are any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    # Copy the remaining elements of R[], if there are any
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

def mergeSort(arr, l, r):
    if l < r:
        m = l + (r - l) // 2

        # Sort first and second halves
        mergeSort(arr, l, m)
        mergeSort(arr, m + 1, r)

        merge(arr, l, m, r)

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
    mergeSort(arr, 0, n - 1)
    end = time.time()

    tn = end - start
    print("\nSorted array is")
    for i in range(n):
        print("%d" % arr[i], end=" ")

    temp += 1
    ot.append(tn)
    print("\nExecution Time:", tn)

# Plot a graph
Y = ot
plt.plot(X, Y)
plt.show()
