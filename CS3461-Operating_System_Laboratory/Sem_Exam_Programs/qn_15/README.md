# 15. a. Write a shell program to find the area of rectangle by getting length and breadth from user.
# b. Consider a disk queue with requests for I/O to blocks on cylinders 4, 34, 10, 7, 19, 73, 2, 15, 6, 20. The SSTF scheduling algorithm is used. The head is initially at cylinder number 50. The cylinders are numbered from 0 to 100. Find the total head movement (in number of cylinders) incurred while servicing these requests using C.

## a. Write a shell program to find the area of rectangle by getting length and breadth from user.

`$ bash rectangle.sh`

OUTPUT:
```
Enter the length of the rectangle: 4
Enter the breadth of the rectangle: 2
Area of the rectangle: 8 square units
```

## b. Consider a disk queue with requests for I/O to blocks on cylinders 4, 34, 10, 7, 19, 73, 2, 15, 6, 20. The SSTF scheduling algorithm is used. The head is initially at cylinder number 50. The cylinders are numbered from 0 to 100. Find the total head movement (in number of cylinders) incurred while servicing these requests using C.

`$ cc sstf.c -o sstf`

OUTPUT:

```
Enter the number of Requests: 10
Enter the Requests sequence: 4
34
10
7
19
73
2
15
6
20
Enter initial head position: 50
Total head movement is 119
```
