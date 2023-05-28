# 8. a. Write a shell program to find Factorial of a number.
# b. Consider the reference string 6, 1, 1, 2, 0, 3, 4, 6, 0, 2, 1, 2, 1, 2, 0, 3, 2, 1, 2, 0 for a memory with three frames and calculate number of page faults by using FIFO in C.

## a. Write a shell program to find Factorial of a number.

`$ bash factorial.sh`

OUTPUT:
```
Enter a Number
5
The Factorial of the given Number is 120
```

## b. Consider the reference string 6, 1, 1, 2, 0, 3, 4, 6, 0, 2, 1, 2, 1, 2, 0, 3, 2, 1, 2, 0 for a memory with three frames and calculate number of page faults by using FIFO in C.

`$ cc fifo_page.c -o fifo_page`

`$ ./fifo_page`

OUTPUT:

```
FIFO Page Replacement

Enter the number of pages: 20

Enter the page numbers:
6
1
1
2
0
3
4
6
0
2
1
2
1
2
0
3
2
1
2
0

Enter the number of frames: 3

Ref String      Page Frames
6               6       -1      -1
1               6       1       -1
1
2               6       1       2
0               0       1       2
3               0       3       2
4               0       3       4
6               6       3       4
0               6       0       4
2               6       0       2
1               1       0       2
2
1
2
0
3               1       3       2
2
1
2
0               1       3       0
Page Faults: 12

```
