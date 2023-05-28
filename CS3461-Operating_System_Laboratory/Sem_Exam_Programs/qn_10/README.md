# 10. a. Write a shell program to display date with time.
# b. Consider a disk queue with requests for I/O to blocks on cylinders 98, 183, 41, 122, 14, 124, 65, 67. The FCFS scheduling algorithm is used. The head is initially at cylinder number 53. The cylinders are numbered from 0 to 199. Find the total head movement (in number of cylinders) incurred while servicing these requests using C.

## a. Write a shell program to display date with time.

`$ bash date_time.sh`

OUTPUT:

```
Current Date and Time
---------------------
Date: 2023-05-28
Time: 13:04:56
```

## b. Consider a disk queue with requests for I/O to blocks on cylinders 98, 183, 41, 122, 14, 124, 65, 67. The FCFS scheduling algorithm is used. The head is initially at cylinder number 53. The cylinders are numbered from 0 to 199. Find the total head movement (in number of cylinders) incurred while servicing these requests using C.

`$ cc fcfs.c -o fcfs`

OUTPUT:

```
Enter the max range of the disk: 199
Enter the size of the request queue: 8
Enter the queue of disk positions to be read: 98
183
41
122
14
124
65
67
Enter the initial head position: 53
Disk head moves from 53 to 98 with seek 45
Disk head moves from 98 to 183 with seek 85
Disk head moves from 183 to 41 with seek 142
Disk head moves from 41 to 122 with seek 81
Disk head moves from 122 to 14 with seek 108
Disk head moves from 14 to 124 with seek 110
Disk head moves from 124 to 65 with seek 59
Disk head moves from 65 to 67 with seek 2
Total Seek Time is 632
Average Seek Time is 79.000000

```
