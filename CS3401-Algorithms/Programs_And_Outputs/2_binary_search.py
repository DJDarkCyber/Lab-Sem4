def binary_search(my_list, low, high, elem):
    # Check base case
    if high >= low:
        mid = (high + low) // 2
        # If element is present at the middle itself
        if my_list[mid] == elem:
            return mid
        # If element is smaller than mid, then it can only be present in the left subarray
        elif my_list[mid] > elem:
            return binary_search(my_list, low, mid - 1, elem)
        # Else the element can only be present in the right subarray
        else:
            return binary_search(my_list, mid + 1, high, elem)
    else:
        # Element is not present in the array
        return -1

# Test array
import matplotlib.pyplot as plt
import time

ot = []
yvalue = []
T = int(input("Enter number of executions: "))

for j in range(T):
    n = int(input("Enter n: "))
    yvalue.append(n)
    my_list = []

    for i in range(n):
        ele = int(input("Enter element: "))
        my_list.append(ele)

    elem_to_search = int(input("Enter key: "))

    print("The list is:")
    for i in range(n):
        print(my_list[i])

    start = time.time()
    my_result = binary_search(my_list, 0, len(my_list) - 1, elem_to_search)
    end = time.time()
    tn = end - start

    if my_result != -1:
        print("Element found at index", my_result)
    else:
        print("Element not found!")

    ot.append(tn)
    print("Execution time:", ot)

# Plot a graph
x = ot
y = yvalue
plt.plot(x, y)
plt.show()
