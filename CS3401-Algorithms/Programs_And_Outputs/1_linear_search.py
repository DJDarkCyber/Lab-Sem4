def linearSearch(array, n, x):
    for i in range(0, n):
        if array[i] == x:
            return 1

    return -1

import matplotlib.pyplot as plt
import time

ot = []
T = int(input("Enter no of Execution: "))
temp = 0
y = []
for j in range(0, T):
    n = int(input("Enter  n: "))
    y.append(n)
    my_list = []
    for i in range(0, n):
        ele = int(input("Enter Element : "))
        my_list.append(ele)
    elem_to_search = int(input("Enter key : "))
    print("The list is ", my_list)
    start = time.time()
    my_result = linearSearch(my_list, n, elem_to_search)
    end = time.time()
    tn = end-start
    if my_result != -1:
        print("Element found at index ", str(my_result))
    else:
        print("Element not found!")

    temp = temp + 1
    ot.append(tn)

print("Execution Time ", ot)
X = ot
Y = y
plt.plot(X, Y)
plt.show()
